import os
import json
from datetime import datetime
from typing import Dict, List, Optional
from dotenv import load_dotenv 
from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# A2A Klassen für Request und Response
class Message(BaseModel):
    role: str
    content: str

class TaskRequest(BaseModel):
    messages: List[Message]
    stream: bool = False

class TaskResponse(BaseModel):
    task_id: str
    messages: List[Message]

# Einen einfachen simulierten Wetterdienst erstellen
def get_weather(location: str) -> Dict:
    # In einer echten Anwendung würdest du hier eine Wetter-API aufrufen
    # Das ist nur eine Simulation für Lernzwecke
    weather_data = {
        "Berlin": {"temp": 15, "condition": "cloudy"},
        "New York": {"temp": 22, "condition": "sunny"},
        "Tokyo": {"temp": 18, "condition": "rainy"},
        "London": {"temp": 12, "condition": "foggy"},
    }
    
    return weather_data.get(location, {"temp": 20, "condition": "unknown"})


# LLM für die Verarbeitung verwenden
def process_weather_query(query: str) -> str:
    # API-Key aus der Umgebungsvariable abrufen
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "Error: Google API key not found in environment variables"
    
    # Den LLM initialisieren
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)
    # Location aus der Anfrage extrahieren
    extract_prompt = ChatPromptTemplate.from_messages([
        ("system", "Extract the location from the weather query. Return ONLY the location name, nothing else."),
        ("user", f"{query}")
    ])
    
    extraction_chain = extract_prompt | llm
    location = extraction_chain.invoke({}).content.strip()
    
    # Wetterdaten abrufen
    weather_data = get_weather(location)
    
    # Antwort generieren
    response_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful weather assistant. Create a friendly, informative response about the weather."),
        ("user", f"Location: {location}\nTemperature: {weather_data['temp']}°C\nCondition: {weather_data['condition']}\n\nCreate a weather report.")
    ])
    
    response_chain = response_prompt | llm
    return response_chain.invoke({}).content

# FastAPI App erstellen
app = FastAPI(title="Weather A2A Agent")

# Agent-Karte definieren
@app.get("/.well-known/agent.json")
async def get_agent_card():
    return {
        "schema_version": "0.0.1",
        "name": "Weather Agent",
        "description": "An agent that provides weather information for different locations",
        "capabilities": {
            "task": {
                "task_type": "function",
                "name": "get_weather",
                "description": "Get weather information for a specific location"
            }
        }
    }

# Task-Endpunkt
@app.post("/task")
async def create_task(request: TaskRequest):
    try:
        # Letzte Benutzernachricht abrufen
        user_message = next((m.content for m in reversed(request.messages) if m.role == "user"), "")
        
        # Wetterdaten verarbeiten
        response_content = process_weather_query(user_message)
        
        # Task-ID generieren
        task_id = f"weather-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Antwort erstellen
        return TaskResponse(
            task_id=task_id,
            messages=[Message(role="assistant", content=response_content)]
        )
    except Exception as e:
        return TaskResponse(
            task_id=f"error-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            messages=[Message(role="assistant", content=f"Error processing weather request: {str(e)}")]
        )

# Server starten
if __name__ == "__main__":
    import uvicorn
    # Starte den Server auf Port 10000
    uvicorn.run(app, host="localhost", port=10000)