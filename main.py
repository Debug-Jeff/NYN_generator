from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, red
import random, string

def random_case(s):
    return ''.join(random.choice([c.upper(), c.lower()]) for c in s)

def generate_not_yet_pdf():
    c = canvas.Canvas("NOT_YET_NUCLEAR.pdf", pagesize=A4)
    width, height = A4
    words = ["NOT YET", "not yet", "nOt YeT", "NOt YEt", "NOT yet"]
    fonts = ["Helvetica", "Courier", "Times-Roman", "Helvetica-BoldOblique", "ZapfDingbats"]
    
    for _ in range(1000): 
        x, y = random.randint(0, int(width)), random.randint(0, int(height))
        size = random.randint(6, 72)
        angle = random.randint(0, 359)
        font = random.choice(fonts)
        opacity = random.uniform(0.2, 1.0)
        color = red if random.random() < 0.05 else black
        
        c.setFont(font, size)
        c.setFillColor(color)
        c.setFillAlpha(opacity)
        c.rotate(angle)
        c.drawString(x, y, random_case(random.choice(words)))
        c.rotate(-angle)
    
    c.save()

generate_not_yet_pdf()