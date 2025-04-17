import pdfkit
from jinja2 import Template

# ✅ Configure the path to wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

def generate_fir_pdf(data):
    with open("templates/fir_template.html") as f:
        template = Template(f.read())
    html_out = template.render(data)
    path = f"generated_fir_{data['name'].replace(' ', '_')}.pdf"
    pdfkit.from_string(html_out, path, configuration=config)
    return path
