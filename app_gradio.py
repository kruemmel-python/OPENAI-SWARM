"""
================================================================================
AUSFÜHRLICHE DOKUMENTATION UND KOMMENTARE (IN DEUTSCH)

Ziel dieses Skripts:
--------------------
Dieses Skript realisiert einen Chat mit dem GPT-4-Modell über das sogenannte
"Swarm"-Framework. Dabei gibt es mehrere spezialisierte Agenten, die jeweils
einen bestimmten Rechtsbereich (z. B. BGB, StGB, Steuerrecht usw.) abdecken.
"Agent Dirk" dient als zentraler Verteiler, der die Anfrage erkennt und an den
passenden Fach-Agenten weiterleitet.

Gleichzeitig wird die Oberfläche nicht mehr mittels "CustomTkinter" erstellt,
sondern per "Gradio". Dabei wird in einem einzigen Chatfenster mit dem Namen
"chatbot" die Konversation abgebildet. Jede Eingabe des Nutzers und die
darauf folgende Antwort des jeweils aktiven Agenten werden in einem
Chat-Verlauf gelistet.

Wichtige Bausteine:
1) Laden des OpenAI-API-Schlüssels aus einer ".env"-Datei
2) Definition mehrerer Agenten
3) Ein "Verteiler-Agent" namens "Agent Dirk"
4) Eine Chat-Funktion `send_message`, die den Chatverlauf in Gradio steuert
5) Eine Funktion `set_api_key`, mit der zur Laufzeit der verwendete API-Schlüssel
   geändert werden kann

Aufbau des Codes:
-----------------
1. Laden und Setzen des API-Schlüssels über dotenv und openai
2. Deklaration von Funktionen, die (theoretisch) für "function calling" benötigt
   werden. Diese Funktionen geben den jeweiligen Fach-Agenten zurück.
3. Erstellung und Konfiguration der Agenten – insbesondere "Agent Dirk"
   mit dem Vermerk, dass er bestimmte Schlüsselwörter erkennt ("BGB", "HGB", usw.)
   und dann an den passenden Agenten delegieren soll.
4. Globale Variablen für den Chatverlauf `messages` und den Start-Agenten
   `current_agent`
5. Die Funktion `send_message`, die von Gradio aufgerufen wird und sowohl
   die Nutzer-Eingabe als auch die generierte Antwort in den Chatverlauf
   schreibt.
6. Die Funktion `set_api_key`, die .env aktualisiert und den globalen
   openai.api_key zur Laufzeit ändert.
7. Das Gradio-Interface (Blocks, Chatbot, Textbox, Buttons), in dem
   Nutzerinteraktionen und Anzeigen gesteuert werden.

================================================================================
"""

import gradio as gr
from swarm import Swarm, Agent
import os
from dotenv import load_dotenv, set_key
import openai

# ---------------------------------------------------------------------
# 1) .env laden und OpenAI-Schlüssel initialisieren
# ---------------------------------------------------------------------
# Wir laden die Umgebungsvariablen (insb. OPENAI_API_KEY) aus einer .env-Datei.
# Anschließend legen wir openai.api_key auf den geladenen Schlüssel.
# Danach erstellen wir einen "Swarm"-Client zur Kommunikation mit GPT-4.
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = Swarm()

# ---------------------------------------------------------------------
# 2) Definition der Agenten-Funktionen (falls "function calling" genutzt wird)
# ---------------------------------------------------------------------
# Diese Funktionen kehren jeweils ein bestimmtes Agentenobjekt zurück und
# dienen als mögliche "Functions" im Swarm-Framework, die GPT-4 aufrufen kann,
# wenn es entsprechende Schlüsselwörter erkennt (z. B. "BGB").
# In diesem Skript wird ihre Existenz vermerkt, auch wenn die automatische
# Erkennung nicht immer 1:1 verlässlich ist.
def transfer_to_agent_bgb():
    return agent_bgb

def transfer_to_agent_hgb():
    return agent_hgb

def transfer_to_agent_stgb():
    return agent_stgb

def transfer_to_agent_arbgb():
    return agent_arbgb

def transfer_to_agent_sgb():
    return agent_sgb

def transfer_to_agent_steuerrecht():
    return agent_steuerrecht

def transfer_to_agent_vwvfgg():
    return agent_vwvfgg

def transfer_to_agent_vwgo():
    return agent_vwgo

def transfer_to_agent_uwg():
    return agent_uwg

def transfer_to_agent_urhg():
    return agent_urhg

def transfer_to_agent_patg():
    return agent_patg

def transfer_to_agent_markeng():
    return agent_markeng

def transfer_to_agent_owig():
    return agent_owig

def transfer_to_agent_baubgb():
    return agent_baubgb


# ---------------------------------------------------------------------
# 3) Definition der Agenten
# ---------------------------------------------------------------------
# Hier werden die einzelnen Agent-Objekte für das Swarm-Framework erzeugt.
# Jeder Agent hat:
#  - name: Identifikationsname (z. B. "Agent BGB")
#  - instructions: Text-Anweisungen, nach denen er seine Antworten generiert
#  - model: Das GPT-4-Modell, das verwendet wird
#
# "Agent Dirk" fungiert als Verteiler-Agent, der laut seinen Instruktionen
# die Anfrage an den passenden Fach-Agenten weiterreichen soll, wenn ein
# bestimmtes Wort (z. B. "BGB", "HGB", etc.) in der Benutzeranfrage vorkommt.
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

# Diese Liste kann nützlich sein, falls wir später im Code über alle Agenten
# iterieren möchten (z. B. zur Anzeige aller Agenten).
agents_list = [
    agent_dirk, agent_bgb, agent_hgb, agent_stgb, agent_arbgb, agent_sgb,
    agent_steuerrecht, agent_vwvfgg, agent_vwgo, agent_uwg, agent_urhg,
    agent_patg, agent_markeng, agent_owig, agent_baubgb
]

# ---------------------------------------------------------------------
# 4) Zentrale Variablen & Methoden: Chat-Logik
# ---------------------------------------------------------------------
# 'messages' speichert die gesamte Unterhaltung in Form einer Liste von
# Dictionary-Objekten, die jeweils eine Rolle ("role") und den Textinhalt
# ("content") haben. "current_agent" ist der Agent, an den wir standardmäßig
# die Anfrage senden (in diesem Beispiel: Agent Dirk als Startpunkt).
messages = []
current_agent = agent_dirk  # Wir starten mit Agent Dirk

def send_message(user_input, chat_history):
    """
    Wird von Gradio aufgerufen, sobald der Nutzer eine Nachricht absendet.
    ---------------------------------------------------------------------
    Parameter:
      - user_input: Der Text, den der Nutzer eingegeben hat
      - chat_history: Die bisherige Historie, die der Chatbot in Gradio anzeigt
    ---------------------------------------------------------------------
    Ablauf:
      1) Prüfen, ob eine leere Nachricht vorliegt (falls ja, kein Update).
      2) Speichern der Nutzernachricht in unserer internen 'messages'-Liste.
      3) Aufruf von client.run(...) mit dem aktuellen Agenten (standardmäßig Dirk),
         wodurch GPT-4 eine Antwort erzeugt, ggf. an einen Fach-Agenten delegiert.
      4) Speichern der erhaltenen KI-Antwort in 'messages' und Hinzufügen zum
         Chatverlauf, das Gradio anzeigt.
      5) Rückgabe des aktualisierten chat_history an Gradio, damit dieser
         die neue Unterhaltung rendern kann.
    """
    global messages, current_agent

    # Falls nichts eingegeben wurde, aktualisieren wir den Chat nicht.
    if not user_input.strip():
        return chat_history

    # 1) User-Eingabe (Rolle: "user") in 'messages' ablegen
    messages.append({"role": "user", "content": user_input})

    # 2) GPT-4 Anfrage via Swarm
    response = client.run(agent=current_agent, messages=messages)
    agent_response = response.messages[-1]["content"]

    # 'response.agent' enthält den Agenten, der zuletzt die Antwort gegeben hat.
    answered_by = response.agent.name  # z. B. "Agent BGB" oder "Agent Dirk"

    # 3) Speichern der KI-Antwort in 'messages', Rolle: "assistant"
    messages.append({"role": "assistant", "content": agent_response})

    # 4) Auch in Gradio den Chatverlauf aktualisieren: Wir zeigen beim User-Teil
    #    in eckigen Klammern an, welcher Agent geantwortet hat. Das ist optional,
    #    macht aber nachvollziehbar, wer (laut Swarm) gesprochen hat.
    chat_history.append((f"[{answered_by}] {user_input}", agent_response))

    return chat_history

def set_api_key(new_key):
    """
    Ermöglicht das Ändern des API-Schlüssels zur Laufzeit über Gradio.
    -------------------------------------------------------------------
    Parameter:
      - new_key: Der vom Nutzer eingegebene neue API-Schlüssel
    Ablauf:
      1) Prüfen, ob der Schlüssel nicht leer ist.
      2) In der .env-Datei setzen und openai.api_key aktualisieren.
      3) Rückgabe einer Erfolgsmeldung (oder Fehlermeldung) an Gradio.
    """
    if new_key.strip():
        set_key(".env", "OPENAI_API_KEY", new_key)
        openai.api_key = new_key
        return "API-Schlüssel erfolgreich gespeichert."
    else:
        return "Kein Schlüssel eingegeben oder ungültig."


# ---------------------------------------------------------------------
# 5) Gradio-UI
# ---------------------------------------------------------------------
# Hier erstellen wir die Gradio-Benutzeroberfläche:
# - Ein "Chatbot"-Element, in dem der Konversationsverlauf angezeigt wird.
# - Eine Textbox + Button zum Absenden der Nutzereingabe.
# - Eine Textbox + Button zum Setzen eines neuen API-Schlüssels.
with gr.Blocks() as demo:
    gr.Markdown("## Swarm-Chat mit Agent Dirk (Weiterleitung zu Fachagenten)")

    # Das zentrale Chat-Widget
    chatbot = gr.Chatbot([], elem_id="chatbot", label="Chatverlauf")

    # Ein Eingabefeld und ein Button fürs Senden
    with gr.Row():
        user_input_box = gr.Textbox(
            show_label=False,
            placeholder="Ihre Nachricht eingeben...",
        )
        send_btn = gr.Button("Send")

    # Eingabefeld und Button, um den OpenAI-Schlüssel zur Laufzeit zu setzen
    api_key_input = gr.Textbox(
        show_label=True,
        label="OpenAI API-Schlüssel (Optional)",
        placeholder="Neuen Key eingeben und auf 'Speichern' klicken..."
    )
    api_key_save_btn = gr.Button("Speichern")

    # Verknüpfung von Nutzeraktionen mit den oben definierten Funktionen:
    # Sobald im user_input_box ENTER gedrückt wird, ruft Gradio 'send_message'
    # auf und übergibt (user_input_box, chatbot) als Inputs. Das Ergebnis (chat_history)
    # wird im chatbot (Ausgabe-Element) angezeigt.
    user_input_box.submit(send_message, inputs=[user_input_box, chatbot], outputs=chatbot)
    send_btn.click(send_message, inputs=[user_input_box, chatbot], outputs=chatbot)

    # Setzen des API-Schlüssels
    api_key_save_btn.click(set_api_key, inputs=api_key_input, outputs=None)

# Demo starten
demo.launch()
