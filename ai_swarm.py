"""
================================================================================
Dieses Skript demonstriert die Verwendung einer Chat-Applikation basierend auf dem
'Swarm'-Konzept und mehreren GPT-4-Agenten. Über ein GUI, das mit CustomTkinter 
(ctk) erstellt wurde, kann der Nutzer Nachrichten eingeben und erhält daraufhin 
Antworten von unterschiedlichen 'Agenten'. Diese Agenten sind spezialisiert auf 
bestimmte Themenbereiche (Python, Windows, PowerShell) und werden durch einen 
'Service-Agenten' (Agent Dirk) ausgelesen und angesprochen.

Das Ziel ist eine flexible und erweiterbare Struktur, bei der eingehende 
Benutzeranfragen durch 'Agent Dirk' gefiltert und an den jeweils passenden 
Agenten weitergeleitet werden können. 

Wichtige Elemente in diesem Skript:
- Verwendung der .env-Datei (Umgebungsvariablen) für den OpenAI API-Schlüssel
- Mehrere Agenten-Objekte, die unterschiedliche Rollen / Anweisungen haben
- Ein GUI zur Interaktion mit dem Chat-System
- Funktionen zur Verwaltung des API-Schlüssels und zum Wechseln des GUI-Themes

Zudem sind in diesem Code zahlreiche Kommentare enthalten, um Schritt für Schritt 
aufzuzeigen, was hier passiert, wie es passiert und warum es so gelöst wurde.
================================================================================
"""

import customtkinter as ctk
from tkinter import scrolledtext, Menu
from swarm import Swarm, Agent
import os
from dotenv import load_dotenv, set_key
import openai

# API-Schlüssel setzen
load_dotenv()  # Lade Umgebungsvariablen aus einer .env-Datei
openai.api_key = os.getenv("OPENAI_API_KEY")

# Swarm-Client initialisieren
client = Swarm()

def transfer_to_agent_mona():
    """
    Diese Funktion gibt das Objekt `agent_mona` zurück, um eine 
    Anfrage an Agent Mona (Python-Experte) weiterzureichen.
    
    Warum:
    - Wir möchten gezielt Anfragen, die sich um Python-Code drehen, 
      an einen passenden Agenten weiterleiten.
    """
    return agent_mona

def transfer_to_agent_peter():
    """
    Diese Funktion gibt das Objekt `agent_peter` zurück, um eine 
    Anfrage an Agent Peter (Windows-Experte) weiterzureichen.
    
    Warum:
    - Wenn sich eine Anfrage auf Windows-Fragen bezieht, 
      wird sie an diesen speziellen Agenten delegiert.
    """
    return agent_peter

def transfer_to_agent_ralf():
    """
    Diese Funktion gibt das Objekt `agent_ralf` zurück, um eine 
    Anfrage an Agent Ralf (PowerShell-Experte) weiterzureichen.
    
    Warum:
    - Sobald wir eine PowerShell-bezogene Frage identifizieren, 
      leiten wir sie an diesen Agenten weiter.
    """
    return agent_ralf

# -----------------------------------------------------------------------------
# Definition der Agenten:
# -----------------------------------------------------------------------------
# Hier werden Instanzen der Klasse Agent erzeugt. Jeder Agent hat eigene
# Anweisungen (instructions), einen Namen und nutzt das GPT-4-Modell über
# den Swarm-Client, um Antworten zu generieren.
# -----------------------------------------------------------------------------

agent_dirk = Agent(
    name="Agent Dirk",
    instructions=(
        "Du bist ein freundlicher Service-Agent, der Anfragen filtert und an "
        "andere Agenten weitergibt. Wir haben drei Agenten: "
        "1. Mona: Sie ist auf Python-Code spezialisiert. "
        "2. Peter: Er ist auf Windows-Probleme spezialisiert. "
        "3. Ralf: Er ist auf PowerShell-Prompts spezialisiert. "
        "Leite die Anfragen an den entsprechenden Agenten weiter."
    ),
    functions=[transfer_to_agent_mona, transfer_to_agent_peter, transfer_to_agent_ralf],
    model="gpt-4"  # Stelle sicher, dass das GPT-4-Modell verwendet wird
)

agent_mona = Agent(
    name="Agent Mona",
    instructions="Du analysierst und erstellst professionellen Python-Code.",
    model="gpt-4"  # Stelle sicher, dass das GPT-4-Modell verwendet wird
)

agent_peter = Agent(
    name="Agent Peter",
    instructions="Du hilfst bei Windows-Problemen und gibst detaillierte Anweisungen zur Lösung.",
    model="gpt-4"  # Stelle sicher, dass das GPT-4-Modell verwendet wird
)

agent_ralf = Agent(
    name="Agent Ralf",
    instructions="Du hilfst bei PowerShell-Prompts und gibst detaillierte Anweisungen zur Lösung.",
    model="gpt-4"  # Stelle sicher, dass das GPT-4-Modell verwendet wird
)

# -----------------------------------------------------------------------------
# GUI-Funktionalität:
# -----------------------------------------------------------------------------
# Nachfolgend werden die Funktionen definiert, die das GUI-Verhalten steuern.
# -----------------------------------------------------------------------------

def send_message():
    """
    Diese Funktion wird aufgerufen, wenn der Benutzer auf den 'Send'-Button klickt.
    Sie liest den Text aus dem Eingabefeld `input_field` aus, fügt ihn zur 
    Nachrichtenhistorie `messages` hinzu und ruft die Swarm-API auf, um eine 
    Antwort zu erhalten. Anschließend wird die Antwort im Chat-Fenster angezeigt.
    
    Ablauf (Was geschieht hier):
    1. Lesen des Nutzereingangs (user_input).
    2. Hinzufügen der Nutzereingabe zur gemeinsamen Nachrichtenhistorie.
    3. Ausführen der `client.run(...)` Methode, um eine Antwort vom aktiven Agenten 
       zu bekommen.
    4. Aktualisieren des angezeigten Chatverlaufs (chat_history).
    5. Leeren des Eingabefelds.
    
    Warum:
    - Wir möchten eine Interaktion zwischen Nutzer und Agent ermöglichen, bei der 
      der Agent mithilfe der Nachrichtenhistorie sinnvolle Antworten generiert.
    
    Wie:
    - Die `Swarm`-Klasse verwaltet die Kommunikation mit dem GPT-4-Modell und 
      nutzt die Anweisungen des jeweiligen Agenten.
    """
    global current_agent
    user_input = input_field.get().strip()
    if not user_input:
        return  # Verhindert, dass leere Eingaben verarbeitet werden

    # Füge die Anfrage zur Nachrichtenliste hinzu
    messages.append({"role": "user", "content": user_input})

    try:
        # Rufe den Swarm-Client auf, um eine Antwort zu generieren
        response = client.run(
            agent=current_agent,
            messages=messages
        )
        agent_response = response.messages[-1]["content"]
        current_agent = response.agent

        # Aktualisiere den Chatverlauf
        chat_history.config(state=ctk.NORMAL)
        chat_history.insert(ctk.END, f"You: {user_input}\n")
        chat_history.insert(ctk.END, f"{current_agent.name}: {agent_response}\n\n")
        chat_history.config(state=ctk.DISABLED)
        chat_history.see(ctk.END)

        # Leere das Eingabefeld
        input_field.delete(0, ctk.END)
    except Exception as e:
        # Falls ein Fehler auftritt, wird er im Chat-Verlauf angezeigt
        chat_history.config(state=ctk.NORMAL)
        chat_history.insert(ctk.END, f"Error: {e}\n\n")
        chat_history.config(state=ctk.DISABLED)

def set_api_key():
    """
    Diese Funktion liest den in das `api_key_entry` Eingabefeld geschriebenen 
    String aus und aktualisiert damit die .env-Datei und die OpenAI-API-Schlüsselvariable.

    Was:
    - Es wird ein neuer API-Key aus dem Eingabefeld gelesen und geprüft, ob er
      nicht leer ist. 
    - Anschließend wird er mittels `set_key` in der .env-Datei abgelegt.
    - Der globale `openai.api_key` wird ebenfalls aktualisiert.

    Warum:
    - Somit kann der Nutzer ohne Programmieraufwand den API-Schlüssel zur Laufzeit
      ändern, ohne das Skript beenden zu müssen.
    """
    new_key = api_key_entry.get().strip()
    if new_key:
        set_key(".env", "OPENAI_API_KEY", new_key)
        openai.api_key = new_key
        api_key_entry.delete(0, ctk.END)
        print("API-Schlüssel erfolgreich gespeichert.")

def change_theme(theme):
    """
    Wechselt zwischen den Erscheinungsmodi 'light' und 'dark' für das GUI.
    
    Was:
    - Aufruf der `ctk.set_appearance_mode(theme)`-Funktion.

    Warum:
    - Ermöglicht dem Nutzer, das Erscheinungsbild des Fensters zu ändern.

    Wie:
    - Wird über das Menü 'Themen' in der GUI aufgerufen, 
      je nachdem, welchen Menüpunkt der Nutzer anklickt.
    """
    ctk.set_appearance_mode(theme)

# -----------------------------------------------------------------------------
# Initialisierung der Nachrichtenhistorie und Auswahl des Start-Agenten:
# -----------------------------------------------------------------------------
# Wir beginnen hier mit einer vordefinierten Nachricht in der `messages`-Liste, 
# um dem Nutzer erste Informationen zu liefern. Der Start-Agent wird auf 
# 'agent_dirk' gesetzt, da dieser unser Service-Agent ist.
# -----------------------------------------------------------------------------

messages = [{"role": "user", "content": "Welche Agenten stehen zur Verfügung? Und wobei helfen sie?"}]
current_agent = agent_dirk

# -----------------------------------------------------------------------------
# Erstellung des Hauptfensters mittels CustomTkinter:
# -----------------------------------------------------------------------------

root = ctk.CTk()
root.title("Swarm Chat")

# -----------------------------------------------------------------------------
# Menüerstellung:
# -----------------------------------------------------------------------------
# Hier wird ein Menü zur Auswahl des Themas (Hell/Dunkel) angelegt.
# -----------------------------------------------------------------------------
menu = Menu(root)
root.config(menu=menu)

theme_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Themen", menu=theme_menu)
theme_menu.add_command(label="Hell", command=lambda: change_theme("light"))
theme_menu.add_command(label="Dunkel", command=lambda: change_theme("dark"))

# -----------------------------------------------------------------------------
# Chatverlauf (ScrolledText):
# -----------------------------------------------------------------------------
# Dieses Widget zeigt vergangene Nachrichten an und erlaubt das Scrollen.
# -----------------------------------------------------------------------------
chat_history = scrolledtext.ScrolledText(root, wrap=ctk.WORD, state=ctk.DISABLED)
chat_history.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# -----------------------------------------------------------------------------
# Eingabefeld (CTkEntry) für Nutzernachrichten:
# -----------------------------------------------------------------------------
input_field = ctk.CTkEntry(root)
input_field.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# -----------------------------------------------------------------------------
# Send-Button:
# -----------------------------------------------------------------------------
# Beim Klicken wird die Funktion `send_message()` aufgerufen.
# -----------------------------------------------------------------------------
send_button = ctk.CTkButton(root, text="Send", command=send_message)
send_button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

# -----------------------------------------------------------------------------
# API-Schlüssel-Felder:
# -----------------------------------------------------------------------------
# Ein Label, ein Eingabefeld und ein Button zum Setzen des neuen API-Schlüssels.
# -----------------------------------------------------------------------------
api_key_label = ctk.CTkLabel(root, text="OpenAI API-Schlüssel:")
api_key_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

api_key_entry = ctk.CTkEntry(root)
api_key_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

api_key_button = ctk.CTkButton(root, text="Speichern", command=set_api_key)
api_key_button.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

# -----------------------------------------------------------------------------
# Grid-Konfiguration zur dynamischen Größenanpassung:
# -----------------------------------------------------------------------------
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)

# -----------------------------------------------------------------------------
# Starten der Haupt-Loop:
# -----------------------------------------------------------------------------
# Dies hält das Fenster offen, bis der Nutzer das Programm schließt.
# -----------------------------------------------------------------------------
root.mainloop()
