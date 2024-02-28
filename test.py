import PyPDF2

def write_to_pdf(output_file, text):
    # Create a new PDF file
    pdf_writer = PyPDF2.PdfWriter()

    # Create a new page with the text
    page = PyPDF2.pdf.PageObject.createTextObject(text)
    pdf_writer.addPage(page)

    # Write the changes to the output PDF file
    with open(output_file, 'wb') as output:
        pdf_writer.write(output)

if __name__ == "__main__":
    output_pdf = "output.pdf"  # Path to the output PDF file
    text_to_write = "This text is written using PyPDF2!"  # Text to be written to the PDF

    write_to_pdf(output_pdf, text_to_write)
