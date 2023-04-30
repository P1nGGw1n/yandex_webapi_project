from flask import Flask, request, jsonify, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.secret_key = 'yandex_secret_key'
db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(500))

    def __repr__(self):
        return '<Note %r>' % self.title


@app.route('/', methods=['GET', 'POST'])
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)


@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        create_note()
    return get_notes()


def create_note():
    data = request.form
    new_note = Note(title=data['title'], content=data['content'])
    db.session.add(new_note)
    db.session.commit()


def get_notes():
    notes = Note.query.all()
    return render_template('notes.html', notes=notes)


@app.route('/notes/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted successfully')
    return redirect('http://127.0.0.1:5000/')


if __name__ == '__main__':
    app.run(debug=True)
