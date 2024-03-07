import markdown
import pdfkit

# Convert Markdown to HTML
input_filename = 'index.md'
output_filename = 'output.pdf'
with open(input_filename, 'r', encoding='utf-8') as f:
    text = f.read()
html = markdown.markdown(text)

# Convert HTML to PDF
pdfkit.from_string(html, output_filename)
