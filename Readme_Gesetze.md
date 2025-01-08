# Swarm Chat

Swarm Chat ist eine Anwendung, die mehrere GPT-4-basierte Agenten verwendet, um verschiedene Arten von Anfragen zu bearbeiten. Die Anwendung nutzt die `swarm`-Bibliothek, um die Koordination und Ausführung der Agenten zu vereinfachen und zu steuern. Die Benutzeroberfläche wurde mit `customtkinter` erstellt, um ein modernes und anpassbares Design zu bieten.
![image](https://github.com/user-attachments/assets/8f0127ec-a446-49d4-a2c5-97d614cb25f8)

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
   python gesetz.py
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

Die Anwendung unterstützt derzeit mehrere Agenten, die auf verschiedene gesetzliche Fachgebiete spezialisiert sind:

1. **Agent Dirk**:
   - **Beschreibung**: Ein freundlicher Service-Agent, der Anfragen filtert und an andere Agenten weitergibt.
   - **Funktionen**: Kann Anfragen an verschiedene spezialisierte Agenten weiterleiten.

2. **Agent BGB**:
   - **Beschreibung**: Spezialisiert auf das Bürgerliche Gesetzbuch (BGB) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

3. **Agent HGB**:
   - **Beschreibung**: Spezialisiert auf das Handelsgesetzbuch (HGB) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

4. **Agent StGB**:
   - **Beschreibung**: Spezialisiert auf das Strafgesetzbuch (StGB) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

5. **Agent Arbeitsrecht**:
   - **Beschreibung**: Spezialisiert auf das Arbeitsgesetzbuch (ArbGB) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

6. **Agent Sozialrecht**:
   - **Beschreibung**: Spezialisiert auf das Sozialgesetzbuch (SGB) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

7. **Agent Steuerrecht**:
   - **Beschreibung**: Spezialisiert auf das Steuerrecht (AO, EStG, UStG, etc.) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

8. **Agent Verwaltungsverfahrensgesetz**:
   - **Beschreibung**: Spezialisiert auf das Verwaltungsverfahrensgesetz (VwVfG) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

9. **Agent Verwaltungsgerichtsordnung**:
   - **Beschreibung**: Spezialisiert auf die Verwaltungsgerichtsordnung (VwGO) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

10. **Agent Gesetz gegen den unlauteren Wettbewerb**:
    - **Beschreibung**: Spezialisiert auf das Gesetz gegen den unlauteren Wettbewerb (UWG) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

11. **Agent Urheberrechtsgesetz**:
    - **Beschreibung**: Spezialisiert auf das Urheberrechtsgesetz (UrhG) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

12. **Agent Patentrecht**:
    - **Beschreibung**: Spezialisiert auf das Patentrecht (PatG) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

13. **Agent Markengesetz**:
    - **Beschreibung**: Spezialisiert auf das Markengesetz (MarkenG) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

14. **Agent Gesetz über Ordnungswidrigkeiten**:
    - **Beschreibung**: Spezialisiert auf das Gesetz über Ordnungswidrigkeiten (OWiG) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

15. **Agent Baurecht**:
    - **Beschreibung**: Spezialisiert auf das Baugesetzbuch (BauGB) und gibt detaillierte Informationen und Ratschläge zu diesem Bereich.

## GUI

Die Benutzeroberfläche wurde mit `customtkinter` erstellt und bietet ein modernes und anpassbares Design. Die GUI unterstützt den Wechsel zwischen hellen und dunklen Themen und bietet eine einfache Möglichkeit, den OpenAI API-Schlüssel zu speichern und zu verwalten.

## Beispiele

Hier sind einige Beispiele für die Verwendung der Anwendung:

1. **Anfrage zum BGB**:
   ```
   You: Ich habe eine Frage zum Bürgerlichen Gesetzbuch.
   Agent Dirk: Ich leite Ihre Anfrage an Agent BGB weiter.
   Agent BGB: [Antwort mit detaillierten Informationen und Ratschlägen zum BGB]
   ```

2. **Anfrage zum Steuerrecht**:
   ```
   You: Ich benötige Informationen zum Steuerrecht.
   Agent Dirk: Ich leite Ihre Anfrage an Agent Steuerrecht weiter.
   Agent Steuerrecht: [Antwort mit detaillierten Informationen und Ratschlägen zum Steuerrecht]
   ```

3. **Anfrage zum Markengesetz**:
   ```
   You: Ich brauche Hilfe bei einer Frage zum Markengesetz.
   Agent Dirk: Ich leite Ihre Anfrage an Agent Markengesetz weiter.
   Agent Markengesetz: [Antwort mit detaillierten Informationen und Ratschlägen zum Markengesetz]
   ```

## Fehlerbehebung

- **Fehlermeldungen**: Überprüfen Sie die Fehlermeldungen in der Konsole, um Hinweise auf das Problem zu erhalten.
- **API-Schlüssel**: Stellen Sie sicher, dass Ihr OpenAI API-Schlüssel korrekt in der `.env`-Datei gespeichert ist.
- **Abhängigkeiten**: Stellen Sie sicher, dass alle erforderlichen Abhängigkeiten installiert sind.

## Weitere Infos zu Swarm
swarm - Bildungsressourcen-Repository
https://github.com/openai/swarm

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der [LICENSE](LICENSE)-Datei.
