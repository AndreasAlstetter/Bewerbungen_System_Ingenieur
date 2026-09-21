from pathlib import Path
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
SOURCE = BASE_DIR / "motivationsschreiben_ferchau_optimiert.md"
OUTPUT = BASE_DIR / "motivationsschreiben_ferchau.pdf"

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


def build_pdf():
    register_fonts()
    blocks = parse_source()
    document = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=23 * mm,
        bottomMargin=22 * mm,
        title="Motivationsschreiben Andreas Alstetter - FERCHAU",
        author="Andreas Alstetter",
    )
    frame = Frame(document.leftMargin, document.bottomMargin, document.width, document.height, id="letter")
    document.addPageTemplates([PageTemplate(id="modern", frames=frame, onPage=draw_background)])

    contact_style = ParagraphStyle(
        "contact", fontName="SegoeUI", fontSize=9.2, leading=12.2, textColor=MUTED, spaceAfter=0
    )
    title_style = ParagraphStyle(
        "title", fontName="SegoeUISemibold", fontSize=17.5, leading=21, textColor=NAVY, spaceBefore=5 * mm, spaceAfter=1.5 * mm
    )
    reference_style = ParagraphStyle(
        "reference", fontName="SegoeUISemibold", fontSize=9.3, leading=12, textColor=TEAL, spaceAfter=6 * mm
    )
    body_style = ParagraphStyle(
        "body", fontName="SegoeUI", fontSize=9.7, leading=14.2, textColor=TEXT, alignment=TA_LEFT, spaceAfter=4.3 * mm
    )
    date_style = ParagraphStyle(
        "date", fontName="SegoeUI", fontSize=9.2, leading=12, textColor=MUTED, spaceBefore=5 * mm, spaceAfter=6 * mm
    )
    salutation_style = ParagraphStyle(
        "salutation", fontName="SegoeUISemibold", fontSize=9.7, leading=14.2, textColor=TEXT, spaceAfter=4.3 * mm
    )
    closing_style = ParagraphStyle(
        "closing", fontName="SegoeUI", fontSize=9.7, leading=14.2, textColor=TEXT, spaceAfter=0
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
            story.append(Spacer(1, 7 * mm))
        elif index == len(blocks) - 1:
            story.append(Paragraph(escape(block[0]), closing_style))
        else:
            style = salutation_style if index == 4 else body_style
            story.append(Paragraph(escape(" ".join(block)), style))

    document.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    build_pdf()