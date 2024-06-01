from fpdf import FPDF

name = input("Name: ")


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 40)
        # Printing title:
        self.cell(0, 80, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")


final = PDF()
final.set_margin(0)
final.add_page()
final.image("shirtificate.png", w=final.epw, y=80)
final.set_font("helvetica", "B", 20)
final.set_text_color(255, 255, 255)
final.cell(0, 150, f"{name} took cs50", align="C")
final.output("shirtificate.pdf")
