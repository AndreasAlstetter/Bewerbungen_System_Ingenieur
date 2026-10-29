---
name: profil-belegabgleich
description: "Use when checking application claims about education, work history, skills, projects, dates, or results against source documents; identify evidence, contradictions, and unverified claims."
argument-hint: "Aussage oder Text und optional den Bewerbungskontext angeben"
---

# Profil-Belegabgleich

Prüfe konkrete Bewerbungsbehauptungen gegen die im Repository vorhandenen
Nachweise. Der Skill ist lesend und ersetzt keine Nutzerbestätigung.

## Ablauf

1. Zerlege den Text in einzeln prüfbare Aussagen.
2. Prüfe zuerst `02_Nachweise/` und `03_Studium/`, danach
   `01_Bewerbung/04_Profil/Profil_und_Kompetenzen.md`.
3. Verwende aktive Bewerbungstexte und `01_Bewerbung/99_Archiv/` nicht als
   unabhängigen Tatsachenbeleg.
4. Ordne jede Aussage ein:
   - **Belegt:** direkt durch einen Primärbeleg gestützt.
   - **Abgeleitet:** schlüssige Zusammenfassung mehrerer Belege; Herleitung
     nennen.
   - **Offen:** unbelegt, mehrdeutig, widersprüchlich oder bestätigungsbedürftig.
5. Gib relativen Belegpfad und, wenn auffindbar, Abschnitt/Seite an.
6. Empfiehl bei offenen Punkten eine präzise Rückfrage. Nicht raten oder
   stillschweigend aktualisieren.

## Ausgabe

| Aussage | Status | Beleg/Datei | Einschränkung oder Rückfrage |
|---|---|---|---|

Schließe mit einer Liste der verwendbaren Aussagen und der vor Verwendung zu
klärenden Punkte.
