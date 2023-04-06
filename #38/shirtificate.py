import fpdf
from fpdf import FPDF, Image

def create_pdf(users_name):
    pdf = FPDF()
    pdf.add_page()
    img = Image('jharvard.png')
    img.draw(50, 50)

    pdf.set_font("helvetica", "B", 16)
    pdf.cell(40, 10, f"{users_name} took CS50", ln=1, align='C')
    pdf.output("result.pdf", 'F')

def main():
    users_name = input("Name: ")
    create_pdf(users_name)

if __name__ == '__main__':
    main()