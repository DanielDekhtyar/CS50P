# Learning Python with CS50
# CS50 Shirtificate
# https://cs50.harvard.edu/python/2022/psets/8/shirtificate/


from fpdf import FPDF
from fpdf.enums import XPos, YPos


class ShirtificatePDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 35)
        # Move to the center of the page
        self.set_y(10)  # Move down by 10 units
        self.cell(0, 0, "CS50 Shirtificate", align="C")
        self.ln(10)

    def add_shirt_image(self):
        # Calculate the X-axis position to center the image
        image_width = 210
        x_position = (self.w - image_width) / 2
        # Set position to center the image
        self.set_x(x_position)
        # Add the shirt's image
        self.image(
            r"C:\Programming\VS Code\CS50P\Problem Set 8 - Object-Oriented Programming\shirtificate.png",
            x_position,
            self.get_y(),
            image_width,
        )
        # Move down after adding the image
        self.ln(50)

    def add_user_name(self, name):
        # Set font for the user's name
        self.set_font("helvetica", "B", 20)
        self.set_text_color(255, 255, 255)
        # Move to the center of the page
        self.ln(10)
        self.cell(0, 10, f"{name} took CS50", align="C")


pdf = ShirtificatePDF(format="A4", orientation="P")
pdf.add_page()
pdf.add_shirt_image()
pdf.add_user_name(input("Name: "))
pdf.output("shirtificate.pdf")
