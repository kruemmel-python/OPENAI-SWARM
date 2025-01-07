# Swarm Chat

Swarm Chat ist eine Anwendung, die mehrere GPT-4-basierte Agenten verwendet, um verschiedene Arten von Anfragen zu bearbeiten. Die Anwendung nutzt die `swarm`-Bibliothek, um die Koordination und Ausführung der Agenten zu vereinfachen und zu steuern. Die Benutzeroberfläche wurde mit `customtkinter` erstellt, um ein modernes und anpassbares Design zu bieten.

## Inhaltsverzeichnis

- [Einführung](#einführung)
- [Funktionen](#funktionen)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Agenten](#agenten)
- [GUI](#gui)
- [Beispiele](#beispiele)
- [Fehlerbehebung](#fehlerbehebung)
- [Lizenz](#lizenz)

## Einführung

Swarm Chat ist eine Anwendung, die mehrere GPT-4-basierte Agenten verwendet, um verschiedene Arten von Anfragen zu bearbeiten. Die Anwendung nutzt die `swarm`-Bibliothek, um die Koordination und Ausführung der Agenten zu vereinfachen und zu steuern. Die Benutzeroberfläche wurde mit `customtkinter` erstellt, um ein modernes und anpassbares Design zu bieten.

## Funktionen

- **Mehrere Agenten**: Die Anwendung unterstützt mehrere Agenten, die auf verschiedene Arten von Anfragen spezialisiert sind.
- **Dynamische Übergaben**: Agenten können die Ausführung an andere Agenten übergeben, um spezifische Anfragen zu bearbeiten.
- **Anpassbare GUI**: Die Benutzeroberfläche wurde mit `customtkinter` erstellt und bietet ein modernes und anpassbares Design.
- **Themenwechsel**: Die Anwendung unterstützt den Wechsel zwischen hellen und dunklen Themen.
- **API-Schlüssel-Verwaltung**: Die Anwendung bietet eine einfache Möglichkeit, den OpenAI API-Schlüssel zu speichern und zu verwalten.

## Installation

1. **Abhängigkeiten installieren**:
   Stellen Sie sicher, dass Sie Python installiert haben. Installieren Sie die erforderlichen Abhängigkeiten mit `pip`:
   ```sh
   pip install customtkinter python-dotenv openai
   pip install git+https://github.com/openai/swarm.git
   ```

2. **API-Schlüssel**:
   Erstellen Sie eine `.env`-Datei im Projektverzeichnis und fügen Sie Ihren OpenAI API-Schlüssel hinzu:
   ```
   OPENAI_API_KEY=Ihr_OpenAI_API_Schlüssel_hier
   ```

3. **Anwendung starten**:
   Führen Sie die Anwendung aus:
   ```sh
   python ai_swarm.py
   ```

## Verwendung

1. **Anwendung starten**:
   Starten Sie die Anwendung, indem Sie den oben genannten Befehl ausführen.

2. **Nachricht senden**:
   Geben Sie Ihre Anfrage in das Eingabefeld ein und klicken Sie auf "Send". Der entsprechende Agent wird Ihre Anfrage bearbeiten und eine Antwort liefern.

3. **Thema ändern**:
   Verwenden Sie das Menü "Themen", um zwischen hellen und dunklen Themen zu wechseln.

4. **API-Schlüssel speichern**:
   Geben Sie Ihren OpenAI API-Schlüssel in das entsprechende Eingabefeld ein und klicken Sie auf "Speichern", um den Schlüssel in der `.env`-Datei zu speichern.

## Agenten

Die Anwendung unterstützt derzeit vier Agenten:

1. **Agent Dirk**:
   - **Beschreibung**: Ein freundlicher Service-Agent, der Anfragen filtert und an andere Agenten weitergibt.
   - **Funktionen**: Kann Anfragen an Agent Mona, Agent Peter und Agent Ralf weiterleiten.

2. **Agent Mona**:
   - **Beschreibung**: Spezialisiert auf die Analyse und Erstellung von professionellem Python-Code.

3. **Agent Peter**:
   - **Beschreibung**: Spezialisiert auf Windows-Probleme und bietet detaillierte Anweisungen zur Lösung.

4. **Agent Ralf**:
   - **Beschreibung**: Spezialisiert auf PowerShell-Prompts und bietet detaillierte Anweisungen zur Lösung.

## GUI

Die Benutzeroberfläche wurde mit `customtkinter` erstellt und bietet ein modernes und anpassbares Design. Die GUI unterstützt den Wechsel zwischen hellen und dunklen Themen und bietet eine einfache Möglichkeit, den OpenAI API-Schlüssel zu speichern und zu verwalten.

## Beispiele

Hier sind einige Beispiele für die Verwendung der Anwendung:

1. **Python-Code-Analyse**:
   ```
   You: Ich brauche Hilfe bei der Analyse von Python-Code.
   Agent Dirk: Ich leite Ihre Anfrage an Agent Mona weiter.
   Agent Mona: [Antwort mit Python-Code-Analyse]
   ```

2. **Windows-Probleme**:
   ```
   You: Ich habe ein Problem mit meinem Windows-Betriebssystem.
   Agent Dirk: Ich leite Ihre Anfrage an Agent Peter weiter.
   Agent Peter: [Antwort mit detaillierten Anweisungen zur Lösung des Windows-Problems]
   ```

3. **PowerShell-Prompts**:
   ```
   You: Ich brauche Hilfe bei einem PowerShell-Prompt.
   Agent Dirk: Ich leite Ihre Anfrage an Agent Ralf weiter.
   Agent Ralf: [Antwort mit detaillierten Anweisungen zur Lösung des PowerShell-Prompts]
   ```

## Fehlerbehebung

- **Fehlermeldungen**: Überprüfen Sie die Fehlermeldungen in der Konsole, um Hinweise auf das Problem zu erhalten.
- **API-Schlüssel**: Stellen Sie sicher, dass Ihr OpenAI API-Schlüssel korrekt in der `.env`-Datei gespeichert ist.
- **Abhängigkeiten**: Stellen Sie sicher, dass alle erforderlichen Abhängigkeiten installiert sind.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der [LICENSE](LICENSE)-Datei.
