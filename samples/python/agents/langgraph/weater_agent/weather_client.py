import requests
import json
import os

def main():
    # Server-URL
    server_url = "http://localhost:10000"
    
    # 1. Discovery: Agent-Karte abrufen
    print("Fetching agent card...")
    response = requests.get(f"{server_url}/.well-known/agent.json")
    if response.status_code == 200:
        agent_card = response.json()
        print(f"Connected to agent: {agent_card['name']}")
        print(f"Description: {agent_card['description']}")
        print(f"Capabilities: {json.dumps(agent_card['capabilities'], indent=2)}")
    else:
        print(f"Failed to fetch agent card: {response.status_code}")
        return
    
    # 2. Interaktion mit dem Agent
    while True:
        user_input = input("\nAsk about weather (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        # Task an den Server senden
        task_request = {
            "messages": [{"role": "user", "content": user_input}],
            "stream": False
        }
        
        print("Sending request to agent...")
        response = requests.post(f"{server_url}/task", json=task_request)
        
        if response.status_code == 200:
            task_response = response.json()
            for message in task_response["messages"]:
                if message["role"] == "assistant":
                    print(f"\nAgent Response: {message['content']}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()