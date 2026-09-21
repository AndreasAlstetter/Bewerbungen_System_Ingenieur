import argparse
import re
from pathlib import Path
from typing import Dict, Iterable, List

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, Frame, KeepTogether, PageTemplate, Paragraph, Spacer, Table, TableStyle

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_COMPANY = "Ferchau"

PAGE_W, PAGE_H = A4
SIDEBAR_W = 64 * mm
MAIN_LEFT = SIDEBAR_W + 8 * mm
MAIN_RIGHT = 12 * mm
MAIN_W = PAGE_W - MAIN_LEFT - MAIN_RIGHT

NAVY = colors.HexColor("#10283A")
NAVY_SOFT = colors.HexColor("#183D52")
TEAL = colors.HexColor("#18A5A5")
TEAL_SOFT = colors.HexColor("#E9F5F5")
TEXT = colors.HexColor("#23313B")
MUTED = colors.HexColor("#60717D")
LINE = colors.HexColor("#D7E3E7")
WHITE = colors.white

COMMON_PROFILE = {
    "name": "Andreas Alstetter",
    "location": "Pfarrer-Kempter Straße 4, 89358 Kammeltal",
    "phone": "+49 152 01472197",
    "email": "andreas.alstetter13@gmail.com",
    "linkedin": "linkedin.com/in/andreas-alstetter-2aba562b2",
}

EXPERIENCE = [
    (
        "2022 – heute",
        "Mechatroniker – Vorinbetriebnahme",
        "GROB-WERKE GmbH & Co. KG",
        [
            "Vorinbetriebnahme, Funktionsprüfung und Fehleranalyse mechatronischer Maschinen und Anlagen mit Fokus auf technische Integrität.",
            "Zusammenarbeit mit Konstruktion, Montage, Softwareentwicklung und Fachabteilungen zur Lösung technischer Schnittstellenprobleme und Qualitätsabweichungen.",
            "Internationale Montage- und Inbetriebnahmeeinsätze in Spanien, Mexiko und Indien im interdisziplinären Team unter Zeitdruck.",
            "Technische Dokumentation, Übergabeprozesse und strukturierte Anlagenanalyse für eine nachvollziehbare Betriebsübernahme.",
            "Teilzeittätigkeit mit 21 Stunden pro Woche parallel zum Bachelorstudium in Systems Engineering.",
        ],
    ),
    (
        "2025 – 08/2026",
        "Studentische Hilfskraft",
        "Technologie-Transferzentrum Leipheim",
        [
            "Entwicklung und Erprobung einer Pick-by-Light-Anwendung im logistischen Szenario.",
            "Programmierung und Inbetriebnahme eines AMR- und Robotiksystems im Rahmen einer Lernfabrik für industrielle Digitalisierung und Automatisierung.",
            "Unterstützung bei 3D-Druck, Prototyping, technischer Evaluierung und Recherche zum Thema Werkerführung mit KI",
            "Nebentätigkeit mit 8 Stunden pro Woche parallel zum Bachelorstudium in Systems Engineering.",
        ],
    ),
]

EDUCATION = [
    (
        "2022 – heute",
        "Bachelorstudium Systems Engineering",
        "Technische Hochschule Augsburg",
        "Schwerpunkte: industrielle Informationsverarbeitung, Embedded Systems, industrielle Bildverarbeitung, verteilte Systeme, IT-Security, Datenkommunikation, Operations Management, digitale Supply Chain und Projektführung.",
    ),
    (
        "2021 – 2022",
        "Ausbildung zum Mechatroniker",
        "GROB-WERKE GmbH & Co. KG",
        "Abschluss als Mechatroniker mit Fokus auf elektromechanische Systeme, Inbetriebnahme und Anlagenpraxis im Automobilbereich.",
    ),
    (
        "2018 – 2020",
        "Ausbildung zum Mechatroniker",
        "Klein GmbH, Jettingen-Scheppach",
        "Ausbildungsabschnitt im Bereich Mechatronik mit praktischer Ausbildung an technischen Systemen und Anlagen im Baumaschinen-Sektor.",
    ),
]

PROJECTS = [
    (
        "Odoo-to-Celonis-Datenpipeline",
        "Aufbau einer Prozessdaten-Pipeline aus Odoo-Daten für Process Mining, Event-Log-Erstellung und Wertstromanalyse in Celonis.",
    ),
    (
        "Automatisierte Odoo-Provisionierung",
        "Python-basierte Provisionierung von Produkt-, Stücklisten-, Lager- und Produktionsdaten mit XML-RPC-Integration und Datenvalidierung.",
    ),
    (
        "EPLAN-Makro-Proximitätssuche",
        "Bachelorarbeitsprojekt zur Ähnlichkeitssuche und zum Ranking von EPLAN-Makros auf Basis des Lambda-Rank-Algorithmus und Embedding-Ansätzen.",
    ),
    (
        "Pick-by-Light und Intralogistik",
        "Praxisnahe Digitalisierung manueller Kommissionierungs- und Materialbereitstellungsprozesse mit Fokus auf Effizienz und Fehlerreduktion.",
    ),
]

SKILLS = [
    ("Python & KI", "Python · PyTest · NumPy · Matplotlib · PyTorch  · scikit-learn · Feature Engineering · Model Evaluation"),
    ("Data & AI", "SQL · Datenanalyse · Process Mining · Event Logs · Datenpipelines"),
    ("DevOps", "Git · Bash · VS Code · Jira · Confluence"),
    ("Industrie & Integration", "ERP-Integration · Odoo · Celonis · Automatisierung · technische Systemanalyse"),
    ("Engineering", "EPLAN · CAD · 3D-Druck · Dokumentation · Prototyping · technische Analyse"),
    ("Sprachen", "Deutsch – (Muttersprache) <br/>Englisch – B1 (fortgeschritten)"),
]

COMPANY_CONFIGS: Dict[str, Dict[str, object]] = {
    "ferchau": {
        "display_name": "Ferchau",
        "title": "Softwareentwickler KI & Data Science | Python | Machine Learning",
        "summary": (
            "System-Ingenieur mit technischer Ausbildung im Mechatronikbereich, starkem Fokus auf Python, "
            "Datenanalyse, KI-gestützte Analyseprozesse und industrielle Systemintegration. Erfahrung in der Entwicklung "
            "von Datenpipelines, Anbindung von ERP-/Prozessdaten, Analyse von Datensätzen und Anwendung von Machine-Learning-"
            "Ansätzen im praxisnahen Bereich. Kombiniert technisches Verständnis für industrielle Prozesse mit analytischem "
            "Denken und Datenkompetenz sowie einem starken Interesse an der Entwicklung intelligenter Softwarelösungen."
        ),
        "focus": ["Python & KI", "Machine Learning", "Data Engineering", "APIs", "Industrial AI"],
        "focus_line": "Python-Entwicklung · Machine Learning · Deep Learning · Datenanalysen · Prozessdatenanalyse · industrielle Systemintegration",
        "project_title": "BACHELORARBEIT & ML-PROJEKTARBEIT",
        "project_detail": "<b>Proximitätssuche von EPLAN-Makros</b><br/>auf Basis des Lambda-Rank-Algorithmus",
        "project_description": "Technische Bereiche: Sentence-Transformer, Embedding-Modelle, Clustering, Triplet-Learning, Datenanalyse, Feature-Engineering, Modellbewertung und Datenaufbereitung.",
    },
    "mhp": {
        "display_name": "MHP",
        "title": "AI Engineer | Data Science | Python | Cloud Solutions",
        "summary": (
            "System-Ingenieur mit Fokus auf datengetriebene Lösungen, Prozessautomatisierung und intelligente Analyselösungen. "
            "Verbindet technisches Verständnis für industrielle Prozesse mit KI-Architektur sowie "
            "Praxisorientierung in der Daten- und Systemintegration."
        ),
        "focus": ["Python & KI", "Data Science", "Automation", "Applied AI"],
        "focus_line": "Python-Entwicklung ·  Datenmodelle · Automatisierung",
        "project_title": "AUSGEWÄHLTE PROJEKTE",
        "project_detail": "<b>Odoo-to-Celonis-Datenpipeline</b><br/>Aufbau einer Prozessdaten-Pipeline für Analyse, Visualisierung und datenbasierte Optimierung.",
        "project_description": "Technische Aspekte: Datenmodellierung, Prozessanalyse, Event Logs, ETL-Workflows und modellbasierte Entscheidungsunterstützung.",
    },
    "bmw_group": {
        "display_name": "BMW Group",
        "title": "Machine Learning Engineer | Python | Data & AI Systems",
        "summary": (
            "Motivierter Entwickler mit Interesse an datengetriebenen, skalierbaren AI-Lösungen im Bereich digitaler Mobilität, "
            "Prozessdaten und automatisierter Entscheidungslogik. Bringt technisches Verständnis aus Mechatronik und Datenanalyse "
            "mit und setzt dies praxisnah in intelligenten Software- und Analyseprozessen um."
        ),
        "focus": ["AI Engineering", "Data Platforms", "Python", "Analytics", "System Integration"],
        "focus_line": "Machine Learning · Prozessdatenanalyse · Datenplattformen · API-Integration · KI-gestützte Entscheidungsprozesse",
        "project_title": "AUSGEWÄHLTE PROJEKTE",
        "project_detail": "<b>Automatisierte Odoo-Provisionierung</b><br/>Datenorientierte Provisionierung und Automatisierung des Produkt-, Lager- und Prozessdatenflusses.",
        "project_description": "Technische Schwerpunkte: Datenvalidierung, Automatisierung, Integrationslogik und skalierbare Prozessoptimierung.",
    },
}

styles = getSampleStyleSheet()
pdfmetrics.registerFont(TTFont("SegoeUI", "C:/Windows/Fonts/segoeui.ttf"))
pdfmetrics.registerFont(TTFont("SegoeUISemibold", "C:/Windows/Fonts/seguisb.ttf"))

styles.add(ParagraphStyle(name="SideName", fontName="SegoeUISemibold", fontSize=18, leading=21, textColor=NAVY, alignment=0, spaceAfter=2 * mm))
styles.add(ParagraphStyle(name="SideTitle", fontName="SegoeUISemibold", fontSize=8.4, leading=10.5, textColor=TEAL, alignment=0, spaceAfter=4 * mm))
styles.add(ParagraphStyle(name="SideHeading", fontName="SegoeUISemibold", fontSize=7.2, leading=10, textColor=TEAL, spaceBefore=6 * mm, spaceAfter=2 * mm, letterSpace=1.1))
styles.add(ParagraphStyle(name="SideText", fontName="SegoeUI", fontSize=8.0, leading=10.8, textColor=TEXT, alignment=0))
styles.add(ParagraphStyle(name="Section", fontName="SegoeUISemibold", fontSize=8.8, leading=11, textColor=TEAL, spaceBefore=6 * mm, spaceAfter=4.5 * mm, borderColor=LINE, borderWidth=0.6, borderPadding=2.2 * mm))
styles.add(ParagraphStyle(name="Summary", fontName="SegoeUI", fontSize=10.2, leading=15, textColor=MUTED, spaceAfter=2 * mm))
styles.add(ParagraphStyle(name="Period", fontName="SegoeUISemibold", fontSize=8.1, leading=10.5, textColor=TEAL))
styles.add(ParagraphStyle(name="Role", fontName="SegoeUISemibold", fontSize=10.1, leading=12, textColor=TEXT))
styles.add(ParagraphStyle(name="Company", fontName="SegoeUISemibold", fontSize=8.6, leading=11, textColor=MUTED))
styles.add(ParagraphStyle(name="Body", fontName="SegoeUI", fontSize=8.7, leading=11.5, textColor=TEXT))
styles.add(ParagraphStyle(name="SmallMuted", fontName="SegoeUI", fontSize=8.3, leading=11, textColor=MUTED))
styles.add(ParagraphStyle(name="ListBullet", fontName="SegoeUI", fontSize=8.3, leading=11, leftIndent=3 * mm, firstLineIndent=-2.5 * mm, textColor=TEXT, spaceAfter=1 * mm))


def P(text, style_name):
    return Paragraph(text, styles[style_name])


def _slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def get_company_config(company_name: str) -> Dict[str, object]:
    key = _slugify(company_name)
    if key not in COMPANY_CONFIGS:
        raise ValueError(
            f"Firma '{company_name}' nicht gefunden. Verfügbare Firmen: {', '.join(sorted(COMPANY_CONFIGS.keys()))}"
        )
    config = COMPANY_CONFIGS[key].copy()
    config["slug"] = key
    return config


def build_profile(company_name: str) -> Dict[str, object]:
    config = get_company_config(company_name)
    profile = COMMON_PROFILE.copy()
    profile.update({
        "company": config["display_name"],
        "title": config["title"],
        "summary": config["summary"],
        "focus": config["focus"],
        "focus_line": config["focus_line"],
        "project_title": config["project_title"],
        "project_detail": config["project_detail"],
        "project_description": config["project_description"],
        "output_name": f"lebenslauf_{config['slug']}.pdf",
    })
    return profile


def draw_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(TEAL_SOFT)
    canvas.rect(0, 0, SIDEBAR_W, PAGE_H, stroke=0, fill=1)
    canvas.setFillColor(WHITE)
    canvas.rect(SIDEBAR_W, 0, PAGE_W - SIDEBAR_W, PAGE_H, stroke=0, fill=1)
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 7 * mm, PAGE_W, 7 * mm, stroke=0, fill=1)

    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.45)
    for x in range(12, 101, 9):
        canvas.line(PAGE_W - 39 * mm + x * mm, PAGE_H - 21 * mm, PAGE_W - 39 * mm + x * mm, PAGE_H - 7 * mm)
    for y in range(1, 3):
        canvas.line(PAGE_W - 39 * mm, PAGE_H - (7 + y * 4) * mm, PAGE_W - 3 * mm, PAGE_H - (7 + y * 4) * mm)
    canvas.setFillColor(TEAL)
    canvas.circle(PAGE_W - 15 * mm, PAGE_H - 14 * mm, 1.8 * mm, fill=1, stroke=0)

    canvas.setStrokeColor(TEAL)
    canvas.setLineWidth(1.2)
    canvas.line(18 * mm, 14 * mm, 40 * mm, 14 * mm)
    canvas.setFont("SegoeUI", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(PAGE_W - 18 * mm, 11.2 * mm, f"{doc.page:02d}")
    canvas.restoreState()


class CVDocTemplate(BaseDocTemplate):
    def __init__(self, filename, sidebar):
        super().__init__(filename, pagesize=A4, leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0)
        main_frame = Frame(MAIN_LEFT, 22 * mm, MAIN_W, PAGE_H - 50 * mm, id="main", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="CV", frames=[main_frame], onPage=lambda c, d: _on_page(c, d, sidebar))])


def _on_page(canvas, doc, sidebar):
    draw_background(canvas, doc)
    sidebar.wrapOn(canvas, SIDEBAR_W, PAGE_H)
    sidebar.drawOn(canvas, 0, PAGE_H - sidebar._height - 7 * mm)


def sidebar_story(profile):
    focus_text = "<br/>".join(profile["focus"])
    story = [
        P(profile["name"], "SideName"),
        P(profile["title"], "SideTitle"),
        Spacer(1, 5 * mm),
        P("PERSÖNLICHE DATEN", "SideHeading"),
        P(f"<b>Wohnort</b><br/>{profile['location']}", "SideText"),
        P(f"<b>Telefon</b><br/>{profile['phone']}", "SideText"),
        P(f"<b>E-Mail</b><br/>{profile['email']}", "SideText"),
        P(f"<b>LinkedIn</b><br/>{profile['linkedin']}", "SideText"),
        Spacer(1, 5 * mm),
        P("FOCUS", "SideHeading"),
        P(focus_text, "SideText"),
        Spacer(1, 3 * mm),
        P("TECHNISCHE KOMPETENZEN", "SideHeading"),
    ]
    for label, value in SKILLS:
        story.append(P(label, "SideHeading"))
        story.append(P(value, "SideText"))

    return story


def experience_entry(period, role, company, items):
    left = P(period, "Period")
    right = [P(role, "Role"), P(company, "Company"), Spacer(1, 1.5 * mm)]
    right.extend(P(f"• {item}", "ListBullet") for item in items)
    table = Table([[left, right]], colWidths=[30 * mm, MAIN_W - 34 * mm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
    ]))
    return KeepTogether(table)


def education_entry(period, degree, institution, details):
    left = P(period, "Period")
    right = [P(degree, "Role"), P(institution, "Company"), P(details, "SmallMuted")]
    table = Table([[left, right]], colWidths=[30 * mm, MAIN_W - 34 * mm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
    ]))
    return KeepTogether(table)


def build_story(profile):
    story = [
        P("BERUFSFOKUS", "Section"),
        P(profile["summary"], "Summary"),
        P(profile["focus_line"], "Body"),
        P("BERUFSERFAHRUNG", "Section"),
    ]

    for period, role, company, items in EXPERIENCE:
        story.append(experience_entry(period, role, company, items))

    story.append(P("AUSBILDUNG & STUDIUM", "Section"))
    for period, degree, institution, details in EDUCATION:
        story.append(education_entry(period, degree, institution, details))

    story.append(P("AUSGEWÄHLTE PROJEKTE", "Section"))
    for title, detail in PROJECTS:
        story.append(P(f"<b>{title}</b><br/>{detail}", "Body"))

    story.extend([
        P(profile["project_title"], "Section"),
        P(profile["project_detail"], "Body"),
        P(profile["project_description"], "SmallMuted"),
        Spacer(1, 6 * mm),
        P("Stand: September 2026 · Referenzen und Projektdetails auf Anfrage", "SmallMuted"),
    ])
    return story


def build_company_pdf(company_name: str, output_dir: Path | None = None) -> Path:
    profile = build_profile(company_name)
    output_dir = output_dir or BASE_DIR
    output_path = output_dir / profile["output_name"]

    sidebar = Table([[sidebar_story(profile)]], colWidths=[SIDEBAR_W], hAlign="LEFT")
    sidebar.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 8 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 14 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8 * mm),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))

    doc = CVDocTemplate(str(output_path), sidebar)
    doc.build(build_story(profile))

    if not output_path.exists() or output_path.stat().st_size == 0:
        raise RuntimeError(f"PDF für {profile['company']} wurde nicht korrekt erzeugt.")

    print(f"Erstellt: {output_path} ({output_path.stat().st_size} Bytes)")
    return output_path


def parse_args():
    parser = argparse.ArgumentParser(description="Erstelle firmenspezifische Lebensläufe als PDF.")
    parser.add_argument("--company", "--firmen", action="append", dest="companies", default=[], help="Name der Firma, z. B. Ferchau, MHP oder BMW Group")
    parser.add_argument("--all", action="store_true", help="Erstellt alle vordefinierten Lebensläufe.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.all:
        companies = list(COMPANY_CONFIGS.keys())
    elif args.companies:
        companies = args.companies
    else:
        companies = [DEFAULT_COMPANY]

    for company_name in companies:
        build_company_pdf(company_name)

