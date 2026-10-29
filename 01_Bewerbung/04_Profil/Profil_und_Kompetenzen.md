# Bewerberprofil und Kompetenzübersicht

**Interne Arbeitsgrundlage für Bewerbungen – geprüft am 21.10.2026.**
Dieses Profil trennt belegte Angaben, eigene Projektbeschreibungen und
Weiterentwicklungsfelder. Die ergänzende lokale Dateisuche umfasste relevante
Unterlagen und Quelltexte in den persönlichen Dokumente-, Downloads- und
OneDrive-/Hochschulordnern. Windows-, Programm-, Cache- und
Abhängigkeitsverzeichnisse wurden nicht inhaltlich durchsucht. Bei Widersprüchen
haben Zeugnisse und die jeweils aktuelle Quelldatei Vorrang vor älteren
Anschreiben oder Positionierungsnotizen.

## Profil in Kürze

Systems-Engineering-Student und ausgebildeter Mechatroniker mit industrieller
Praxiserfahrung in Vorinbetriebnahme, Funktionsprüfung und Fehlersuche sowie
praktischen Projekten an der Schnittstelle von Python, Datenintegration,
Automatisierung und KI. Besonders überzeugend ist die Verbindung aus
mechatronischem Verständnis, analytischer Arbeitsweise und dem Blick auf das
Zusammenspiel von Software und realen Produktionsabläufen.

Passende Zielrichtungen sind Python-/Softwareentwicklung mit Daten- oder
KI-Bezug, Data Science im industriellen Umfeld, technische Systemintegration
sowie die Umsetzung und Erprobung digitaler Produktionslösungen.

## Ausbildung und Berufspraxis

### Studium

- **Systems Engineering, Technische Hochschule Augsburg**, laut Lebenslauf seit
  2022; Schwerpunkt unter anderem auf Informatik, industrieller
  Informationsverarbeitung, Embedded Systems, industrieller Bildverarbeitung,
  verteilten und sicheren Industriesystemen sowie Datenkommunikation.
- Der aktuelle Notenstand bezeichnet den Bachelor als **angestrebten
  Abschluss**. In den geprüften Unterlagen war kein Abschlusszeugnis enthalten;
  Bewerbungen sollten daher den Abschluss nicht als bereits erworben darstellen,
  solange kein aktueller Nachweis vorliegt.

### Berufsausbildung und Industrie

- **Mechatronik-Ausbildung** bei Klein GmbH (2018–2020) und GROB-WERKE
  (2021–2022); Ausbildungszeugnis und Lebenslauf führen den Abschluss als
  Mechatroniker.
- **GROB-WERKE GmbH & Co. KG, Mechatroniker in der Vorinbetriebnahme**,
  laut Lebenslauf seit 2022, parallel zum Studium mit 21 Wochenstunden.
- Im Lebenslauf dokumentierte Aufgaben: Vorinbetriebnahme, Funktionsprüfung,
  Fehleranalyse und Zusammenarbeit mit Konstruktion, Montage,
  Softwareentwicklung und Fachabteilungen. Ebenfalls angegeben sind
  internationale Montage- und Inbetriebnahmeeinsätze in Spanien, Mexiko und
  Indien.
- Das Profil verbindet damit praktische Anlagenkenntnis mit systematischer
  Fehlersuche, Schnittstellenverständnis und Zusammenarbeit in
  interdisziplinären Teams.

### Technologie-Transferzentrum Leipheim

Die studentische Tätigkeit ist im Lebenslauf mit 2025 bis August 2026
angegeben. Die Aufgabenbeschreibung und das Arbeitszeugnis belegen folgende
praktische Arbeiten:

- Entwicklung und Erprobung einer Pick-by-Light-Anwendung.
- Python-Konnektor zur API-Anbindung einer NEXT-LAB-Cloud-Lösung und
  bidirektionale Integration mit einem MES: Fertigungsaufträge wurden an die
  Werkerführung übergeben und Bearbeitungs- sowie Auftragsstatus an das MES
  zurückgemeldet.
- Programmierung und Integration eines Omron-AMR über ARCL und einen
  Python-Konnektor; definierte Routen und eine Werkerinteraktion per Tastendruck
  wurden in den Materialbereitstellungsprozess integriert und erprobt.
- Technische Recherche und Evaluierung zu KI-gestützter Werkerführung für einen
  Prusa-HT90-3D-Drucker, einschließlich Betrachtung von Prototypen,
  Bedienoberflächen und Integrationsfähigkeit. Das belegt Evaluierungs- und
  Konzeptarbeit, nicht die Entwicklung eines produktiven KI-Modells.
- Implementierung eines Werkzeugmanagementsystems mit strukturierter
  Lagerplatzadressierung und Bezug zur 5S-Methodik.

## Software-, Daten- und KI-Projekte

### Bachelorarbeit: EPLAN-Makro-Ranking

Die eingereichte Bachelorarbeit trägt den Titel **„Proximitätssuche von
EPLAN-Makros auf Basis des LambdaRank-Algorithmus“**. Der Volltext belegt:

- Entwicklung einer Python-Pipeline zur Datenaufbereitung, zum Training und
  zur Evaluation eines LightGBM-LambdaRank-Rankingsystems.
- Strukturierung von Artikel- und Makrodaten in Merkmale und Kandidatenprofile;
  die Arbeit wertet 375 Kandidatenprofile aus.
- Vergleich mehrerer Modellkonfigurationen und Auswertung mit
  Recall@k, Mean Reciprocal Rank, Family Recall und hierarchischem nDCG.
- Getrennte Trainings-, Validierungs- und Testdaten. Identische
  Merkmals-Fingerprints werden beim Split gruppiert; eine gesonderte
  Leakage-Sicherheitsprüfung kontrolliert unter anderem Überschneidungen und
  die Nutzung von Zielinformationen. Der Testdatensatz wird erst nach der
  Modellauswahl zur abschließenden Bewertung herangezogen.
- Für den ausgewiesenen Testlauf: Recall@1 **34,78 %**, Recall@3 **47,83 %**,
  Recall@10 **67,98 %**, MRR **0,4534**, Family Recall@1 **87,35 %** und
  hierarchisches nDCG@10 **0,7449**.

Die Arbeit belegt so insbesondere Datenaufbereitung, Feature Engineering,
Ranking, reproduzierbare Evaluation, Fehleranalyse und einen sorgfältigen
Umgang mit Datenleckage. Sie belegt keine produktive Bereitstellung des Modells
in einer Unternehmensumgebung.

**Abgleichhinweis:** Zusätzlich hast du angegeben, dich im Rahmen der
Bachelorarbeit mit Sentence-Transformern, Embedding-Modellen und
LLM-Fine-Tuning beschäftigt zu haben. Im lokalen Python-Codebestand wurde
zusätzlich ein konkretes Sentence-Transformer-Skript gefunden; damit ist die
Arbeit mit Embeddings und Cosine Similarity durch Quellcode gestützt, aber nicht
eindeutig der eingereichten Bachelorarbeit zuzuordnen. Die Bachelorarbeits-PDF
selbst beschreibt diese Methode nicht nachvollziehbar. LLM-Fine-Tuning wird
weder durch die PDF noch durch die geprüften lokalen Quelltexte belegt. Die
Themen sind daher nachfolgend mit ihrer jeweiligen Beleggrenze getrennt
festgehalten.

### Datenintegration und Prozessanalyse

Der Lebenslauf-Generator und firmenspezifische Projektbeschreibungen nennen:

- Python-basierte Provisionierung von Produkt-, Stücklisten-, Lager- und
  Produktionsdaten mit Odoo-XML-RPC und Datenvalidierung.
- Odoo-zu-Celonis-Datenpipeline zur Erstellung von Event Logs und zur
  Prozessanalyse beziehungsweise Wertstrombetrachtung in Celonis.
- Datenflüsse zwischen Cloud-Diensten, MES, ERP-Daten und
  Produktionsprozessen.

Diese Kompetenzen sind im Bewerbungsprojekt beschrieben; für konkrete
Bewerbungen sollten die eigene Rolle, der tatsächlich umgesetzte Umfang und
verwendete Schnittstellen bei Bedarf anhand der Projektunterlagen präzisiert
werden.

Eine ergänzend gefundene Odoo-Celonis-Projektdokumentation beschreibt eine
umgesetzte Datenpipeline mit technischer Staging-Schicht, normalisierten
Dimensionstabellen und einem vereinheitlichten Event Log. Der dokumentierte
Ablauf umfasst außerdem Datenübernahme und -modellierung in Celonis sowie die
Bereitstellung von Analysen und KPIs in Celonis Studio. Das stützt Erfahrung mit
ETL-/Datenmodellierungs- und Process-Mining-Abläufen; konkrete SQL-Skripte oder
die produktive Betriebsverantwortung sind mit dieser Dokumentation allein nicht
nachgewiesen.

### Weiterer lokaler KI- und Ranking-Codebestand

Außerhalb des Bewerbungsordners wurde unter `C:\Users\andre\Downloads\src`
ein umfangreicher Python-Codebestand zu Artikel-/Makro-Retrieval und Ranking
gefunden. Die Dateien belegen im Quelltext folgende technische Ansätze:

- Ein Skript lädt `sentence-transformers/all-MiniLM-L6-v2`, erzeugt
  Satz-Embeddings und berechnet Cosine Similarity für Textpaare. Die Ähnlichkeit
  wird unter anderem zur Label-Prüfung mit konfigurierten Schwellenwerten
  herangezogen. Das ist die Verwendung eines vortrainierten Sentence
  Transformers, kein Nachweis für dessen Fine-Tuning.
- Eine separate Retrieval-Pipeline bildet strukturierte Produktmerkmale als
  Feature-Vektoren ab und kombiniert BM25-Textsuche, gewichtete
  Merkmalsähnlichkeit, Kandidatenaggregation und Re-Ranking.
- Ein zusätzlicher Trainingslauf implementiert einen Makro-Klassifikator mit
  `SGDClassifier` sowie einen paarweisen Artikel-Ranker mit `SGDRegressor`.
  Die Paarmerkmale umfassen Differenzen und elementweise Produkte von
  Sparse-Vektoren. Die Konfiguration sieht getrennte Train-,
  Development- und Validation-Splits, reproduzierbare Seeds sowie Auswahl-
  und Evaluationsmetriken wie Recall@k, Precision@k, Hit Rate, nDCG@10 und
  MRR vor.
- Weitere Module behandeln train-only Feature-Transformationen,
  Daten-/Vertragsvalidierung, Leakage-Schutz sowie Modell-Metadaten,
  Backups und eine Vorbereitung für den Modell-Deployment-Transfer.

Das belegt zusätzliche praktische Beschäftigung mit semantischen Embeddings,
Information Retrieval, Feature Engineering und klassischen ML-Rankingverfahren.
Der lokale Bestand enthält jedoch keine dazugehörigen trainierten
Modellartefakte oder protokollierten Ergebnisse; die Ausführung, Güte und
Bereitstellung dieses separaten Codes sind damit nicht belegt. Es wurden dort
auch keine Implementierungen von LLM-Fine-Tuning, PEFT/LoRA oder QLoRA
gefunden. Die im Modellmanagement erwähnte Unterstützung von
Hugging-Face-Dateiformaten ist für sich kein Fine-Tuning-Nachweis.

### Studienprojekte: Messdatenerfassung und technische Projektplanung

Im Python-Code eines Studienprojekts aus dem ersten Semester ist ein
Messaufbau mit Raspberry Pi, I²C-Bus und ADS1115-Analog-Digital-Wandler
dokumentiert. Die Software liest Messwerte eines Peltier-Aufbaus ein,
berechnet Spannung, Strom, Leistung und Energie, protokolliert Messreihen als
CSV und stellt Messdaten mit Pandas und Matplotlib grafisch dar. Das stützt
Grundlagen in Python, Sensor-/Hardwareanbindung, Messdatenerfassung,
Datenaufbereitung und technischer Auswertung im Studienkontext.

Projektmanagement-Unterlagen aus dem Systems-Engineering-Studium dokumentieren
außerdem Einzelarbeiten zu Stakeholdermanagement, Projektstrukturplan,
RACI-Matrix, Aufwandsschätzung, Termin- und Ressourcenplanung sowie Kosten-
und Earned-Value-Auswertung. Eine Projektplanung zur Lernfabrik behandelt
Datenarchitektur, IIoT-Schnittstellen, Digital Twin, Visualisierung und
Simulation als konzeptionelle Arbeitspakete. Eine weitere Systems-Engineering-
Projektarbeit dokumentiert Aufgaben zu Projektzielen, Stakeholdern,
Risikobetrachtung, Arbeitspaketen, Team- und Ressourcenplanung sowie
Meilensteinen. Das sind Studien- und Planungserfahrungen, kein Nachweis, dass
die dort entworfenen Digital-Twin-, Cloud-, Datenbank- oder
Simulationslösungen produktiv implementiert wurden.

### Gewächshaus-Prototyp: Weboberfläche, Sensorik und MQTT

Im Hochschulordner liegen sowohl ein Pflichtenheft als auch ein
Python-/Web-Codebestand für ein Gewächshausprojekt. Das Pflichtenheft beschreibt
unter anderem Temperatur- und Feuchtesensorik, eine motorisierte Dachluke,
Wasserventile sowie Anforderungen an Anzeige und Steuerung über eine
Weboberfläche. Es hält mehrere konkrete Hardware- und Softwareentscheidungen
noch als offene Auswahl fest.

Der lokale Codebestand dokumentiert einen funktionsorientierten Prototyp mit:

- Flask-Dashboard und HTML-Ansichten für Sensordaten und Wettervorhersage.
- MQTT-Nachrichtenfluss für Sensordaten und Fotos sowie eine
  HTTP-Schnittstelle zum Senden von Steuerbefehlen.
- SQLite-Speicherung von Sensormessungen und Bilddaten.
- Python-Modulen für Wettervorhersage, zeitgesteuerte Auswertung und
  wetterabhängige Bewässerungsbefehle.

Das ist konkreter Beleg für die Verbindung von Webentwicklung,
API-/Messaging-Integration, Datenhaltung und Systemkonzeption im Studienprojekt.
Der Ordner ist als Backup/Prototyp abgelegt; der Code wurde im Rahmen dieser
Recherche nur statisch gelesen und auf Python-Syntax geparst, nicht gegen
Hardware oder einen MQTT-Broker ausgeführt. Eine produktive Bereitstellung und
eine automatische Lüftungssteuerung sind durch die geprüften Dateien nicht
belegt. Hardwarewahl, Microcontroller-Firmware und Teile der Steuerlogik sind
im Pflichtenheft noch offen.

### Weitere selbst beschriebene Projekte

In früheren Bewerbungsunterlagen wurden außerdem folgende Projekte
beschrieben. Die zugehörigen Quellprojekte liegen nicht als eigenständige
Implementierungsnachweise in diesem Projektordner vor:

- Make-Workflow zur Verarbeitung von Excel-Daten und automatisierten
  Newsletter-Entwürfen mit einem OpenAI-Modell. Die Anschreiben nennen
  „GPT-6“; die genaue Modellbezeichnung und der real eingesetzte Dienst sollten
  vor einer erneuten Verwendung überprüft werden.
- Kassen-App für einen Verein.

Diese Beispiele sind als eigene Projektangaben verwendbar, sollten aber nicht
mit Arbeitszeugnissen oder im Ordner vorhandenen Quellcode gleichgesetzt
werden.

## Kompetenzübersicht

| Kompetenzfeld | belastbar beschreibbarer Stand |
|---|---|
| Python-Entwicklung | Bachelorarbeit, Datenpipelines, Konnektoren und Integrationsprojekte |
| APIs und Systemintegration | API-/Cloud-/MES-Anbindung im TTZ; Odoo-XML-RPC laut Projektbeschreibung |
| Machine Learning | LightGBM, LambdaRank, Feature Engineering, Ranking, Modellvergleich und Evaluation |
| Embeddings und Retrieval | Sentence-Transformer-Embeddings, Cosine Similarity, BM25, gewichtete Merkmalsähnlichkeit und Re-Ranking laut lokalem Quellcode; Ausführung nicht nachgewiesen |
| Datenqualität | strukturierte Splits, gruppierte Fingerprints, Leakage-Prüfung und Testdatenauswertung |
| Python-ML-Implementierung | Sparse-Features, SGDClassifier/SGDRegressor, reproduzierbare Splits und Rankingmetriken laut lokalem Codebestand |
| Produktionssysteme | Vorinbetriebnahme, Funktionstests, Fehlersuche, MES, Pick-by-Light und AMR |
| Datenanalyse/Prozess | Odoo-/Celonis-Datenpipeline, Staging/Normalisierung, Event Logs und Process Mining laut Projektdokumentation |
| Sensorik und Messdaten | Raspberry Pi, I²C/ADS1115, CSV-Messreihen, Pandas und Matplotlib im Studienprojekt |
| Web- und IoT-Integration | Flask, HTML, SQLite, MQTT, Sensordaten-/Fotoübertragung, HTTP-Steuerbefehle und Wetterdaten im Gewächshaus-Prototyp |
| Prototyping und Evaluierung | 3D-Druck, technische Lösungsrecherche, Werkerführung und Werkzeugmanagement |
| Zusammenarbeit | Schnittstellenarbeit zwischen Mechanik, Elektrik, Software und Fachbereichen; internationale Einsätze laut Lebenslauf |
| Systems Engineering/Projektorganisation | Stakeholder, Projektstrukturplan, RACI, Aufwand, Termine, Ressourcen, Kosten und Earned Value im Studienkontext; GPM-Basiszertifikat |
| Web/Automatisierung | HTML, CSS, JavaScript, Wetter-API, Make und Vereins-Kassen-App laut eigenen Projektbeschreibungen |

**Sprachen laut Lebenslauf:** Deutsch (Muttersprache), Englisch (B1).

## Beleglage und Positionierungsgrenzen

### Durch Unterlagen besonders gut belegt

- Mechatronik-Ausbildung und industrielle Anlagenpraxis.
- Praktische Schnittstellen- und Integrationsarbeit mit Python, API, Cloud,
  MES und AMR.
- Bachelorarbeit mit eigenständig entwickelter und ausgewerteter
  Ranking-Pipeline.
- Analytisches Vorgehen, technische Fehlersuche, strukturierte Tests und
  Ergebnisbewertung.
- Zusammenarbeit mit technischen und fachlichen Beteiligten.

### Als eigene Projektangaben, für die weitere Primärbelege hilfreich wären

- Genaue Zuordnung des gefundenen Sentence-Transformer-Skripts zur
  Bachelorarbeit sowie Nachweis seiner tatsächlichen Ausführung.
- LLM-Fine-Tuning im Bachelorarbeitskontext: bisher nur eigene Angabe; lokale
  Primärbelege wurden nicht gefunden.
- Odoo-/Celonis-, Make- und Kassen-App-Projekte, soweit konkrete
  Umsetzungstiefe oder Ergebnisse behauptet werden.
- Produktiver Betrieb oder vollständige Hardwareintegration des
  Gewächshaus-Prototyps; im lokalen Ordner liegen Backup- und Studienartefakte,
  kein Betriebs- oder Abnahmenachweis.
- Verwendete Version des OpenAI-Modells im Make-Newsletter-Workflow.
- Autorschaft und Umfang einer weiteren lokalen Python-Anwendung für
  Rechnungs-/Kassenprozesse; wegen fehlender eindeutiger Zuordnung nicht als
  bestätigte Erfahrung in das Profil aufgenommen.

### Nicht als vorhandene Praxiserfahrung behaupten, sofern keine neuen Belege vorliegen

- Produktiver Betrieb von RAG-Systemen, QLoRA-Fine-Tuning oder selbst
  entwickelten LLMs.
- Berufliche Implementierung mit Copilot Studio, SAP Joule oder Power
  Platform.
- Umfangreiche Cloud-, DevOps-, Container-Orchestrierungs- oder
  Infrastructure-as-Code-Praxis.
- Produktiver Rollout einer KI-Werkerführung oder eigenständige Entwicklung
  eines trainierten KI-Modells im TTZ.

Diese Felder können als Interesse, Lernziel oder nächste fachliche Entwicklung
formuliert werden, nicht als bereits belegte Erfahrung.

## Quellen im Projekt

- [Bachelorarbeit](../Inhalte_Studium/Bachelorarbeit.pdf)
- [Notenstand Hochschule](../Zeugnisse/Notenstand_Hochschule.pdf)
- [Lebenslauf-Quelldatei](./code/lebenslauf/lebenslauf.py) und
  [Lebenslauf-PDF](../Zeugnisse/Lebenslauf.pdf)
- [Arbeitszeugnis HNU](../Zeugnisse/Arbeitszeugnis_HNU.pdf)
- [Arbeitszeugnis GROB](../Zeugnisse/Arbeitszeugnis_GROB.pdf)
- [TTZ-Aufgabenbeschreibung](../Arbeitszeugnisse/Aufgaben_TTZ_Arbeitszeugnis.docx)
- [Ausbildungszeugnis](../Zeugnisse/Ausbildungszeugnis.pdf)
- [GPM-Basiszertifikat](../Zeugnisse/GPM_Basiszertifikat.pdf)
- [Interne KI-Positionierungsnotizen](../KI-Recherche.txt) – nicht als
  unabhängiger Umsetzungsnachweis zu verwenden.
- Lokaler KI-/Ranking-Codebestand außerhalb dieses Repositories:
  `C:\Users\andre\Downloads\src\utils\quantification.py`,
  `C:\Users\andre\Downloads\src\pipeline\400_training\P400_train_macro_and_article_rankers.py`
  und `C:\Users\andre\Downloads\src\retrieval\`.
- Studienprojekt Messdatenerfassung:
  `C:\Users\andre\OneDrive - hs-augsburg.de\Studium_Systems_Engineering\Semester 1\Projekt_1\Workspace\src\Code\`.
- Odoo-/Celonis-Projektdokumentation:
  `C:\Users\andre\Downloads\odoo_celonis_zusammenfassung_kurz.docx`.
- Studiennachweise für Systems-Engineering-Projektplanung:
  `C:\Users\andre\Downloads\SE_2147455_AlstetterAndreas_Projektdesing.pdf`
  sowie `C:\Users\andre\Downloads\Projekt_Plan.pdf`.
- Gewächshaus-Projektunterlagen und Prototypcode:
  `C:\Users\andre\OneDrive - hs-augsburg.de (1)\Studium_Systems_Engineering\Semester 5\Projekt I 2\Pflichtenheft Projekt I.docx`
  und `C:\Users\andre\OneDrive\Dokumente\Studium_Systems_Engineering\Semester_5\Projekt\Backup_Raspi\Greenhouse\`.
