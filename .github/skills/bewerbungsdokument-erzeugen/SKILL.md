---
name: bewerbungsdokument-erzeugen
description: "Use when explicitly asked to generate a company-specific CV PDF, cover-letter PDF, or application package using the repository generators."
argument-hint: "Firma, Quelle, gewünschte Dokumente und Zielpfad angeben"
---

# Bewerbungsdokument erzeugen

Erzeuge nur ausdrücklich angeforderte Dateien. Ausgaben gehören in den
`output/`-Ordner derselben Firma.

## Vor dem Lauf

1. Kläre Firmenordner, Quelldatei, Generator, Dokumenttyp und Zielpfad.
2. Prüfe Quelle, Generator und notwendige gemeinsame Ressourcen.
3. Prüfe, ob die Zieldatei bereits existiert. Überschreibe sie nicht; frage
   nach Freigabe oder neuem Zielpfad.
4. Verwende keine als ungeprüft oder veraltet erkannten Quelle ohne Hinweis.

## Generatoren

- Lebenslauf: `01_Bewerbung/02_Generatoren/01_Lebenslauf/lebenslauf.py
  --company <Firmenname>`. Standardmäßig entsteht die PDF im
  `output/`-Ordner der passenden Firma.
- Anschreiben: `01_Bewerbung/02_Generatoren/02_Anschreiben_PDF/erzeuge_motivationsschreiben_pdf.py
  --source <Eingabe-Markdown> --output <Ziel-PDF>`.

Auf Windows PowerShell können Argumente wie folgt über mehrere Zeilen
fortgesetzt werden:

```powershell
python .\01_Bewerbung\02_Generatoren\02_Anschreiben_PDF\erzeuge_motivationsschreiben_pdf.py `
  --source .\01_Bewerbung\01_Firmen\<firma>\input\<quelle>.md `
  --output .\01_Bewerbung\01_Firmen\<firma>\output\<ausgabe>.pdf
```

## Nach dem Lauf

1. Prüfe Prozessabschluss und Fehlerausgabe.
2. Prüfe Existenz und plausible Dateigröße.
3. Öffne/validiere das PDF, prüfe Seitenzahl, Umbrüche, Sonderzeichen,
   Kontaktdaten und Übereinstimmung zur Quelle.
4. Nenne genau den Ausgabepfad und verbleibende Einschränkungen.

Keine Datei versenden. Erzeugte Dokumente bleiben bis zur ausdrücklichen
Nutzerprüfung Entwürfe.
