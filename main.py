from flask import Flask, render_template, request, redirect, url_for
from pprint import pprint

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html',all_books=all_books)


@app.route("/add")
def add():
    return render_template('add.html')

@app.route("/add-book", methods = ["GET", "POST"])
def add_book():
    book_name = request.form.get("book-name")
    book_author = request.form.get("book-author")
    book_rating = int(request.form.get("book-rating"))

    book = {
        "title": book_name,
        "author": book_author,
        "rating": book_rating,
    }

    all_books.append(book)
    pprint(all_books)

    return redirect(url_for("add"))



if __name__ == "__main__":
    app.run(debug=True)

