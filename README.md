<div align="center">

# PDF-RAG-Assistant

### Schluss mit PDF öffnen, scrollen, suchen.

**Der KI-Assistent, der einen ganzen Ordner voller PDFs liest<br>und jede Frage dazu in Sekunden beantwortet. Mit Beleg.**

![Status](https://img.shields.io/badge/Status-Prototyp-orange)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![RAG](https://img.shields.io/badge/Architektur-RAG-8A2BE2)
![Vektordatenbank](https://img.shields.io/badge/Vektordatenbank-Chroma-green)
![LLM](https://img.shields.io/badge/LLM-Claude%20API-black)

[Was es kann](#was-es-kann) · [Mehrwert](#mehrwert) · [Datenschutz](#datenschutz) · [Demo](#demo) · [Ausblick](#ausblick) · [Schnellstart](#schnellstart)

</div>

---

**Heute:** Dokument suchen, öffnen, durchlesen, Angabe heraussuchen, beim nächsten Dokument von vorn.

**Mit diesem System:** Frage eintippen. Fertig.

## Was es kann

| | | |
| --- | --- | --- |
| 💬 | **Versteht normale Sprache** | Keine Suchbegriffe, keine Schulung |
| 📂 | **Liest den ganzen Ordner** | Jede PDF im Ordner wird eingelesen und durchsuchbar |
| 📄 | **Antwortet aus Ihren Dokumenten** | Nicht aus allgemeinem Internetwissen |
| 🔗 | **Verbindet Informationen** | Kombiniert Angaben aus mehreren Dokumenten |
| 📎 | **Belegt jede Antwort** | Die Quelle steht immer dabei |
| 🛑 | **Erfindet nichts** | Fehlt eine Information, sagt das System das |

## Mehrwert

- **Schnellere Entscheidungen:** Informationen in Sekunden statt nach langer Suche
- **Entlastete Mitarbeiter:** Weniger Suchen, weniger Rückfragen
- **Wissen für alle:** Auskunft unabhängig von Abteilung und Erfahrung
- **Vertrauen:** Jede Antwort ist am Originaldokument prüfbar

## Datenschutz

- **Ihre Dokumente bleiben bei Ihnen:** PDFs, Suchindex und Suche liegen lokal
- **Minimale Weitergabe:** Nur die wenigen Textabschnitte, die zur Frage passen, gehen an das Sprachmodell. Nie das ganze Archiv
- **Geplant: vollständig interner Betrieb.** Mit einem lokalen Sprachmodell verlässt kein Zeichen das Unternehmen

## Warum ein eigenes System statt eines Chat-Tools?

Ein Chat-Tool hilft einer Person mit einigen Dateien. Dieses System ist ein Baustein für das ganze Unternehmen:

| | Chat-Tool | Dieses System |
| --- | --- | --- |
| **Umfang** | Einzelne Dateien pro Unterhaltung | Ausgelegt auf den gesamten Dokumentenbestand |
| **Einbindung** | Eigene Oberfläche | In bestehende Systeme integrierbar, z. B. SAP |
| **Kontrolle** | Anbieter entscheidet | Modell, Suche und Speicherort frei wählbar |
| **Daten** | Ganze Dateien werden hochgeladen | Nur passende Abschnitte gehen ans Modell |

## Demo

Beispielfragen an die Musterbelege im Ordner `docs` (eine Rechnung, eine Bestellung):

| Frage | Antwort aus den Dokumenten |
| --- | --- |
| Wie hoch ist der Rechnungsbetrag der Rechnung 90001234? | 3.242,75 EUR, Quelle: Musterrechnung |
| Was haben wir bei TechParts bestellt und wann wird geliefert? | 50 Edelstahlwellen und 10 Kanister Industrieschmierstoff, Liefertermin 02.12.2026, Quelle: Musterbestellung |
| Vergleiche die Zahlungsbedingungen von Kunde und Lieferant. | Kunde: 14 Tage ohne Abzug. Lieferant: 30 Tage netto, 2 % Skonto bei 14 Tagen. Quellen: beide Belege |


So sieht ein Aufruf aus:

```powershell
python rag.py "Wie hoch ist der Rechnungsbetrag der Rechnung 90001234?"
```

Die Ausgabe beginnt mit den verwendeten Quellen, danach folgt die Antwort.

## Ausblick

Noch nicht umgesetzt, baut aber direkt auf dem Prototyp auf:

| Ausbaustufe | Nutzen |
| --- | --- |
| **Vollständig interner Betrieb** | Lokales Sprachmodell, kein Zeichen verlässt das Unternehmen |
| **Tausende Dokumente** | Das gesamte Archiv in einem Schritt durchsuchen |
| **Automatisches Sortieren** | PDFs nach Dokumentart und Inhalt einordnen |
| **Auswertungen auf Zuruf** | Übersichten über viele Dokumente hinweg |
| **Automatische Prüfung** | Dokumente abgleichen, Abweichungen melden |
| **Gescannte Unterlagen** | Auch Papierdokumente werden lesbar |
| **Oberfläche und Zugriffsrechte** | Bedienung im Browser, jeder sieht nur, was er darf |
| **Anbindung an SAP** | Betrieb auf der SAP Business Technology Platform |
| **KI-Agenten** | Digitale Assistenten nutzen das Dokumentenwissen selbstständig |

---

## Schnellstart

Voraussetzungen: Python 3.13, Git, API-Key aus der [Anthropic Console](https://console.anthropic.com)

```powershell
git clone https://github.com/oemer-systems/pdf-rag-assistant.git
cd pdf-rag-assistant
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
$env:ANTHROPIC_API_KEY="dein-key"
```

PDFs in den Ordner `docs` legen, dann:

```powershell
python rag.py ingest          # Dokumente einlesen
python rag.py "Deine Frage"   # Frage stellen
```

## Technik

`PDF einlesen` → `in Abschnitte teilen` → `als Vektoren speichern` → `passende Abschnitte suchen` → `Antwort mit Quelle erzeugen`

RAG-Pipeline (Retrieval-Augmented Generation) mit Python, Chroma, pypdf und der Claude API.


## Stand des Prototyps

- Getestet mit wenigen Musterdokumenten
- Bedienung über das Terminal, noch keine Zugriffsrechte
- Textabschnitte gehen an eine externe API, vor dem Einsatz mit echten Daten ist eine Datenschutzprüfung nötig

---

<div align="center">

Lernprojekt, mit KI-Unterstützung entwickelt. Die Musterbelege (Rechnung, Bestellung) im Ordner `docs` sind frei erfunden.

**Kontakt:** [github.com/oemer-systems](https://github.com/oemer-systems)

</div>
