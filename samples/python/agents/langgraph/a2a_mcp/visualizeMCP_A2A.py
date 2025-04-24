# -------------------- MCP: TOOL SERVER --------------------

class MCPToolServer:
    """Ein einfacher MCP-Tool-Server mit Funktionen für Reiseplanung."""
    
    def __init__(self):
        self.tools = {
            "calculate_budget": self.calculate_budget,
            "get_weather": self.get_weather,
            "search_flights": self.search_flights,
            "search_hotels": self.search_hotels
        }
    
    def list_tools(self):
        """Gibt eine Liste aller verfügbaren Tools und ihrer Beschreibungen zurück."""
        tool_descriptions = {
            "calculate_budget": {
                "name": "calculate_budget",
                "description": "Berechnet das verfügbare Budget für Aktivitäten",
                "parameters": {
                    "total_budget": "Gesamtbudget für die Reise",
                    "flight_cost": "Kosten für Flüge",
                    "hotel_cost": "Kosten für die Unterkunft"
                }
            },
            "get_weather": {
                "name": "get_weather",
                "description": "Gibt Wetterdaten für einen bestimmten Ort zurück",
                "parameters": {
                    "location": "Name des Ortes",
                    "month": "Monat (1-12)"
                }
            },
            "search_flights": {
                "name": "search_flights",
                "description": "Sucht Flüge zwischen zwei Orten",
                "parameters": {
                    "origin": "Abflugort",
                    "destination": "Zielort",
                    "date": "Reisedatum (YYYY-MM-DD)"
                }
            },
            "search_hotels": {
                "name": "search_hotels",
                "description": "Sucht Hotels an einem bestimmten Ort",
                "parameters": {
                    "location": "Name des Ortes",
                    "check_in": "Check-in-Datum (YYYY-MM-DD)",
                    "nights": "Anzahl der Übernachtungen"
                }
            }
        }
        return tool_descriptions
    
    def call_tool(self, tool_name, parameters):
        """Ruft ein Tool mit den angegebenen Parametern auf."""
        if tool_name not in self.tools:
            return {"error": f"Tool '{tool_name}' nicht gefunden"}
        
        tool = self.tools[tool_name]
        try:
            result = tool(**parameters)
            return {"result": result}
        except Exception as e:
            return {"error": str(e)}
    
    # Implementierung der eigentlichen Tools
    
    def calculate_budget(self, total_budget, flight_cost, hotel_cost):
        """Berechnet das verfügbare Budget für Aktivitäten."""
        activities_budget = total_budget - flight_cost - hotel_cost
        return {
            "total_budget": total_budget,
            "flight_cost": flight_cost,
            "hotel_cost": hotel_cost,
            "activities_budget": activities_budget
        }
    
    def get_weather(self, location, month):
        """Simuliert Wetterdaten für einen bestimmten Ort."""
        weather_data = {
            "Hawaii": {
                "6": {"temp": 28, "condition": "sonnig", "rain_days": 3},
                "7": {"temp": 29, "condition": "sonnig", "rain_days": 2},
                "8": {"temp": 29, "condition": "sonnig", "rain_days": 2}
            },
            "Paris": {
                "6": {"temp": 22, "condition": "gemischt", "rain_days": 7},
                "7": {"temp": 25, "condition": "sonnig", "rain_days": 5},
                "8": {"temp": 24, "condition": "sonnig", "rain_days": 6}
            },
            "Tokyo": {
                "6": {"temp": 24, "condition": "regnerisch", "rain_days": 12},
                "7": {"temp": 28, "condition": "feucht", "rain_days": 10},
                "8": {"temp": 30, "condition": "feucht", "rain_days": 8}
            }
        }
        
        if location not in weather_data:
            return {"error": f"Keine Wetterdaten für {location} verfügbar"}
        
        if str(month) not in weather_data[location]:
            return {"error": f"Keine Wetterdaten für {location} im Monat {month}"}
        
        return {
            "location": location,
            "month": month,
            "data": weather_data[location][str(month)]
        }
    
    def search_flights(self, origin, destination, date):
        """Simuliert eine Flugsuche."""
        # In einer echten Anwendung würde hier eine API angesprochen werden
        dummy_flights = {
            "LAX-HNL": [
                {"airline": "Hawaiian", "price": 450, "duration": "5h 45m"},
                {"airline": "Delta", "price": 520, "duration": "5h 55m"},
                {"airline": "United", "price": 480, "duration": "6h 10m"}
            ],
            "JFK-CDG": [
                {"airline": "Air France", "price": 780, "duration": "7h 30m"},
                {"airline": "Delta", "price": 820, "duration": "7h 20m"},
                {"airline": "United", "price": 750, "duration": "7h 45m"}
            ]
        }
        
        route_key = f"{origin}-{destination}"
        if route_key not in dummy_flights:
            # Rückfallflüge für nicht definierte Routen
            return {
                "flights": [
                    {"airline": "Generic Air", "price": 500, "duration": "6h 0m"},
                    {"airline": "Budget Air", "price": 450, "duration": "6h 30m"}
                ]
            }
        
        return {"flights": dummy_flights[route_key]}
    
    def search_hotels(self, location, check_in, nights):
        """Simuliert eine Hotelsuche."""
        # In einer echten Anwendung würde hier eine API angesprochen werden
        dummy_hotels = {
            "Hawaii": [
                {"name": "Beach Resort", "price_per_night": 240, "rating": 4.5},
                {"name": "Tropical Paradise", "price_per_night": 320, "rating": 4.8},
                {"name": "Ocean View Lodge", "price_per_night": 180, "rating": 4.0}
            ],
            "Paris": [
                {"name": "Le Grand Hotel", "price_per_night": 270, "rating": 4.6},
                {"name": "Eiffel Apartments", "price_per_night": 210, "rating": 4.3},
                {"name": "Seine River Hotel", "price_per_night": 190, "rating": 4.1}
            ],
            "Tokyo": [
                {"name": "Sakura Inn", "price_per_night": 200, "rating": 4.4},
                {"name": "Tokyo Skyline Hotel", "price_per_night": 280, "rating": 4.7},
                {"name": "Cherry Blossom Suites", "price_per_night": 240, "rating": 4.5}
            ]
        }
        
        if location not in dummy_hotels:
            # Rückfallhotels für nicht definierte Orte
            return {
                "hotels": [
                    {"name": "Standard Hotel", "price_per_night": 150, "rating": 3.8},
                    {"name": "Comfort Inn", "price_per_night": 120, "rating": 3.5}
                ]
            }
        
        hotels = dummy_hotels[location]
        # Berechne Gesamtpreis für die Anzahl der Nächte
        for hotel in hotels:
            hotel["total_price"] = hotel["price_per_night"] * nights
        
        return {"hotels": hotels}


# -------------------- MCP: CLIENT --------------------

class MCPClient:
    """Ein vereinfachter MCP-Client, der mit dem MCP-Tool-Server kommuniziert."""
    
    def __init__(self, server):
        self.server = server
        self.available_tools = None
    
    def discover_tools(self):
        """Fragt den Server nach verfügbaren Tools und speichert sie."""
        self.available_tools = self.server.list_tools()
        return self.available_tools
    
    def call_tool(self, tool_name, parameters):
        """Ruft ein bestimmtes Tool mit den angegebenen Parametern auf."""
        if self.available_tools is None:
            self.discover_tools()
        
        if tool_name not in self.available_tools:
            return {"error": f"Tool '{tool_name}' ist nicht verfügbar"}
        
        # In einem echten System würden hier Parameter validiert
        return self.server.call_tool(tool_name, parameters)


# -------------------- A2A: SPEZIALISIERTE AGENTEN --------------------

class TravelAgent:
    """Ein spezialisierter Agent für Reisebuchungen (Flüge und Hotels)."""
    
    def __init__(self, mcp_client):
        self.mcp_client = mcp_client
        self.agent_card = {
            "name": "Travel Agent",
            "description": "Spezialist für Reisebuchungen, Flüge und Hotels",
            "skills": [
                {
                    "id": "flight_booking",
                    "name": "Flugbuchung",
                    "description": "Kann die besten Flüge für Ihre Reise finden"
                },
                {
                    "id": "hotel_booking",
                    "name": "Hotelbuchung",
                    "description": "Kann die passende Unterkunft für Ihren Aufenthalt finden"
                }
            ]
        }
    
    def process_task(self, task):
        """Verarbeitet eine delegierte Aufgabe von einem anderen Agenten."""
        message = task["message"]
        
        # Simulierte Verarbeitung der natürlichen Sprache
        if "flüge" in message.lower() and "hotel" in message.lower():
            return self.plan_travel(task)
        elif "flüge" in message.lower():
            return self.find_flights(task)
        elif "hotel" in message.lower():
            return self.find_hotels(task)
        else:
            return {
                "status": "input-required",
                "message": "Ich bin nicht sicher, was Sie suchen. Möchten Sie Flüge, Hotels oder beides?"
            }
    
    def plan_travel(self, task):
        """Plant sowohl Flüge als auch Hotels."""
        # Extrahiere Informationen aus der Nachricht
        message = task["message"]
        
        # In einem echten System würde hier NLP verwendet
        # Hier vereinfachen wir stark
        origin = "LAX" if "LAX" in message else "JFK"
        destination = "Hawaii" if "Hawaii" in message or "Maui" in message else "Paris"
        date = "2025-06-15" # Standardwert
        nights = 5 # Standardwert
        
        # MCP-Calls für Flüge und Hotels
        flights_result = self.mcp_client.call_tool("search_flights", {
            "origin": origin,
            "destination": destination,
            "date": date
        })
        
        hotels_result = self.mcp_client.call_tool("search_hotels", {
            "location": destination,
            "check_in": date,
            "nights": nights
        })
        
        # Wähle die besten Optionen aus (vereinfacht)
        best_flight = min(flights_result["result"]["flights"], key=lambda x: x["price"])
        best_hotel = max(hotels_result["result"]["hotels"], key=lambda x: x["rating"])
        
        return {
            "status": "completed",
            "result": {
                "flight": best_flight,
                "hotel": best_hotel,
                "total_cost": best_flight["price"] + best_hotel["total_price"]
            }
        }
    
    def find_flights(self, task):
        """Sucht nur Flüge."""
        # Vereinfachte Implementierung...
        message = task["message"]
        origin = "LAX" if "LAX" in message else "JFK"
        destination = "Hawaii" if "Hawaii" in message or "Maui" in message else "Paris"
        date = "2025-06-15"
        
        flights_result = self.mcp_client.call_tool("search_flights", {
            "origin": origin,
            "destination": destination,
            "date": date
        })
        
        return {
            "status": "completed",
            "result": {
                "flights": flights_result["result"]["flights"]
            }
        }
    
    def find_hotels(self, task):
        """Sucht nur Hotels."""
        # Vereinfachte Implementierung...
        message = task["message"]
        location = "Hawaii" if "Hawaii" in message or "Maui" in message else "Paris"
        check_in = "2025-06-15"
        nights = 5
        
        hotels_result = self.mcp_client.call_tool("search_hotels", {
            "location": location,
            "check_in": check_in,
            "nights": nights
        })
        
        return {
            "status": "completed",
            "result": {
                "hotels": hotels_result["result"]["hotels"]
            }
        }


class WeatherAdvisor:
    """Ein spezialisierter Agent für Wetterberatung und optimale Reisezeiten."""
    
    def __init__(self, mcp_client):
        self.mcp_client = mcp_client
        self.agent_card = {
            "name": "Weather Advisor",
            "description": "Spezialist für Wetterberatung und optimale Reisezeiten",
            "skills": [
                {
                    "id": "weather_forecast",
                    "name": "Wettervorhersage",
                    "description": "Kann Wetterbedingungen für verschiedene Orte vorhersagen"
                },
                {
                    "id": "travel_season_advice",
                    "name": "Reisezeitenberatung",
                    "description": "Empfiehlt die beste Jahreszeit für bestimmte Reiseziele"
                }
            ]
        }
    
    def process_task(self, task):
        """Verarbeitet eine delegierte Aufgabe von einem anderen Agenten."""
        message = task["message"]
        
        # Simulierte Verarbeitung der natürlichen Sprache
        if "wetter" in message.lower():
            return self.get_weather_info(task)
        elif "beste zeit" in message.lower() or "beste jahreszeit" in message.lower():
            return self.recommend_travel_season(task)
        else:
            return {
                "status": "input-required",
                "message": "Möchten Sie Wetterinformationen für einen bestimmten Ort oder eine Empfehlung für die beste Reisezeit?"
            }
    
    def get_weather_info(self, task):
        """Gibt Wetterinformationen für einen bestimmten Ort zurück."""
        message = task["message"]
        
        # Extrahiere Ort und Monat (vereinfacht)
        location = "Hawaii" if "Hawaii" in message or "Maui" in message else "Paris"
        month = 6  # Default: Juni
        
        if "juli" in message.lower():
            month = 7
        elif "august" in message.lower():
            month = 8
        
        # MCP-Call für Wetterdaten
        weather_result = self.mcp_client.call_tool("get_weather", {
            "location": location,
            "month": month
        })
        
        return {
            "status": "completed",
            "result": weather_result["result"]
        }
    
    def recommend_travel_season(self, task):
        """Empfiehlt die beste Reisezeit für ein Reiseziel."""
        message = task["message"]
        
        # Extrahiere Ort (vereinfacht)
        location = "Hawaii" if "Hawaii" in message or "Maui" in message else "Paris"
        
        # Sammle Wetterdaten für verschiedene Monate
        weather_data = {}
        for month in [6, 7, 8]:  # Juni, Juli, August
            result = self.mcp_client.call_tool("get_weather", {
                "location": location,
                "month": month
            })
            weather_data[month] = result["result"]["data"]
        
        # Bestimme den besten Monat (vereinfacht: weniger Regentage = besser)
        best_month = min(weather_data.keys(), key=lambda m: weather_data[m]["rain_days"])
        month_names = {6: "Juni", 7: "Juli", 8: "August"}
        
        return {
            "status": "completed",
            "result": {
                "best_month": best_month,
                "best_month_name": month_names[best_month],
                "reason": f"Am wenigsten Regentage ({weather_data[best_month]['rain_days']} Tage) und durchschnittlich {weather_data[best_month]['temp']}°C",
                "all_data": weather_data
            }
        }


class BudgetPlanner:
    """Ein spezialisierter Agent für Reisebudgetplanung."""
    
    def __init__(self, mcp_client):
        self.mcp_client = mcp_client
        self.agent_card = {
            "name": "Budget Planner",
            "description": "Spezialist für Reisebudgetplanung und -optimierung",
            "skills": [
                {
                    "id": "budget_calculation",
                    "name": "Budgetberechnung",
                    "description": "Kann das verfügbare Budget für Aktivitäten berechnen"
                },
                {
                    "id": "budget_optimization",
                    "name": "Budgetoptimierung",
                    "description": "Empfiehlt Möglichkeiten zur Kostenoptimierung"
                }
            ]
        }
    
    def process_task(self, task):
        """Verarbeitet eine delegierte Aufgabe von einem anderen Agenten."""
        message = task["message"]
        
        # Simulierte Verarbeitung der natürlichen Sprache
        if "budget" in message.lower() and "berechnen" in message.lower():
            return self.calculate_available_budget(task)
        elif "budget" in message.lower() and "optimieren" in message.lower():
            return self.optimize_budget(task)
        else:
            return {
                "status": "input-required",
                "message": "Möchten Sie Ihr verfügbares Budget berechnen oder Tipps zur Budgetoptimierung erhalten?"
            }
    
    def calculate_available_budget(self, task):
        """Berechnet das verfügbare Budget für Aktivitäten."""
        message = task["message"]
        
        # Extrahiere Budgetinformationen (vereinfacht)
        total_budget = 3000  # Standardwert
        
        # Suche nach Zahlen in der Nachricht
        import re
        budget_match = re.search(r'budget.*?(\d+)', message.lower())
        if budget_match:
            total_budget = int(budget_match.group(1))
        
        # Extrahiere Flug- und Hotelkosten (vereinfacht)
        flight_cost = 500  # Standardwert
        hotel_cost = 1200  # Standardwert
        
        # In einer realen Anwendung würden diese Werte aus der Nachricht extrahiert
        # oder aus früheren Ergebnissen anderer Agenten übernommen
        
        # MCP-Call für Budgetberechnung
        budget_result = self.mcp_client.call_tool("calculate_budget", {
            "total_budget": total_budget,
            "flight_cost": flight_cost,
            "hotel_cost": hotel_cost
        })
        
        activities_budget = budget_result["result"]["activities_budget"]
        
        daily_budget = activities_budget / 5  # Annahme: 5-tägige Reise
        
        return {
            "status": "completed",
            "result": {
                "total_budget": total_budget,
                "flight_cost": flight_cost,
                "hotel_cost": hotel_cost,
                "activities_budget": activities_budget,
                "daily_budget": daily_budget,
                "budget_assessment": "ausreichend" if activities_budget > 500 else "knapp"
            }
        }
    
    def optimize_budget(self, task):
        """Gibt Tipps zur Budgetoptimierung."""
        # In einer realen Anwendung würde hier komplexere Logik stehen
        return {
            "status": "completed",
            "result": {
                "optimization_tips": [
                    "Vergleichen Sie verschiedene Fluggesellschaften für bessere Preise",
                    "Erwägen Sie eine Unterkunft etwas außerhalb des Zentrums",
                    "Buchen Sie Aktivitäten im Voraus für Rabatte",
                    "Nutzen Sie öffentliche Verkehrsmittel statt Taxis"
                ]
            }
        }


# -------------------- A2A: PERSONAL ASSISTANT (KOORDINATOR) --------------------

class PersonalAssistant:
    """Der Haupt-Agent, der andere Agenten koordiniert (A2A-Koordinator)."""
    
    def __init__(self):
        # MCP-Setup
        self.mcp_server = MCPToolServer()
        self.mcp_client = MCPClient(self.mcp_server)
        
        # A2A-Setup: Spezialisierte Agenten
        self.travel_agent = TravelAgent(self.mcp_client)
        self.weather_advisor = WeatherAdvisor(self.mcp_client)
        self.budget_planner = BudgetPlanner(self.mcp_client)
        
        # Aufgabenverfolgung
        self.tasks = {}
    
    def process_request(self, user_message):
        """Verarbeitet eine Benutzeranfrage und delegiert an spezialisierte Agenten."""
        print(f"\n[Personal Assistant] Verarbeite Anfrage: '{user_message}'")
        
        # Simuliertes Verstehen der Benutzerabsicht
        # In einer realen Anwendung würde hier NLP verwendet
        
        # Entscheide, welche Agenten relevant sind
        relevant_agents = []
        
        if any(word in user_message.lower() for word in ["reise", "urlaub", "trip", "hawaii", "paris", "flug", "hotel"]):
            relevant_agents.append(self.travel_agent)
        
        if any(word in user_message.lower() for word in ["wetter", "klima", "regen", "sonnig", "temperatur", "beste zeit"]):
            relevant_agents.append(self.weather_advisor)
        
        if any(word in user_message.lower() for word in ["budget", "kosten", "geld", "ausgaben", "sparen"]):
            relevant_agents.append(self.budget_planner)
        
        # Wenn keine relevanten Agenten gefunden wurden, alle einbeziehen (Fallback)
        if not relevant_agents:
            print("[Personal Assistant] Keine spezifischen Agenten identifiziert, verwende alle")
            relevant_agents = [self.travel_agent, self.weather_advisor, self.budget_planner]
        
        # Aufgaben erstellen und an relevante Agenten delegieren
        responses = {}
        
        for agent in relevant_agents:
            agent_name = agent.agent_card["name"]
            print(f"[Personal Assistant] Delegiere an {agent_name}")
            
            # Erstelle eine Aufgabe für den Agenten (A2A-Task)
            task_id = f"task_{len(self.tasks) + 1}"
            task = {
                "id": task_id,
                "message": user_message,
                "status": "pending"
            }
            self.tasks[task_id] = task
            
            # Delegiere die Aufgabe an den Agenten
            response = agent.process_task(task)
            responses[agent_name] = response
            
            # Aktualisiere den Aufgabenstatus
            task["status"] = response["status"]
            if "result" in response:
                task["result"] = response["result"]
        
        # Integriere die Ergebnisse zu einer umfassenden Antwort
        return self._integrate_results(user_message, responses)
    
    def _integrate_results(self, user_message, responses):
        """Integriert die Ergebnisse der verschiedenen Spezialisten-Agenten."""
        print(f"[Personal Assistant] Integriere Ergebnisse von {len(responses)} Agenten")
        
        # Prüfe, ob weitere Eingabe erforderlich ist
        requires_input = any(r["status"] == "input-required" for r in responses.values())
        if requires_input:
            # Sammle alle Fragen der Agenten
            questions = [r["message"] for r in responses.values() if r["status"] == "input-required"]
            return {
                "status": "input-required",
                "message": "Ich benötige mehr Informationen: " + " ".join(questions)
            }
        
        # Integriere die Ergebnisse zu einer kohärenten Antwort
        # Hier stark vereinfacht - in einer echten Anwendung würde LLM verwendet
        
        # Sammle alle Ergebnisse
        integrated_result = {}
        
        # Sammle Reiseinformationen vom Travel Agent
        if "Travel Agent" in responses and responses["Travel Agent"]["status"] == "completed":
            travel_result = responses["Travel Agent"]["result"]
            integrated_result.update({
                "travel_info": travel_result
            })
        
        # Sammle Wetterinformationen vom Weather Advisor
        if "Weather Advisor" in responses and responses["Weather Advisor"]["status"] == "completed":
            weather_result = responses["Weather Advisor"]["result"]
            integrated_result.update({
                "weather_info": weather_result
            })
        
        # Sammle Budgetinformationen vom Budget Planner
        if "Budget Planner" in responses and responses["Budget Planner"]["status"] == "completed":
            budget_result = responses["Budget Planner"]["result"]
            integrated_result.update({
                "budget_info": budget_result
            })
        
        # Erstelle einen Zusammenfassungstext
        summary = "Hier ist meine Zusammenfassung basierend auf den Informationen unserer Experten:\n\n"
        
        if "travel_info" in integrated_result:
            travel_info = integrated_result["travel_info"]
            if "flight" in travel_info and "hotel" in travel_info:
                flight = travel_info["flight"]
                hotel = travel_info["hotel"]
                summary += f"Reise: Flug mit {flight['airline']} für ${flight['price']} und Aufenthalt im {hotel['name']} für ${hotel['total_price']}.\n"
            elif "flights" in travel_info:
                flights = travel_info["flights"]
                summary += f"Flugoptionen: {len(flights)} verfügbare Flüge, beginnend bei ${min([f['price'] for f in flights])}.\n"
            elif "hotels" in travel_info:
                hotels = travel_info["hotels"]
                summary += f"Hoteloptionen: {len(hotels)} verfügbare Hotels, beginnend bei ${min([h['price_per_night'] for h in hotels])} pro Nacht.\n"
        
        if "weather_info" in integrated_result:
            weather_info = integrated_result["weather_info"]
            if "data" in weather_info:
                data = weather_info["data"]
                summary += f"Wetter in {weather_info.get('location', 'dem Reiseziel')}: {data['temp']}°C, {data['condition']} mit etwa {data['rain_days']} Regentagen pro Monat.\n"
            elif "best_month_name" in weather_info:
                summary += f"Beste Reisezeit: {weather_info['best_month_name']} - {weather_info['reason']}.\n"
        
        if "budget_info" in integrated_result:
            budget_info = integrated_result["budget_info"]
            if "activities_budget" in budget_info:
                summary += f"Budget: ${budget_info['total_budget']} Gesamtbudget, davon ${budget_info['activities_budget']} für Aktivitäten (${budget_info.get('daily_budget', 0):.2f} pro Tag).\n"
            elif "optimization_tips" in budget_info:
                tips = budget_info["optimization_tips"]
                summary += f"Budgettipps: {tips[0]} und {tips[1]}.\n"
        
        # Rückgabe der integrierten Ergebnisse
        return {
            "status": "completed", 
            "message": summary,
            "detailed_results": integrated_result
        }


# -------------------- HAUPTFUNKTION ZUM TESTEN --------------------

def main():
    """Hauptfunktion zum Testen des Reiseplanungssystems."""
    
    print("=== A2A & MCP Reiseplanungssystem ===")
    print("Dieses System veranschaulicht die Konzepte von MCP und A2A.")
    print("- MCP: Verbindung zwischen Agenten und Tools (strukturiert)")
    print("- A2A: Verbindung zwischen Agenten (natürliche Sprache)")
    print("\nBeispielanfragen:")
    print("1. Plane eine Reise nach Hawaii im Juni mit einem Budget von 3000 Dollar")
    print("2. Wie ist das Wetter in Paris im Juli?")
    print("3. Was ist die beste Reisezeit für Tokyo?")
    print("4. Berechne mein Budget für eine Reise nach Hawaii")
    
    # Initialisiere den persönlichen Assistenten
    assistant = PersonalAssistant()
    
    while True:
        print("\n" + "="*50)
        user_input = input("\nDeine Anfrage (oder 'exit' zum Beenden): ")
        
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("Auf Wiedersehen!")
            break
        
        # Verarbeite die Anfrage und erhalte die integrierte Antwort
        response = assistant.process_request(user_input)
        
        # Zeige die Antwort an
        if response["status"] == "input-required":
            print(f"\n[Assistent benötigt weitere Informationen] {response['message']}")
        else:
            print(f"\n[Zusammenfassung] {response['message']}")
            
            # Optional: Detaillierte Ergebnisse anzeigen
            show_details = input("\nMöchtest du die detaillierten Ergebnisse sehen? (j/n): ")
            if show_details.lower() in ['j', 'ja', 'y', 'yes']:
                import json
                print("\n[Detaillierte Ergebnisse]")
                print(json.dumps(response["detailed_results"], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()