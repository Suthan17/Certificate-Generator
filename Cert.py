import streamlit as st
import pandas as pd
import os
import io
import zipfile
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4  # Import both letter and A4 sizes
from reportlab.lib import colors

def generate_pdf_certificate_dynamic_font(template_path, name, output_path, custom_color, max_font_size, horizontal_offset, vertical_offset):
    # Calculate the dynamic font size based on the length of the name and the max font size
    base_font_size = max_font_size
    max_name_length = 25
    if len(name) > max_name_length:
        font_size = base_font_size * (max_name_length / len(name))
    else:
        font_size = base_font_size

    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)  # Use A4 size here
    
    # Set font, size, and color
    c.setFont("Helvetica-Bold", font_size)
    c.setFillColor(colors.HexColor(custom_color))
    


    # Calculate the x coordinate for centering the text horizontally
    text_width = c.stringWidth(name, "Helvetica-Bold", font_size)
    x = ((letter[0] - text_width) / 2) + horizontal_offset 
    y = (letter[1] / 2) + vertical_offset  # Keep your existing vertical offset
    
    # Draw the name string at the specified (x, y) coordinates
    c.drawString(x, y, name)
    c.save()
    
    packet.seek(0)
    new_pdf = PdfReader(packet)
    
    existing_pdf = PdfReader(open(template_path, "rb"))
    output = PdfWriter()
    
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    
    with open(output_path, "wb") as outputStream:
        output.write(outputStream)

def generate_batch_certificates(template_path, names, output_directory, custom_color, max_font_size, horizontal_offset, vertical_offset):
    for i, name in enumerate(names):
        output_path = f"{output_directory}/Certificate_{name}.pdf"
        generate_pdf_certificate_dynamic_font(template_path, name, output_path, custom_color, max_font_size, horizontal_offset, vertical_offset)

# Streamlit App
st.title("Certificate Name Batch Generator")

excel_file = st.file_uploader("Upload Excel file with names:", type=["xlsx"])
if excel_file:
    df = pd.read_excel(excel_file)
    st.write("Data preview:")
    st.write(df.head())
    column = st.selectbox("Select the column to use for names:", df.columns)
    names = df[column].dropna().str.upper()

pdf_file = st.file_uploader("Upload PDF template for certificate:", type=["pdf"])
if pdf_file:
    with open("template.pdf", "wb") as f:
        f.write(pdf_file.read())

vertical_offset = st.slider("Vertical Offset", 0, 200, 105)
horizontal_offset = st.slider("Horizontal Offset", -50, 50, -20)  # Adjust the range as needed
custom_color = st.color_picker("Font Color", '#023149')
max_font_size = st.slider("Maximum Font Size", 10, 100, 30)

if st.button("Generate One Certificate for Preview"):
    if excel_file and pdf_file:
        output_directory = "Certificates"
        os.makedirs(output_directory, exist_ok=True)
        # Generate one certificate for preview
        generate_batch_certificates("template.pdf", names[:1], output_directory, custom_color, max_font_size, horizontal_offset, vertical_offset)
        
        # Provide a link to download the previewed certificate
        previewed_certificate = os.path.join(output_directory, f"Certificate_{names[0]}.pdf")
        st.write("Preview of the first certificate:")
        st.download_button(f"Download Previewed Certificate", previewed_certificate)

if st.button("Generate All Certificates"):
    if excel_file and pdf_file:
        output_directory = "Certificates"
        os.makedirs(output_directory, exist_ok=True)
        generate_batch_certificates("template.pdf", names, output_directory, custom_color, max_font_size, horizontal_offset, vertical_offset)

        zip_path = "Certificates.zip"
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for root, _, files in os.walk(output_directory):
                for file in files:
                    zipf.write(os.path.join(root, file), file)

        st.success("Certificates generated and zipped!")
        st.download_button("Download Zipped Certificates", zip_path)
