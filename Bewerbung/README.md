# Bewerbungsprojekt – Struktur

Dieses Projekt ist nach Firmen getrennt und zentralisiert die Generatoren.

## Ordnerstruktur

Bewerbung/
├── README.md
├── shared/
│   └── Bewerbungsbild.jpg
├── code/
│   ├── lebenslauf/
│   │   └── lebenslauf.py
│   └── motivationsschreiben/
│       └── erzeuge_motivationsschreiben_pdf.py
├── firmen/
│   ├── ferchau/
│   │   ├── input/
│   │   └── output/
│   ├── hensoldt/
│   │   ├── input/
│   │   └── output/
│   ├── mt_aerospace/
│   │   ├── input/
│   │   └── output/
│   ├── smai_solutions/
│   │   ├── input/
│   │   └── output/
│   └── xitaso/
│       ├── input/
│       └── output/
└── archive/
    └── legacy/
        ├── lebenslauf/
        └── motivationsschreiben/

## Verwendung

### Lebenslauf
python .\Bewerbung\code\lebenslauf\lebenslauf.py --company Ferchau

### Motivationsschreiben
python .\Bewerbung\code\motivationsschreiben\erzeuge_motivationsschreiben_pdf.py --source .\Bewerbung\firmen\smai_solutions\input\motivationsschreiben_smai_solutions.md --output .\Bewerbung\firmen\smai_solutions\output\motivationsschreiben_smai_solutions.pdf

## Prinzip

- Code zentral in code/
- firmenspezifische Vorlagen in firmen/<firma>/input/
- firmenspezifische Ergebnisse in firmen/<firma>/output/
- gemeinsame Assets in shared/
- veraltete Kopien im Archiv unter archive/legacy/
