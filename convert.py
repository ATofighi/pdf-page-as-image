import argparse
from pdf2image import convert_from_path
from fpdf import FPDF
import os

def main(input_pdf, output_pdf):
    # Convert the PDF to a list of images
    images = convert_from_path(input_pdf)

    # Create a new PDF
    pdf = FPDF()

    # Iterate over the images
    for i, image in enumerate(images):
        # Save the image as a PNG file
        image.save(f"page_{i}.png", "PNG")

        # Add a page to the PDF
        pdf.add_page()

        pdf.set_auto_page_break(0)

        # Add the image to the PDF
        pdf.image(f"page_{i}.png", 0, 0, 210, 297)  # A4 size in mm

    # Save the PDF
    pdf.output(output_pdf, "F")

    # Delete the temporary image files
    for i in range(len(images)):
        os.remove(f"page_{i}.png")

    print(f"The PDF file {input_pdf} was successfully converted to images and saved as a new PDF file {output_pdf}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a PDF to images and create a new PDF from those images.')
    parser.add_argument('input_pdf', type=str, help='The input PDF file.')
    parser.add_argument('output_pdf', type=str, help='The output PDF file.')
    args = parser.parse_args()
    main(args.input_pdf, args.output_pdf)


