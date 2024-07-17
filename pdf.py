from fpdf import FPDF

# Classe PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        #for col_name in df.columns:
        #    self.cell(19, 10, col_name, 1, 0, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')



class BuildPDF:
    def __init__(self, filename):
        self.filename=filename
        # Créer un PDF
        self.pdf = PDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        # Définir la police
        self.pdf.set_font('Arial', '', 10)


    def add_double_stars_page(self, wds, name, ref, ad, dec, ref_g, m1, m2, parallax, proper_mvt, rad_velocity, dist):
        self.pdf.add_page()
        self.pdf.cell(19, 10, name, 0, 0, 'C')
        self.pdf.cell(30, 10, ref, 0, 0, 'C')
        self.pdf.ln(5)
        self.pdf.cell(19, 10, ad, 0, 0, 'C')
        self.pdf.cell(19, 10, dec, 0, 0, 'C')
    
        self.pdf.ln(10)
        self.pdf.cell(50, 10, ref_g, 0, 0, 'C')
        self.pdf.cell(19, 10, m1, 0, 0, 'C')
        self.pdf.cell(19, 10, m2, 0, 0, 'C')
        
        self.pdf.ln(10)
        self.pdf.cell(19, 10, parallax, 0, 0, 'C')
        self.pdf.cell(19, 10, proper_mvt, 0, 0, 'C')
        self.pdf.cell(19, 10, rad_velocity, 0, 0, 'C')
        self.pdf.cell(19, 10, dist, 0, 0, 'C')

        self.pdf.ln(20)
        self.pdf.cell(19, 10, "Epoque", 0, 0, 'C')
        self.pdf.cell(19, 10, "theta", 0, 0, 'C')
        self.pdf.cell(19, 10, "rho", 0, 0, 'C')
        self.pdf.cell(19, 10, "M1", 0, 0, 'C')
        self.pdf.cell(19, 10, "M2", 0, 0, 'C')
        self.pdf.cell(19, 10, "N", 0, 0, 'C')
        self.pdf.cell(19, 10, "Code", 0, 0, 'C')
        self.pdf.cell(19, 10, "Pu", 0, 0, 'C')
        
        self.pdf.ln(5)
        self.pdf.cell(0, 5, "--------------------------------------------------------------------------------------------------------------------------------", 0, 0,'L') 
        self.pdf.ln(5)
        for index, row in wds[name].iterrows():
            date = str(row['date'])
            theta = str(row['theta'])
            rho = str(row['rho'])
            m1 = str(row['mag1'])
            m2 = str(row['mag2'])
            number = str(row['nn'])
            obscode = str(row['ref'])
            pu = str(row['tech'])
            
            self.pdf.cell(19, 8, date, 0, 0, 'C')
            self.pdf.cell(19, 8, theta, 0, 0, 'C')
            self.pdf.cell(19, 8, rho, 0, 0, 'C')
            self.pdf.cell(19, 8, m1, 0, 0, 'C')
            self.pdf.cell(19, 8, m2, 0, 0, 'C')
            self.pdf.cell(19, 8, number, 0, 0, 'C')
            self.pdf.cell(19, 8, obscode, 0, 0, 'C')
            self.pdf.cell(19, 8, pu, 0, 0, 'C')
            self.pdf.ln(5)

    def add_page(self):
        self.pdf.add_page
    
    def save(self):
        self.pdf.output(self.filename)