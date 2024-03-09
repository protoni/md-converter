# md-converter
Tools to convert markdownfiles to html or pdf

# Setup
```
choco install pandoc
choco install wkhtmltopdf
```

# Convert markdown to html
```
Convert md to html using pandoc tool. Use custom css file.

pandoc -s .\index.md --toc --toc-depth=3 --css=styles.css -o output.html

# Multiple files can be added at the same time to the output
pandoc -s `
example_data\index.md `
example_data\wsl.md `
--toc --toc-depth=3 --css=styles.css -o example_output.html
```

# Convert markdown to pdf
```
# Setup
python -m venv pdf_writer_env
pdf_writer_env/Scripts/activate
pip install markdown pdfkit

# Convert
python .\md_to_pdf.py

# Guidelines
- Code blocks
  - For source code, use 3x ` + python/bash or other syntax highlighter. Otherwise
    the code blocks gets rendered weirdly

- Headlines
  - Start markdown with #h1 tag, this way table of content gets properly separates
    content per page.

- Images
  - Add empty line before any image tag (![img]...). Otherwise the layout gets
    messed up.
```

# Generate pdf
```
Some pdf generator that ChatGPT spit out. Need to experiment further so save here

# Setup
python -m venv pdf_writer_env
pdf_writer_env/Scripts/activate
pip install reportlab

# Generate
python .\pdf_writer.py
```