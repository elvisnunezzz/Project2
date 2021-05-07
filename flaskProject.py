#Create a pdf file with a logo and footer
#Check the directory and open the pdf file called professor.pdf

from fpdf import FPDF

class pdf_document(FPDF):
    def header(self):

        self.image('professor.png', 11, 8, 33)
        # Times bold 10
        self.set_font('Times', 'B', 10)
        # Adjust the size
        self.cell(70)
        # Title
        self.cell(50, 11, 'Python Programming Class', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):

        self.set_y(-15)
        #Set font to times 8
        self.set_font('Times', 'I', 8)

        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

p = pdf_document()

p.alias_nb_pages()
p.add_page()
p.set_font('Times', '', 12)
for i in range(1, 30):
    p.cell(0, 10, 'The best Python Professor ' + str(i), 0, 1)
p.output('professor.pdf', 'F')