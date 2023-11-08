from flask import Flask, flash, render_template, redirect, url_for
from forms import BookForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config["SECRET_KEY"] = "b9f1f7e80d2627b5bdf11skaaieop26f67a4c49858d3f4b39eeadd8f84d5c6bb92fb0a0753"

csrf = CSRFProtect(app)


book_list = []


@app.route('/')
def index():
    return redirect(url_for("create_book"))


@app.route('/create-book', methods=['GET', 'POST',])
def create_book():
    form = BookForm()
    if form.validate_on_submit():
        new_book = {
            "title": form.title.data,
            "author": form.author.data,
            "genre": form.genre.data
        }
        book_list.append(new_book)
        return redirect(url_for("books"))
        
    return render_template("formulario.html", form=form)



@app.route('/books')
def books():
    return render_template('books.html', book_list=book_list)



if __name__ == '__main__':
    app.run(debug=True, port=8080)

