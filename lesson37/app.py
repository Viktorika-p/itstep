from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    intro = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<Article %r' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/list', methods=['POST','GET'])
def list_word():
    if request.method =="Post":
        title = request.form['word']
        trnsl = request.form['translation']

        article = Article(title=title, intro=trnsl)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return "Помилка при додаванні слова"
    else:
        return render_template("list.html")


if __name__ == "__main__":
    app.run(debug=True)
