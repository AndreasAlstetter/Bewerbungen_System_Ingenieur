from pathlib import Path
import argparse
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_SOURCE = BASE_DIR / "motivationsschreiben_ferchau_optimiert.md"
DEFAULT_OUTPUT = BASE_DIR / "motivationsschreiben_ferchau.pdf"

PAGE_WIDTH, PAGE_HEIGHT = A4
NAVY = colors.HexColor("#10283A")
TEAL = colors.HexColor("#18A5A5")
PALE_TEAL = colors.HexColor("#E9F5F5")
TEXT = colors.HexColor("#23313B")
MUTED = colors.HexColor("#60717D")
LIGHT_LINE = colors.HexColor("#D7E3E7")


def register_fonts():
    font_dir = Path("C:/Windows/Fonts")
    pdfmetrics.registerFont(TTFont("SegoeUI", str(font_dir / "segoeui.ttf")))
    pdfmetrics.registerFont(TTFont("SegoeUISemibold", str(font_dir / "seguisb.ttf")))


def parse_source():
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    blocks = []
    current = []

    for line in lines:
        if not line.strip():
            if current:
                blocks.append(current)
                current = []
            continue
        current.append(line)
    if current:
        blocks.append(current)
    return blocks


def plain_heading(line):
    return line.removeprefix("## ").removeprefix("### ")


def draw_background(canvas, document):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_HEIGHT - 7 * mm, PAGE_WIDTH, 7 * mm, fill=1, stroke=0)

    canvas.setStrokeColor(LIGHT_LINE)
    canvas.setLineWidth(0.45)
    for x in range(12, 101, 9):
        canvas.line(PAGE_WIDTH - 39 * mm + x * mm, PAGE_HEIGHT - 21 * mm, PAGE_WIDTH - 39 * mm + x * mm, PAGE_HEIGHT - 7 * mm)
    for y in range(1, 3):
        canvas.line(PAGE_WIDTH - 39 * mm, PAGE_HEIGHT - (7 + y * 4) * mm, PAGE_WIDTH - 3 * mm, PAGE_HEIGHT - (7 + y * 4) * mm)

    canvas.setFillColor(TEAL)
    canvas.circle(PAGE_WIDTH - 15 * mm, PAGE_HEIGHT - 14 * mm, 1.8 * mm, fill=1, stroke=0)
    canvas.setStrokeColor(TEAL)
    canvas.setLineWidth(1.2)
    canvas.line(18 * mm, 14 * mm, 40 * mm, 14 * mm)
    canvas.setFont("SegoeUI", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(PAGE_WIDTH - 18 * mm, 11.2 * mm, f"{document.page:02d}")
    canvas.restoreState()


def build_pdf(source=DEFAULT_SOURCE, output=DEFAULT_OUTPUT):
    register_fonts()
    global SOURCE, OUTPUT
    SOURCE = Path(source)
    OUTPUT = Path(output)
    blocks = parse_source()
    mt_compact = "mt_aerospace" in OUTPUT.stem.lower()
    compact = mt_compact or "xitaso" in OUTPUT.stem.lower()
    document = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=16 * mm if mt_compact else 20 * mm,
        rightMargin=16 * mm if mt_compact else 20 * mm,
        topMargin=17 * mm if mt_compact else (20 * mm if compact else 23 * mm),
        bottomMargin=16 * mm if mt_compact else (19 * mm if compact else 22 * mm),
        title=f"Motivationsschreiben Andreas Alstetter - {OUTPUT.stem}",
        author="Andreas Alstetter",
    )
    frame = Frame(document.leftMargin, document.bottomMargin, document.width, document.height, id="letter")
    document.addPageTemplates([PageTemplate(id="modern", frames=frame, onPage=draw_background)])

    contact_style = ParagraphStyle(
        "contact", fontName="SegoeUI", fontSize=9.2, leading=12.2, textColor=MUTED, spaceAfter=0
    )
    title_style = ParagraphStyle(
        "title", fontName="SegoeUISemibold", fontSize=14.5 if mt_compact else (15.8 if compact else 17.5),
        leading=16.8 if mt_compact else (18.5 if compact else 21), textColor=NAVY,
        spaceBefore=3 * mm if mt_compact else (4 * mm if compact else 5 * mm), spaceAfter=1 * mm
    )
    reference_style = ParagraphStyle(
        "reference", fontName="SegoeUISemibold", fontSize=8.2 if mt_compact else (8.8 if compact else 9.3),
        leading=10 if mt_compact else (11 if compact else 12), textColor=TEAL,
        spaceAfter=3 * mm if mt_compact else (4 * mm if compact else 6 * mm)
    )
    body_style = ParagraphStyle(
        "body", fontName="SegoeUI", fontSize=8.5 if mt_compact else (9.2 if compact else 9.7),
        leading=10.8 if mt_compact else (12.7 if compact else 14.2), textColor=TEXT, alignment=TA_LEFT,
        spaceAfter=2.2 * mm if mt_compact else (3.2 * mm if compact else 4.3 * mm)
    )
    date_style = ParagraphStyle(
        "date", fontName="SegoeUI", fontSize=8.2 if mt_compact else (8.8 if compact else 9.2),
        leading=10 if mt_compact else (11 if compact else 12), textColor=MUTED,
        spaceBefore=3 * mm if mt_compact else (4 * mm if compact else 5 * mm), spaceAfter=3 * mm if mt_compact else (4 * mm if compact else 6 * mm)
    )
    salutation_style = ParagraphStyle(
        "salutation", fontName="SegoeUISemibold", fontSize=8.5 if mt_compact else (9.2 if compact else 9.7),
        leading=10.8 if mt_compact else (12.7 if compact else 14.2), textColor=TEXT,
        spaceAfter=2.2 * mm if mt_compact else (3.2 * mm if compact else 4.3 * mm)
    )
    closing_style = ParagraphStyle(
        "closing", fontName="SegoeUI", fontSize=8.5 if mt_compact else (9.2 if compact else 9.7),
        leading=10.8 if mt_compact else (12.7 if compact else 14.2), textColor=TEXT, spaceAfter=0
    )

    story = []
    for index, block in enumerate(blocks):
        if index == 0:
            story.extend(Paragraph(escape(line), contact_style) for line in block)
        elif index == 1:
            story.extend(Paragraph(escape(line), contact_style) for line in block)
        elif index == 2:
            story.append(Paragraph(escape(block[0]), date_style))
        elif index == 3:
            story.append(Paragraph(escape(plain_heading(block[0])), title_style))
            story.append(Paragraph(escape(plain_heading(block[1])), reference_style))
        elif index == len(blocks) - 2:
            story.append(Paragraph(escape(block[0]), closing_style))
            story.append(Spacer(1, 3 * mm if mt_compact else (5 * mm if compact else 7 * mm)))
        elif index == len(blocks) - 1:
            story.append(Paragraph(escape(block[0]), closing_style))
        else:
            style = salutation_style if index == 4 else body_style
            story.append(Paragraph(escape(" ".join(block)), style))

    document.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Erzeugt ein Motivationsschreiben als PDF.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="Markdown-Datei als Vorlage")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Zielpfad der PDF")
    args = parser.parse_args()
    build_pdf(args.source, args.output)