import argparse
from io import BytesIO
import re
from pathlib import Path
from typing import Dict, Iterable, List

from PIL import Image as PILImage, ImageOps
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, Frame, Image, KeepTogether, PageTemplate, Paragraph, Spacer, Table, TableStyle

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR
for candidate in [BASE_DIR, *BASE_DIR.parents[:3]]:
    if (candidate / "shared").exists() and (candidate / "shared" / "Bewerbungsbild.jpg").exists():
        PROJECT_ROOT = candidate
        break
    if (candidate / "Bewerbungsbild.jpg").exists():
        PROJECT_ROOT = candidate
        break
PHOTO_PATH = PROJECT_ROOT / "shared" / "Bewerbungsbild.jpg"
if not PHOTO_PATH.exists():
    PHOTO_PATH = PROJECT_ROOT / "Bewerbungsbild.jpg"
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
            "Strukturierte Anlagenanalyse mit Fokus auf technische Integrität und Qualitätsabweichungen.",
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
            "Unterstützung bei 3D-Druck, Prototyping, technischer Evaluierung und Recherche zum Thema Werkerführung mit KI.",
            "Nebentätigkeit mit 8 Stunden pro Woche parallel zum Bachelorstudium in Systems Engineering.",
        ],
    ),
]

EDUCATION = [
    (
        "2022 – heute",
        "Bachelorstudium Systems Engineering",
        "Technische Hochschule Augsburg",
        "Schwerpunkte: Informatik 1–3, industrielle Informationsverarbeitung, Embedded Systems, industrielle Bildverarbeitung, verteilte Systeme, sichere Industriesysteme, Datenkommunikation, Operations Management, digitale Supply Chain, Projektführung und Projektorganisation.",
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
    ("Python & KI", "Python · PyTest · NumPy · Matplotlib · PyTorch · scikit-learn · Feature Engineering · Model Evaluation"),
    ("Daten & KI", "SQL · Datenanalyse · Process Mining · Event Logs · Datenpipelines"),
    ("DevOps", "Git · Bash · VS Code · Jira · Confluence"),
    ("Industrie & Integration", "ERP-Integration · Odoo · Celonis · Automatisierung · technische Systemanalyse"),
    ("Technik", "EPLAN · CAD · 3D-Druck · Dokumentation · Prototyping · technische Analyse"),
    ("Projektmanagement", "Projektführung · Projektorganisation · Projektdesign · GPM-Basiszertifikat"),
    ("Sprachen", "Deutsch – (Muttersprache) <br/>Englisch – B1 (fortgeschritten)"),
]

COMPANY_CONFIGS: Dict[str, Dict[str, object]] = {
    "mt_aerospace": {
        "display_name": "MT Aerospace",
        "title": "Systems Engineer | Industrial AI | Mechatronik",
        "summary": (
            "Systems-Engineering-Student und ausgebildeter Mechatroniker mit praktischer Erfahrung in der "
            "Vorinbetriebnahme, Funktionsprüfung und strukturierten Fehleranalyse industrieller Anlagen. Verbindet "
            "technisches Verständnis für mechanische, elektrische und softwarebezogene Schnittstellen mit Python, "
            "Datenanalyse, Automatisierung und Machine Learning. Besonders interessiert an zuverlässigen, "
            "nachvollziehbaren Lösungen für anspruchsvolle Fertigungs-, Prüf- und Entwicklungsprozesse in der Luft- "
            "und Raumfahrt sowie an innovativen Technologien wie Additive Manufacturing und Leichtbau."
        ),
        "focus": ["Systems Engineering", "Industrielle Automatisierung", "Python & Daten", "Technische Analyse", "Qualität & Integration"],
        "focus_line": "Technische Systemanalyse · Python-Entwicklung · Datenpipelines · Automatisierung · industrielle Integration",
        "project_title": "BACHELORARBEIT",
        "project_detail": "<b>Proximitätssuche von EPLAN-Makros</b><br/>auf Basis des Lambda-Rank-Algorithmus",
        "project_description": "Technische Bereiche: Lambda-Rank, Sentence-Transformer, Embedding-Modelle, Clustering, Triplet-Learning, Datenanalyse, Feature-Engineering, Modellbewertung und Datenaufbereitung.",
    },
    "xitaso": {
        "display_name": "XITASO",
        "title": "Softwareentwickler Python & KI | Data Science | Systems Engineering",
        "summary": (
            "Systems-Engineering-Student und ausgebildeter Mechatroniker mit praktischer Erfahrung in industrieller "
            "Vorinbetriebnahme, Robotik und technischen Schnittstellen. Verbindet Python-Entwicklung, Datenanalyse und "
            "Machine Learning mit fundierten Studienleistungen in Informatik, Embedded Systems, industrieller "
            "Informationsverarbeitung, verteilten Systemen und sicheren Industriesystemen. Arbeitet strukturiert, "
            "lernt schnell und entwickelt technische Lösungen gern gemeinsam im agilen Team."
        ),
        "focus": ["Python & KI", "Datenanalyse", "Softwareentwicklung", "Agile Zusammenarbeit", "Systems Engineering"],
        "focus_line": "Python-Entwicklung · Machine Learning · Datenpipelines · APIs · industrielle Softwarelösungen",
        "project_title": "BACHELORARBEIT",
        "project_detail": "<b>Proximitätssuche von EPLAN-Makros</b><br/>auf Basis des Lambda-Rank-Algorithmus",
        "project_description": "Technische Bereiche: Lambda-Rank, Sentence-Transformer, Embedding-Modelle, Clustering, Triplet-Learning, Datenanalyse, Feature-Engineering, Modellbewertung und Datenaufbereitung.",
    },
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
        "project_title": "BACHELORARBEIT",
        "project_detail": "<b>Proximitätssuche von EPLAN-Makros</b><br/>auf Basis des Lambda-Rank-Algorithmus",
        "project_description": "Technische Bereiche: Lambda-Rank, Sentence-Transformer, Embedding-Modelle, Clustering, Triplet-Learning, Datenanalyse, Feature-Engineering, Modellbewertung und Datenaufbereitung.",
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
styles.add(ParagraphStyle(name="ProjectTitle", fontName="SegoeUISemibold", fontSize=9.2, leading=12, textColor=NAVY, spaceBefore=1.5 * mm, spaceAfter=1.5 * mm))
styles.add(ParagraphStyle(name="Body", fontName="SegoeUI", fontSize=8.7, leading=11.5, textColor=TEXT))
styles.add(ParagraphStyle(name="SmallMuted", fontName="SegoeUI", fontSize=8.3, leading=11, textColor=MUTED))
styles.add(ParagraphStyle(name="ListBullet", fontName="SegoeUI", fontSize=8.3, leading=11, leftIndent=3 * mm, firstLineIndent=-2.5 * mm, textColor=TEXT, spaceAfter=1 * mm))


def P(text, style_name):
    return Paragraph(text, styles[style_name])


def profile_photo():
    photo = ImageOps.exif_transpose(PILImage.open(PHOTO_PATH)).convert("RGB")
    target_ratio = 3 / 4
    width, height = photo.size
    current_ratio = width / height
    if current_ratio > target_ratio:
        crop_width = int(height * target_ratio)
        left = (width - crop_width) // 2
        photo = photo.crop((left, 0, left + crop_width, height))
    elif current_ratio < target_ratio:
        crop_height = int(width / target_ratio)
        top = (height - crop_height) // 2
        photo = photo.crop((0, top, width, top + crop_height))

    image_data = BytesIO()
    photo.save(image_data, format="JPEG", quality=95)
    image_data.seek(0)
    return Image(image_data, width=24 * mm, height=32 * mm)


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
    def __init__(self, filename, sidebars):
        super().__init__(filename, pagesize=A4, leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0)
        main_frame = Frame(MAIN_LEFT, 22 * mm, MAIN_W, PAGE_H - 50 * mm, id="main", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="CV", frames=[main_frame], onPage=lambda c, d: _on_page(c, d, sidebars))])


def _on_page(canvas, doc, sidebars):
    draw_background(canvas, doc)
    sidebar = sidebars.get(doc.page)
    if sidebar is not None:
        sidebar.wrapOn(canvas, SIDEBAR_W, PAGE_H)
        sidebar.drawOn(canvas, 0, PAGE_H - sidebar._height - 7 * mm)


def sidebar_story(profile, skill_start=0, skill_end=None, include_identity=False):
    story = []
    if include_identity:
        focus_text = "<br/>".join(profile["focus"])
        identity = Table([
            [[P(profile["name"], "SideName"), P(profile["title"], "SideTitle")], profile_photo()]
        ], colWidths=[26 * mm, 24 * mm], hAlign="LEFT")
        identity.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]))
        story.extend([
            identity,
            Spacer(1, 5 * mm),
            P("PERSÖNLICHE DATEN", "SideHeading"),
            P(f"<b>Wohnort</b><br/>{profile['location']}", "SideText"),
            P(f"<b>Telefon</b><br/>{profile['phone']}", "SideText"),
            P(f"<b>E-Mail</b><br/>{profile['email']}", "SideText"),
            P(f"<b>LinkedIn</b><br/>{profile['linkedin']}", "SideText"),
            Spacer(1, 5 * mm),
            P("FOKUS", "SideHeading"),
            P(focus_text, "SideText"),
            Spacer(1, 3 * mm),
            P("TECHNISCHE KOMPETENZEN", "SideHeading"),
        ])
    else:
        story.append(P("TECHNISCHE KOMPETENZEN · FORTSETZUNG", "SideHeading"))

    for label, value in SKILLS[skill_start:skill_end]:
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
        story.append(P(f"<b>{title}</b>", "ProjectTitle"))
        story.append(P(detail, "Body"))

    story.extend([
        P(profile["project_title"], "Section"),
        P(profile["project_detail"], "ProjectTitle"),
        P(profile["project_description"], "SmallMuted"),
        Spacer(1, 6 * mm),
    ])
    return story


def build_company_pdf(company_name: str, output_dir: Path | None = None) -> Path:
    profile = build_profile(company_name)
    company_slug = _slugify(company_name)
    output_dir = output_dir or (PROJECT_ROOT / "firmen" / company_slug / "output")
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / profile["output_name"]

    def build_sidebar(story):
        sidebar = Table([[story]], colWidths=[SIDEBAR_W], hAlign="LEFT")
        sidebar.setStyle(TableStyle([
            ("LEFTPADDING", (0, 0), (-1, -1), 8 * mm),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6 * mm),
            ("TOPPADDING", (0, 0), (-1, -1), 14 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8 * mm),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]))
        return sidebar

    sidebars = {
        1: build_sidebar(sidebar_story(profile, skill_end=3, include_identity=True)),
        2: build_sidebar(sidebar_story(profile, skill_start=3)),
    }

    doc = CVDocTemplate(str(output_path), sidebars)
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

