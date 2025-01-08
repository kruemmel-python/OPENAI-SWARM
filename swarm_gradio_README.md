# Swarm Chat

Swarm Chat ist eine Anwendung, die mehrere GPT-4-basierte Agenten verwendet, um verschiedene Rechtsfragen zu bearbeiten. Die Anwendung nutzt die `swarm`-Bibliothek, um die Koordination und Ausführung der Agenten zu vereinfachen und zu steuern. Die Benutzeroberfläche wurde mit **Gradio** realisiert, wodurch sie über den Browser bedienbar ist und einen intuitiven Chat-Flow ermöglicht.
![image](https://github.com/user-attachments/assets/7c994981-0ce5-4620-b440-294d40bfa257)

## Inhaltsverzeichnis

- [Einführung](#einführung)
- [Funktionen](#funktionen)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Agenten](#agenten)
- [GUI](#gui)
- [Beispiele](#beispiele)
- [Fehlerbehebung](#fehlerbehebung)
- [Weitere Infos zu Swarm](#weitere-infos-zu-swarm)
- [Lizenz](#lizenz)

## Einführung

Swarm Chat ist eine Anwendung, die mehrere GPT-4-basierte Agenten verwendet, um verschiedene Arten von (insbesondere juristischen) Anfragen zu bearbeiten. Im Zentrum steht **Agent Dirk**, der als freundlicher Service-Agent fungiert und Anfragen an jeweils spezialisierte Fachagenten weiterleitet. Mithilfe der `swarm`-Bibliothek wird festgelegt, welche Schlüsselwörter (z. B. *BGB*, *HGB*, *Steuerrecht*) zu welchem Fachagenten führen sollen. Die Benutzeroberfläche wurde mit **Gradio** erstellt, sodass alle Interaktionen in einem Browserfenster erfolgen.

## Funktionen

- **Mehrere spezialisierte Agenten**: Die Anwendung bietet Fachagenten u. a. für BGB, HGB, StGB, Sozialrecht, Steuerrecht, Baurecht usw.  
- **Agent Dirk**: Leitet Fragen anhand von Schlüsselwörtern an den passenden Fachagenten weiter.  
- **Gradio-Interface**: Einfache Chat-Eingabe mit automatischer Aktualisierung des Verlaufs im Browser.  
- **API-Schlüssel-Verwaltung**: Möglichkeit, den OpenAI API-Schlüssel zur Laufzeit einzugeben oder zu ändern.  
- **Einfache Erweiterbarkeit**: Dank des Swarm-Frameworks können neue Agenten oder Themen hinzugefügt werden.

## Installation

1. **Python und Abhängigkeiten**  
   Stellen Sie sicher, dass Python installiert ist. Installieren Sie anschließend die erforderlichen Bibliotheken, z. B.:
   ```bash
   pip install gradio python-dotenv openai
   # ggf. auch das swarm-Framework (abhängig von dessen Repositorium):
   pip install git+https://github.com/openai/swarm.git
   ```

2. **.env-Datei erstellen**  
   Legen Sie eine `.env`-Datei im Projektverzeichnis an und fügen Sie Ihren OpenAI API-Schlüssel hinzu, z. B.:
   ```bash
   OPENAI_API_KEY=Ihr_OpenAI_API_Schlüssel_hier
   ```

3. **Projekt starten**  
   Führen Sie das Python-Skript aus:
   ```bash
   python ai_swarm_gradio.py
   ```
   (Der Dateiname kann variieren, je nachdem, wie Ihre Datei heißt.)

## Verwendung

1. **Starten**  
   Nach dem Start zeigt das Terminal (bzw. die Konsole) einen lokalen Link (z. B. `http://127.0.0.1:7860`). Öffnen Sie diesen Link in Ihrem Browser.

2. **Chat-Eingabe**  
   Geben Sie im Browserfenster in das Textfeld Ihre Anfrage ein und drücken Sie Enter oder klicken Sie auf den *Send*-Button. Anschließend erscheint Ihre Eingabe im Chat-Fenster sowie die vom passenden Agenten generierte Antwort.

3. **API-Schlüssel ändern**  
   Wenn Sie einen anderen OpenAI API-Schlüssel verwenden möchten, können Sie diesen in das dafür vorgesehene Textfeld eingeben und auf *Speichern* klicken. Dadurch wird die `.env`-Datei aktualisiert.

## Agenten

Die Anwendung unterstützt derzeit folgende Agenten (alle basieren auf dem GPT-4-Modell):

- **Agent Dirk**  
  *Verteiler-Agent.* Erkennt anhand von Schlüsselwörtern, welcher Fachagent zuständig ist.  
- **Agent BGB**  
  *Spezialisiert auf das Bürgerliche Gesetzbuch (BGB).*  
- **Agent HGB**  
  *Spezialisiert auf das Handelsgesetzbuch (HGB).*  
- **Agent StGB**  
  *Spezialisiert auf das Strafgesetzbuch (StGB).*  
- **Agent Arbeitsrecht**  
  *Spezialisiert auf das Arbeitsgesetzbuch (ArbGB).*  
- **Agent Sozialrecht**  
  *Spezialisiert auf das Sozialgesetzbuch (SGB).*  
- **Agent Steuerrecht**  
  *Spezialisiert auf Steuerrecht (AO, EStG, UStG, etc.).*  
- **Agent Verwaltungsverfahrensgesetz**  
  *Spezialisiert auf das VwVfG.*  
- **Agent Verwaltungsgerichtsordnung**  
  *Spezialisiert auf die VwGO.*  
- **Agent Gesetz gegen den unlauteren Wettbewerb**  
  *Spezialisiert auf das UWG.*  
- **Agent Urheberrechtsgesetz**  
  *Spezialisiert auf das UrhG.*  
- **Agent Patentrecht**  
  *Spezialisiert auf das PatG.*  
- **Agent Markengesetz**  
  *Spezialisiert auf das MarkenG.*  
- **Agent Gesetz über Ordnungswidrigkeiten**  
  *Spezialisiert auf das OWiG.*  
- **Agent Baurecht**  
  *Spezialisiert auf das BauGB.*

## GUI

Die Benutzeroberfläche verwendet **Gradio**, sodass Sie über Ihren Browser mit dem Chat interagieren können.  
- Das **Chatbot**-Element zeigt den Gesprächsverlauf.  
- Eine **Textbox** ermöglicht das Eingeben von Nachrichten, die Sie über *Enter* oder den *Send*-Button senden können.  
- Ein **zusätzliches Textfeld** erlaubt Ihnen, zur Laufzeit Ihren OpenAI-API-Schlüssel zu ändern.

## Beispiele

1. **Frage zum BGB**  
   ```
   User: Welche Gewährleistungsrechte habe ich beim Privatkauf eines Autos?
   Agent Dirk: Leitet aufgrund des Schlüsselworts 'BGB' an Agent BGB weiter.
   Agent BGB: [Erklärt die Regelungen zu Sachmängeln, Rücktritt, Minderung, etc.]
   ```
2. **Frage zum OWiG**  
   ```
   User: Was passiert, wenn ich falsch geparkt habe und ein Strafzettel kommt?
   Agent Dirk: Leitet aufgrund 'Ordnungswidrigkeiten' an Agent Gesetz über Ordnungswidrigkeiten weiter.
   Agent Gesetz über Ordnungswidrigkeiten: [Erklärt die Rechtsgrundlage laut OWiG, Bußgeldverfahren usw.]
   ```

## Fehlerbehebung

- **Keine oder leere Antworten**: Prüfen Sie, ob Ihr API-Schlüssel korrekt eingetragen ist (entweder in `.env` oder manuell über die GUI).  
- **Konsole überprüfen**: Sehen Sie sich ggf. das Terminal an, in dem das Skript läuft, um Fehlermeldungen zu ermitteln.  
- **Richtige Python-Version**: Achten Sie darauf, dass Sie eine aktuelle Python-Version (mind. 3.9 oder höher) verwenden.

## Weitere Infos zu Swarm

- [swarm - Bildungsressourcen-Repository](https://github.com/openai/swarm)

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der [LICENSE](LICENSE)-Datei.
