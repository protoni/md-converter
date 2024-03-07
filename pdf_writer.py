from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

def create_pdf_with_bookmarks_and_gray_background(path):
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter
    
    # Set background color to gray for each page
    gray_color = HexColor("#dddddd")
    c.setFillColor(gray_color)
    c.rect(0, 0, width, height, fill=1)

    # Add some content and a bookmark to the first page
    c.setFont("Helvetica", 12)
    c.setFillColorRGB(0, 0, 0) # Set text color to black
    c.drawString(100, 750, "Hello, this is page 1!")
    c.bookmarkPage("page1")
    c.addOutlineEntry("Page 1", "page1", level=0)

    # Start new page with gray background
    c.showPage()
    c.setFillColor(gray_color)
    c.rect(0, 0, width, height, fill=1)

    # Add content and a bookmark to the second page
    c.setFont("Helvetica", 12)
    c.setFillColorRGB(0, 0, 0) # Ensure text color is black
    c.drawString(100, 750, "Hello, this is page 2!")
    c.bookmarkPage("page2")
    c.addOutlineEntry("Page 2", "page2", level=0)

    c.save()

pdf_path = "example_with_bookmarks_and_background.pdf"
create_pdf_with_bookmarks_and_gray_background(pdf_path)
