# 📜 Django Markdown-to-HTML Converter

[![Django Version](https://img.shields.io/badge/Django-4.2-green)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)

Convert your Markdown files to beautifully styled HTML pages! This Django app allows users to upload a `.md` file and see it converted to HTML format with custom styling.

[Project Link](https://roadmap.sh/projects/markdown-note-taking-app)

## 🌟 Features
- Uploads `.md` (Markdown) files and converts them to HTML.
- Styled output with CSS for clean and modern presentation.
- Instant HTML file generation upon uploading the Markdown file.
- Displays the resulting HTML file in a responsive container.

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Django 4.2 or higher

### Installation
1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/django-markdown-html-converter.git
    cd django-markdown-html-converter
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Migrate the Database**
    ```bash
    python manage.py migrate
    ```

4. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

5. **Access the App**
   Open your browser and navigate to `http://127.0.0.1:8000/` to start using the app.

### Usage
1. Go to the **Upload File** page.
2. Select a Markdown file (`.md`) from your device.
3. Click **Upload** to convert it into HTML.
4. View the converted file on the **Result** page with custom styling.

## 🧰 Project Structure

- `Note/forms.py` - Contains the form for uploading files.
- `Note/views.py` - Contains the views for handling file upload, Markdown conversion, and rendering HTML.
- `templates/index.html` - The main page where users upload their files.
- `templates/result.html` - Displays the converted HTML output.
- `static/` - CSS and other static files for styling the HTML output.

## 🛠️ Example Code

```python
import markdown

content = str(file.read(), encoding="utf-8")
tempHTML = markdown.markdown(content)
with open("template/result.html", "w", encoding="utf-8") as f2:
    f2.write(htmlcontent)
```