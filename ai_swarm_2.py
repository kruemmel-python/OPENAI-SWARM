"""
================================================================================
Dieses Skript stellt eine umfangreiche Chat-Applikation dar, bei der verschiedene
Agenten (alle auf das GPT-4-Modell zurückgreifend) je nach thematischem Schwerpunkt 
unterschiedliche gesetzliche Fachgebiete beantworten. 

Der "Agent Dirk" fungiert hierbei als Verteiler-Agent (auch Service-Agent genannt),
der Anfragen je nach enthaltener Schlüsselwörter an die entsprechenden Agenten 
weiterleitet. So gibt es z.B. Agenten für das BGB, HGB, StGB, Steuerrecht usw.

Das GUI wird mittels CustomTkinter (ctk) erstellt und enthält:
 - Eine Reitersteuerung (Tabs) für jede Agenteninstanz
 - Ein Eingabefeld für Chatnachrichten
 - Buttons zum Senden einer Nachricht und zum Setzen eines neuen API-Schlüssels
 - Ein Menü zum Wechseln des Farbschemas (Hell/Dunkel) sowie zum Ändern der 
   Schriftgröße
 - Multithreading für das asynchrone Abrufen der Antworten vom GPT-4-Modell

Wichtig:
 - Der API-Schlüssel wird aus einer .env-Datei gelesen und lässt sich zur Laufzeit 
   ändern.
 - Der Chatverlauf wird pro Agent in dessen Tab separat angezeigt, sodass die 
   Unterhaltungen voneinander getrennt bleiben.
 - Das Skript zeigt exemplarisch, wie mehrere spezialisierte Agents parallel 
   verwaltet und angesprochen werden können.

Das gesamte Skript ist in deutscher Sprache dokumentiert und richtet sich an 
Einsteiger und Fortgeschrittene, die ein Verständnis für die Verwendung von 
Agentensystemen in Python (Version 3.12) sowie GUI-Programmierung mit 
CustomTkinter erlangen möchten.
================================================================================
"""

import customtkinter as ctk
from tkinter import scrolledtext, Menu, ttk, font
from swarm import Swarm, Agent
import os
from dotenv import load_dotenv, set_key
import openai
import threading

# API-Schlüssel laden und OpenAI-Client initialisieren
load_dotenv()  # Lädt Schlüssel aus der .env-Datei
openai.api_key = os.getenv("OPENAI_API_KEY")

# Der Swarm-Client kümmert sich um die Kommunikation mit den GPT-4-Agenten
client = Swarm()

# -----------------------------------------------------------------------------
# Definition der Agenten-Funktionen zur Weiterleitung:
# -----------------------------------------------------------------------------
def transfer_to_agent_bgb():
    """
    Liefert das Agent-Objekt für das Bürgerliche Gesetzbuch (BGB) zurück.
    Dies wird von 'Agent Dirk' genutzt, um gezielte Anfragen an den
    zuständigen Agenten weiterzugeben.
    """
    return agent_bgb

def transfer_to_agent_hgb():
    """
    Liefert das Agent-Objekt für das Handelsgesetzbuch (HGB) zurück.
    """
    return agent_hgb

def transfer_to_agent_stgb():
    """
    Liefert das Agent-Objekt für das Strafgesetzbuch (StGB) zurück.
    """
    return agent_stgb

def transfer_to_agent_arbgb():
    """
    Liefert das Agent-Objekt für das Arbeitsgesetzbuch (ArbGB) zurück.
    (Hier exemplarisch mit 'Agent Arbeitsrecht' bezeichnet.)
    """
    return agent_arbgb

def transfer_to_agent_sgb():
    """
    Liefert das Agent-Objekt für das Sozialgesetzbuch (SGB) zurück.
    """
    return agent_sgb

def transfer_to_agent_steuerrecht():
    """
    Liefert das Agent-Objekt für das Steuerrecht zurück.
    """
    return agent_steuerrecht

def transfer_to_agent_vwvfgg():
    """
    Liefert das Agent-Objekt für das Verwaltungsverfahrensgesetz (VwVfG) zurück.
    """
    return agent_vwvfgg

def transfer_to_agent_vwgo():
    """
    Liefert das Agent-Objekt für die Verwaltungsgerichtsordnung (VwGO) zurück.
    """
    return agent_vwgo

def transfer_to_agent_uwg():
    """
    Liefert das Agent-Objekt für das Gesetz gegen den unlauteren Wettbewerb (UWG) zurück.
    """
    return agent_uwg

def transfer_to_agent_urhg():
    """
    Liefert das Agent-Objekt für das Urheberrechtsgesetz (UrhG) zurück.
    """
    return agent_urhg

def transfer_to_agent_patg():
    """
    Liefert das Agent-Objekt für das Patentrecht (PatG) zurück.
    """
    return agent_patg

def transfer_to_agent_markeng():
    """
    Liefert das Agent-Objekt für das Markengesetz (MarkenG) zurück.
    """
    return agent_markeng

def transfer_to_agent_owig():
    """
    Liefert das Agent-Objekt für das Gesetz über Ordnungswidrigkeiten (OWiG) zurück.
    """
    return agent_owig

def transfer_to_agent_baubgb():
    """
    Liefert das Agent-Objekt für das Baugesetzbuch (BauGB) zurück.
    """
    return agent_baubgb

# -----------------------------------------------------------------------------
# Definition der Agenten:
# -----------------------------------------------------------------------------
# Jeder Agent erhält einen Namen, spezifische Instruktionen sowie das zu 
# verwendende Modell (GPT-4).
# -----------------------------------------------------------------------------
agent_dirk = Agent(
    name="Agent Dirk",
    instructions=(
        "Du bist ein freundlicher Service-Agent, der Anfragen filtert und an "
        "andere Agenten weitergibt. Wir haben mehrere Agenten: "
        "1. BGB: Er ist auf das Bürgerliche Gesetzbuch spezialisiert. "
        "2. HGB: Er ist auf das Handelsgesetzbuch spezialisiert. "
        "3. StGB: Er ist auf das Strafgesetzbuch spezialisiert. "
        "4. Arbeitsrecht: Er ist auf das Arbeitsgesetzbuch spezialisiert. "
        "5. Sozialrecht: Er ist auf das Sozialgesetzbuch spezialisiert. "
        "6. Steuerrecht: Er ist auf das Steuerrecht spezialisiert. "
        "7. Verwaltungsverfahrensgesetz: Er ist auf das Verwaltungsverfahrensgesetz spezialisiert. "
        "8. Verwaltungsgerichtsordnung: Er ist auf die Verwaltungsgerichtsordnung spezialisiert. "
        "9. Gesetz gegen den unlauteren Wettbewerb: Er ist auf das Gesetz gegen den unlauteren Wettbewerb spezialisiert. "
        "10. Urheberrechtsgesetz: Er ist auf das Urheberrechtsgesetz spezialisiert. "
        "11. Patentrecht: Er ist auf das Patentrecht spezialisiert. "
        "12. Markengesetz: Er ist auf das Markengesetz spezialisiert. "
        "13. Gesetz über Ordnungswidrigkeiten: Er ist auf das Gesetz über Ordnungswidrigkeiten spezialisiert. "
        "14. Baurecht: Er ist auf das Baurecht spezialisiert. "
        "Leite die Anfragen an den entsprechenden Agenten weiter. "
        "Wenn die Anfrage das Wort 'BGB' enthält, leite sie an Agent BGB weiter. "
        "Wenn die Anfrage das Wort 'HGB' enthält, leite sie an Agent HGB weiter. "
        "Wenn die Anfrage das Wort 'StGB' enthält, leite sie an Agent StGB weiter. "
        "Wenn die Anfrage das Wort 'Arbeitsrecht' enthält, leite sie an Agent Arbeitsrecht weiter. "
        "Wenn die Anfrage das Wort 'Sozialrecht' enthält, leite sie an Agent Sozialrecht weiter. "
        "Wenn die Anfrage das Wort 'Steuerrecht' enthält, leite sie an Agent Steuerrecht weiter. "
        "Wenn die Anfrage das Wort 'Verwaltungsverfahrensgesetz' enthält, leite sie an Agent Verwaltungsverfahrensgesetz weiter. "
        "Wenn die Anfrage das Wort 'Verwaltungsgerichtsordnung' enthält, leite sie an Agent Verwaltungsgerichtsordnung weiter. "
        "Wenn die Anfrage das Wort 'Gesetz gegen den unlauteren Wettbewerb' enthält, leite sie an Agent Gesetz gegen den unlauteren Wettbewerb weiter. "
        "Wenn die Anfrage das Wort 'Urheberrechtsgesetz' enthält, leite sie an Agent Urheberrechtsgesetz weiter. "
        "Wenn die Anfrage das Wort 'Patentrecht' enthält, leite sie an Agent Patentrecht weiter. "
        "Wenn die Anfrage das Wort 'Markengesetz' enthält, leite sie an Agent Markengesetz weiter. "
        "Wenn die Anfrage das Wort 'Gesetz über Ordnungswidrigkeiten' enthält, leite sie an Agent Gesetz über Ordnungswidrigkeiten weiter. "
        "Wenn die Anfrage das Wort 'Baurecht' enthält, leite sie an Agent Baurecht weiter. "
    ),
    functions=[
        transfer_to_agent_bgb, transfer_to_agent_hgb, transfer_to_agent_stgb,
        transfer_to_agent_arbgb, transfer_to_agent_sgb, transfer_to_agent_steuerrecht,
        transfer_to_agent_vwvfgg, transfer_to_agent_vwgo, transfer_to_agent_uwg,
        transfer_to_agent_urhg, transfer_to_agent_patg, transfer_to_agent_markeng,
        transfer_to_agent_owig, transfer_to_agent_baubgb
    ],
    model="gpt-4"
)

agent_bgb = Agent(
    name="Agent BGB",
    instructions="Du bist spezialisiert auf das Bürgerliche Gesetzbuch (BGB) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

agent_hgb = Agent(
    name="Agent HGB",
    instructions="Du bist spezialisiert auf das Handelsgesetzbuch (HGB) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

agent_stgb = Agent(
    name="Agent StGB",
    instructions="Du bist spezialisiert auf das Strafgesetzbuch (StGB) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

agent_arbgb = Agent(
    name="Agent Arbeitsrecht",
    instructions="Du bist spezialisiert auf das Arbeitsgesetzbuch (ArbGB) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

agent_sgb = Agent(
    name="Agent Sozialrecht",
    instructions="Du bist spezialisiert auf das Sozialgesetzbuch (SGB) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

agent_steuerrecht = Agent(
    name="Agent Steuerrecht",
    instructions="Du bist spezialisiert auf das Steuerrecht (AO, EStG, UStG, etc.) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

agent_vwvfgg = Agent(
    name="Agent Verwaltungsverfahrensgesetz",
    instructions="Du bist spezialisiert auf das Verwaltungsverfahrensgesetz (VwVfG) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

agent_vwgo = Agent(
    name="Agent Verwaltungsgerichtsordnung",
    instructions="Du bist spezialisiert auf die Verwaltungsgerichtsordnung (VwGO) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

agent_uwg = Agent(
    name="Agent Gesetz gegen den unlauteren Wettbewerb",
    instructions="Du bist spezialisiert auf das Gesetz gegen den unlauteren Wettbewerb (UWG) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

agent_urhg = Agent(
    name="Agent Urheberrechtsgesetz",
    instructions="Du bist spezialisiert auf das Urheberrechtsgesetz (UrhG) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

agent_patg = Agent(
    name="Agent Patentrecht",
    instructions="Du bist spezialisiert auf das Patentrecht (PatG) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

agent_markeng = Agent(
    name="Agent Markengesetz",
    instructions="Du bist spezialisiert auf das Markengesetz (MarkenG) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

agent_owig = Agent(
    name="Agent Gesetz über Ordnungswidrigkeiten",
    instructions="Du bist spezialisiert auf das Gesetz über Ordnungswidrigkeiten (OWiG) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

agent_baubgb = Agent(
    name="Agent Baurecht",
    instructions="Du bist spezialisiert auf das Baugesetzbuch (BauGB) und gibst detaillierte Informationen und Ratschläge zu diesem Bereich.",
    model="gpt-4"
)

# -----------------------------------------------------------------------------
# GUI-Funktionalität:
# -----------------------------------------------------------------------------
def send_message():
    """
    Reagiert auf den Klick des 'Send'-Buttons. 
    1) Liest die Nutzereingabe aus dem Eingabefeld `input_field`. 
    2) Identifiziert den aktiven Tab (sprich den aktuell ausgewählten Agenten). 
    3) Führt die Anfrage an das GPT-4-Modell in einem separaten Thread aus.

    Warum Threading?
    - Um die GUI reaktionsfähig zu halten, wird der aufwändige Netzwerkaufruf 
      nicht im Hauptthread ausgeführt, sondern parallel in einem Worker-Thread.
    """
    global current_agent
    user_input = input_field.get().strip()
    if not user_input:
        return  # Vermeidet leere Eingaben

    # Ermittelt den aktuell gewählten Tab im Notebook (Reiter-Steuerung).
    current_tab = chat_tabs.select()
    current_agent_name = chat_tabs.tab(current_tab, "text")

    # Ordnet den eingestellten Agenten (z.B. "Agent BGB") dem globalen current_agent zu.
    for agent in agents:
        if agent.name == current_agent_name:
            current_agent = agent
            break

    # Speichert die Nachricht in der gemeinsamen Nachrichtenhistorie.
    messages.append({"role": "user", "content": user_input})

    # Startet die Netzwerk-/API-Anfrage in einem separaten Thread.
    threading.Thread(target=process_message, args=(user_input, current_agent)).start()

    # Leert das Eingabefeld
    input_field.delete(0, ctk.END)

def process_message(user_input, agent):
    """
    Führt den eigentlichen Request an das GPT-4-Modell aus, 
    wird in einem separaten Thread gestartet. 

    Vorgehensweise:
    1) client.run(...) ruft den Swarm-Client auf und leitet die Anfrage an den 
       jeweiligen Agenten weiter.
    2) Die letzte Antwort wird extrahiert und im UI sichtbar gemacht.
    3) Im Falle eines Fehlers wird dieser angezeigt.
    """
    global current_agent
    try:
        # Anfrage an GPT-4 via Swarm-Client
        response = client.run(
            agent=agent,
            messages=messages
        )
        agent_response = response.messages[-1]["content"]
        current_agent = response.agent

        # Aktualisiert die GUI im Hauptthread mithilfe von root.after(...)
        root.after(0, update_chat_history, user_input, agent_response, current_agent.name)
    except Exception as e:
        # Falls ein Fehler auftritt, ab in den Chatverlauf
        root.after(0, update_chat_history, user_input, f"Error: {e}", current_agent.name)

def update_chat_history(user_input, agent_response, agent_name):
    """
    Diese Funktion aktualisiert den Chatverlauf eines bestimmten Agenten-Tabs 
    im Hauptthread. 
    - user_input: Die Nutzereingabe
    - agent_response: Die Antwort vom Modell
    - agent_name: Name des gerade aktiven Agenten
    """
    # Identifiziere den Frame, der zu diesem Agenten gehört
    frame = agent_frame_map[agent_name]
    chat_history = frame.chat_history
    chat_history.config(state=ctk.NORMAL)
    chat_history.insert(ctk.END, f"You: {user_input}\n")
    chat_history.insert(ctk.END, f"{agent_name}: {agent_response}\n\n")
    chat_history.config(state=ctk.DISABLED)
    chat_history.see(ctk.END)

    # Wechselt in den entsprechenden Tab, um die neue Nachricht sichtbar zu machen
    chat_tabs.select(chat_tabs.index(frame))

def set_api_key():
    """
    Erlaubt das Setzen eines neuen OpenAI API-Schlüssels zur Laufzeit. 
    1) Liest den Key aus dem Eingabefeld `api_key_entry`.
    2) Speichert ihn per set_key(...) in der .env-Datei.
    3) Aktualisiert openai.api_key, sodass die neuen Anfragen mit dem 
       aktualisierten Schlüssel durchgeführt werden.
    """
    new_key = api_key_entry.get().strip()
    if new_key:
        set_key(".env", "OPENAI_API_KEY", new_key)
        openai.api_key = new_key
        api_key_entry.delete(0, ctk.END)
        print("API-Schlüssel erfolgreich gespeichert.")

def change_theme(theme):
    """
    Ermöglicht das Umschalten zwischen 'light' und 'dark' Themen im GUI. 
    Wird über das Menü "Themen" aufgerufen.
    """
    ctk.set_appearance_mode(theme)

def change_font_size(size):
    """
    Ändert die Schriftgröße in allen Chatverläufen. 
    Hierzu wird das 'font' Paket verwendet, um die aktuell eingestellte Schrift 
    auszulesen und zu modifizieren.
    """
    for agent in agents:
        frame = agent_frame_map[agent.name]
        chat_history = frame.chat_history
        current_font = font.Font(font=chat_history['font'])
        chat_history.config(font=(current_font.actual('family'), size))

# -----------------------------------------------------------------------------
# Initialisierung der Nachrichtenhistorie und Auswahl des Start-Agenten:
# -----------------------------------------------------------------------------
messages = [{"role": "user", "content": "Welche Agenten stehen zur Verfügung? Und wobei helfen sie?"}]
current_agent = agent_dirk  # Der globale "current_agent" startet mit Agent Dirk

# -----------------------------------------------------------------------------
# Erstellung des Hauptfensters mittels CustomTkinter:
# -----------------------------------------------------------------------------
root = ctk.CTk()
root.title("Swarm Chat")

# -----------------------------------------------------------------------------
# Menüerstellung:
# -----------------------------------------------------------------------------
menu = Menu(root)
root.config(menu=menu)

theme_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Themen", menu=theme_menu)
theme_menu.add_command(label="Hell", command=lambda: change_theme("light"))
theme_menu.add_command(label="Dunkel", command=lambda: change_theme("dark"))

font_size_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Schriftgröße", menu=font_size_menu)
font_size_menu.add_command(label="Klein", command=lambda: change_font_size(10))
font_size_menu.add_command(label="Mittel", command=lambda: change_font_size(12))
font_size_menu.add_command(label="Groß", command=lambda: change_font_size(14))

# -----------------------------------------------------------------------------
# Chatverlauf (Tabbed Notebook für jeden Agenten):
# -----------------------------------------------------------------------------
chat_tabs = ttk.Notebook(root)
chat_tabs.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

agents = [
    agent_dirk, agent_bgb, agent_hgb, agent_stgb, agent_arbgb, agent_sgb, agent_steuerrecht,
    agent_vwvfgg, agent_vwgo, agent_uwg, agent_urhg, agent_patg, agent_markeng,
    agent_owig, agent_baubgb
]

# Ein Dictionary, um jedem Agenten seinen Frame zuzuordnen
agent_frame_map = {}

for agent in agents:
    # Erstelle für jeden Agenten einen eigenen Frame
    frame = ctk.CTkFrame(chat_tabs)
    # Ein ScrolledText-Widget für den Chatverlauf
    chat_history = scrolledtext.ScrolledText(frame, wrap=ctk.WORD, state=ctk.DISABLED)
    chat_history.pack(expand=True, fill="both")
    frame.chat_history = chat_history

    # Füge den Frame als neuen Tab hinzu
    chat_tabs.add(frame, text=agent.name)

    # Speichere die Zuordnung in unserem Dictionary
    agent_frame_map[agent.name] = frame

# Setze den Verteiler-Agenten (Agent Dirk) als Standard-Tab
chat_tabs.select(0)

# -----------------------------------------------------------------------------
# Eingabefeld für Nutzernachrichten:
# -----------------------------------------------------------------------------
input_field = ctk.CTkEntry(root)
input_field.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# -----------------------------------------------------------------------------
# Send-Button:
# -----------------------------------------------------------------------------
send_button = ctk.CTkButton(root, text="Send", command=send_message)
send_button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

# -----------------------------------------------------------------------------
# API-Schlüssel-Felder:
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
root.mainloop()
