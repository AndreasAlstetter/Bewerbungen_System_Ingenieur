# Bewerbungen – Projektübersicht

Dieses Repository enthält Bewerbungsunterlagen, Nachweise, Studienarbeiten,
Recherchematerial und Dokumentgeneratoren. Die nummerierten Hauptbereiche
halten diese Arbeitskontexte voneinander getrennt.

## Struktur

```text
01_Bewerbung/
├── 01_Firmen/<firma>/{input,output}/
├── 02_Generatoren/
│   ├── 01_Lebenslauf/
│   └── 02_Anschreiben_PDF/
├── 03_Gemeinsame_Ressourcen/
├── 04_Profil/
└── 99_Archiv/
02_Nachweise/
└── 01_Bewerbungsanhänge/
03_Studium/
└── 01_Arbeiten/
04_Recherche/
05_Agenten_und_Skills/
```

## Bereiche und Zuständigkeiten

| Modul | Inhalt und Zweck |
|---|---|
| `01_Bewerbung/01_Firmen/` | Aktive, firmenspezifische Quellen und erzeugte Bewerbungen. Firmennamen bleiben unverändert; Versandpakete können eigene Anlagenkopien enthalten. |
| `01_Bewerbung/02_Generatoren/` | Skripte für Lebensläufe und PDF-Anschreiben. |
| `01_Bewerbung/03_Gemeinsame_Ressourcen/` | Ressourcen, die mehrere Bewerbungen verwenden. |
| `01_Bewerbung/04_Profil/` | Belegte Profilinformationen und Kompetenzgrundlagen. |
| `01_Bewerbung/99_Archiv/` | Historische Unterlagen; nicht als aktive Quelle verwenden. |
| `02_Nachweise/01_Bewerbungsanhänge/` | Zentral bereitgehaltene Nachweise und Bewerbungsanhänge. |
| `03_Studium/01_Arbeiten/` | Abschluss- und sonstige Studienarbeiten. |
| `04_Recherche/` | Positionierungs- und Recherchematerial. |
| `05_Agenten_und_Skills/` | Konzept für getrennte Agentenrollen und wiederverwendbare Skills. |

## Agenten und Skills

Workspace-Regeln, fünf spezialisierte Agenten und fünf wiederverwendbare Skills
sind unter `.github/` eingerichtet:

- `.github/copilot-instructions.md` enthält die workspaceweiten Quellen-,
  Datenschutz- und Schreibregeln.
- `.github/agents/` enthält Koordination, Profilprüfung, Stellenrecherche,
  Redaktion und Dokumentprüfung.
- `.github/skills/` enthält passende Abläufe für Belegabgleich,
  Stellenprofilanalyse, Textentwurf, Dokumenterzeugung und Paketprüfung.

Die detaillierte Nutzung, Generatoraufrufe und Regeln für firmenspezifische
Pakete stehen in [01_Bewerbung/README.md](./01_Bewerbung/README.md).
Das [Agenten- und Skill-Konzept](./05_Agenten_und_Skills/KONZEPT.md) beschreibt
Rollen, Grenzen, Abläufe und Abnahmekriterien.
