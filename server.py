from flask import Flask, render_template, request

app = Flask(__name__)

# Sample book data
books = [
    {
        'title': 'histroy',
        'name':'The Great Maratha',
        'author': 'Ranjit Desai',
        'description': 'A captivating historical fiction about Shivaji.',
        'image': 'https://www.holybooks.com/wp-content/uploads/The-Mahabharata-PDF.jpg',
        'pdf_link': 'https://www.holybooks.com/wp-content/uploads/Mahabharata-VOL-1.pdf'
    },
    {
        'title': 'histroy',
        'author': 'A.P.J. Abdul Kalam',
        'description': 'Autobiography of Dr. A.P.J. Abdul Kalam.',
        'image': 'static/images/download.jpeg',
        'pdf_link': '/uploads/pdf/ram.pdf'
    },
     {
        'title': 'histroy',
        'author': 'A.P.J. Abdul Kalam',
        'description': 'Autobiography of Dr. A.P.J. Abdul Kalam.',
        'image': 'static/images/download.jpeg',
        'pdf_link': '/static/pdfs/wings_of_fire.pdf'
    },
     {
        'title': 'heamu',
        'author': 'A.P.J. Abdul Kalam',
        'description': 'Autobiography of Dr. A.P.J. Abdul Kalam.',
        'image': 'static/images/download.jpeg',
        'pdf_link': '/static/pdfs/wings_of_fire.pdf'
    },
     {
        'title': 'baragava',
        'author': 'A.P.J. Abdul Kalam',
        'description': 'Autobiography of Dr. A.P.J. Abdul Kalam.',
        'image': 'static/images/download.jpeg',
        'pdf_link': '/static/pdfs/wings_of_fire.pdf'
    },
     {
        'title': 'apj',
        'author': 'A.P.J. Abdul Kalam',
        'description': 'Autobiography of Dr. A.P.J. Abdul Kalam.',
        'image': 'static/images/download.jpeg',
        'pdf_link': '/static/pdfs/wings_of_fire.pdf'
    },

    # Add more books as needed
]

# Home route to display books
@app.route('/')
def home():
    return render_template('index.html', books=books)

# Search route to handle search functionality
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    filtered_books = [book for book in books if query in book['title'].lower() or query in book['author'].lower()]
    return render_template('index.html', books=filtered_books)

if __name__ == '__main__':
    app.run(debug=True)
