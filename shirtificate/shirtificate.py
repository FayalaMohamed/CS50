from fpdf import FPDF

class shirt:
    def __init__(self,name):
        self.name=name
        self.create()

    def create(self):
        pdf=FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        # Set font and add the text at the top of the page
        pdf.set_font("helvetica", "B", size=46)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 50, border=0, align="C", txt="CS50 Shirtificate")
        pdf.ln()

        # Add and center shirt image
        pdf.image(
            "shirtificate.png",
            x=15,
            y=(297 / 4),
            w=180,
            alt_text=f"A Harvard shirt with the words: {self.name} took CS50",
        )

        # Set font and add the text on top of the shirt
        pdf.set_font("helvetica", "B", size=28)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 150, border=0, align="C", txt=f"{self.name} took CS50")
        pdf.output("shirtificate.pdf")




def main():
    pdf=shirt(input("What's your name?"))

if __name__ == "__main__":
    main()