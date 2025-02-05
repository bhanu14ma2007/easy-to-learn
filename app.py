from flask import Flask, render_template, jsonify, send_file
import pdfkit

app = Flask(__name__)

# Sample book data (could be from a database)
books = [
    {"name": "Book One", "description": "An exciting adventure.", "image": "static/img/book1.jpg", "pdf_link": "static/files/book1.pdf"},
    {"name": "Book Two", "description": "A thrilling mystery.", "image": "static/img/book2.jpg", "pdf_link": "static/files/book2.pdf"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def get_books():
    return jsonify(books)

@app.route('/generate_pdf')
def generate_pdf():
    pdf_path = 'static/files/output.pdf'
    pdfkit.from_url('http://127.0.0.1:5000/', pdf_path)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
