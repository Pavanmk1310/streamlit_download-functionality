import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Directory to save the generated PDF
pdf_dir = "pdf_files"
os.makedirs(pdf_dir, exist_ok=True)
file_name = os.path.join(pdf_dir, "output.pdf")

def create_pdf(text_to_insert, file_name):
    # Create a canvas object
    c = canvas.Canvas(file_name, pagesize=letter)

    # Set font and size
    c.setFont("Helvetica", 12)

    # Insert the string into the PDF
    c.drawString(100, 750, text_to_insert)

    # Save the PDF file
    c.save()

# The string to be inserted into the PDF
text_to_insert = "My Name ABC, My Mobile Number is 3421117301. My bd official Number is +1(111)333–1101, My foreign phone number is +1(111)333–9999. my yahoo mail is support_1234@gmail.com"

# Streamlit app
st.title("PDF Generator")

# Automatically create the PDF when the page loads
create_pdf(text_to_insert, file_name)
st.success("PDF created successfully!")

with open(file_name, "rb") as f:
    st.download_button(
        label="Download PDF",
        data=f,
        file_name="output.pdf",
        mime="application/pdf"
    )
