# Bewerbungsbereich

Dieser Bereich enthält die aktiven, firmenspezifischen Bewerbungsunterlagen,
gemeinsam genutzte Ressourcen, Profilgrundlagen und deren Generatoren.

## Struktur

```text
01_Bewerbung/
├── 01_Firmen/<firma>/
│   ├── input/                 # bearbeitbare, firmenspezifische Quellen
│   ├── output/                # erzeugte Dokumente
│   ├── Bewerbungsanhänge/     # optionale Versandkopien
│   └── output/Bewerbung/      # optional vollständiges Bewerbungspaket
├── 02_Generatoren/
│   ├── 01_Lebenslauf/
│   └── 02_Anschreiben_PDF/
├── 03_Gemeinsame_Ressourcen/
├── 04_Profil/
└── 99_Archiv/                 # historische Fassungen, nicht aktive Quellen
```

## Verwendung

### Lebenslauf

```powershell
python .\01_Bewerbung\02_Generatoren\01_Lebenslauf\lebenslauf.py --company Ferchau
```

### Anschreiben als PDF

```powershell
python .\01_Bewerbung\02_Generatoren\02_Anschreiben_PDF\erzeuge_motivationsschreiben_pdf.py `
  --source .\01_Bewerbung\01_Firmen\smai_solutions\input\motivationsschreiben_smai_solutions.md `
  --output .\01_Bewerbung\01_Firmen\smai_solutions\output\motivationsschreiben_smai_solutions.pdf
```

## Pflege- und Duplikatregeln

- Generische Generatoren und gemeinsam genutzte Ressourcen liegen getrennt von
  Firmenquellen und Ergebnissen.
- Jede Firma behält einen eigenständigen Bereich. `input/` enthält die
  bearbeitbare Quelle; `output/` enthält daraus erstellte Dateien.
- Versandfertige Kopien von Lebenslauf und Zeugnissen in Bewerbungspaketen sind
  absichtlich redundant und müssen eigenständig verwendbar bleiben.
- ZIP-Dateien können gleiche Anlagen, aber unterschiedliche Anschreiben
  enthalten; sie werden daher nicht allein wegen gleicher Anlagen entfernt.
- `99_Archiv/` enthält historische Fassungen und ist keine Quelle für aktive
  Bewerbungen.

Das quellenbasierte Kompetenzprofil und Hinweise zur Beleglage stehen in
[04_Profil/Profil_und_Kompetenzen.md](./04_Profil/Profil_und_Kompetenzen.md).
