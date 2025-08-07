from reportlab.lib.pagesizes import A4  
from reportlab.pdfgen import canvas  
from reportlab.lib.colors import black, red  
import random  

def random_case(s):  
    return ''.join(random.choice([c.upper(), c.lower()]) for c in s)  

def generate_poster():  
    c = canvas.Canvas("NOT_YET_POSTER.pdf", pagesize=A4)  
    width, height = A4  
    main_text = "NOT YET"  
    c.setFont("Impact", 72)  
    c.setFillColor(black)  
    c.drawCentredString(width/2, height/2, main_text) 

    fonts = ["Times-Roman", "Courier", "Helvetica-Oblique"]  
    for i in range(200):  
        x = width/2 + random.randint(-300, 300)  
        y = height/2 + random.randint(-400, 400)  
        size = random.randint(8, 20)  
        angle = random.randint(-30, 30)  
        color = red if random.random() < 0.05 else black  
        c.setFont(random.choice(fonts), size)  
        c.setFillColor(color)  
        c.rotate(angle)  
        c.drawString(x, y, random_case("not yet"))  
        c.rotate(-angle)  
    c.save()  

generate_poster()  