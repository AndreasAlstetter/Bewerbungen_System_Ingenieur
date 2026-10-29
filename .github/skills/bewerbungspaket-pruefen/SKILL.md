---
name: bewerbungspaket-pruefen
description: "Use when checking a company application before user review or sending: validate requested letters, CV, certificates, package completeness, consistency, filenames, and PDFs without sending anything."
argument-hint: "Firmenordner und gewünschte Stellenanzeige oder Paketinhalt angeben"
---

# Bewerbungspaket prüfen

Prüfe ein angegebenes Paket vollständig gegen den Auftrag. Diese Prüfung
versendet nichts und ersetzt nicht die Freigabe durch den Nutzer.

## Ablauf

1. Kläre Firmenordner, Zielstelle und verlangte Bestandteile.
2. Prüfe `input/`, `output/` und gegebenenfalls firmeneigene Anlagenkopien.
   Zentrale Nachweise liegen in `02_Nachweise/`; Versandkopien können bewusst
   abweichen und sind nicht automatisch redundant.
3. Prüfe Namen, Firma, Rolle, Datumsangaben und persönliche Angaben auf
   Konsistenz zwischen Anschreiben, Lebenslauf und Paket.
4. Prüfe PDFs auf Öffnbarkeit, Seitenzahl, abgeschnittene Inhalte, Sonderzeichen
   und plausibles Layout. Prüfe ZIP-Inhalte, falls ein Paket eine ZIP-Datei
   enthält.
5. Gleiche behauptete Qualifikationen mit `profil-belegabgleich` ab.
6. Melde fehlende, unerwartete, doppelte oder widersprüchliche Dateien. Nichts
   ergänzen, entfernen oder überschreiben, sofern dies nicht separat beauftragt
   wurde.

## Ausgabe

- **Bestanden:** geprüfter Punkt und betroffene Dateien.
- **Fehler:** Abweichung, Pfad und notwendige Korrektur.
- **Offen:** Punkt, der menschliche Bestätigung benötigt.

Beende mit einer klaren Aussage, ob das Paket zur Nutzerprüfung bereit ist.
Nenne es nicht automatisch versandfertig und führe keinen Versand aus.
