from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super_secret_vibe_code_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes_platform.db'
db = SQLAlchemy(app)

# --- DATABASE MODELS ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    version = db.Column(db.Integer, default=1)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

class NoteHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    version = db.Column(db.Integer)
    edited_by = db.Column(db.String(80))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))
    author = db.Column(db.String(80))
    text = db.Column(db.Text, nullable=False)

# --- ROUTES ---
@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    notes = Note.query.all()
    return render_template('index.html', notes=notes, username=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
        session['username'] = username
        session['user_id'] = user.id
        return redirect(url_for('index'))
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>⚡ SyncHub Login</title>
            <style>
                body { 
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; 
                    background: linear-gradient(135deg, #0B132B 0%, #111D4A 100%); 
                    color: #FFFFFF; 
                    margin: 0; 
                    display: flex; 
                    justify-content: center; 
                    align-items: center; 
                    height: 100vh; 
                    overflow: hidden;
                }
                .login-box { 
                    background: #1C2541; 
                    border: 1px solid #3A506B; 
                    padding: 40px; 
                    border-radius: 20px; 
                    width: 100%; 
                    max-width: 380px; 
                    text-align: center; 
                    box-shadow: 0 15px 35px rgba(0,0,0,0.4); 
                }
                h2 { 
                    font-size: 24px; 
                    font-weight: 800; 
                    margin-bottom: 8px; 
                    background: linear-gradient(to right, #4EA8DE, #56CFE1); 
                    -webkit-background-clip: text; 
                    -webkit-text-fill-color: transparent; 
                }
                p {
                    font-size: 14px;
                    color: #64625c;
                    margin-top: 0;
                    margin-bottom: 24px;
                }
                .input-field { 
                    width: 100%; 
                    border: 1px solid #3A506B; 
                    background: #0B132B; 
                    color: white; 
                    padding: 14px; 
                    border-radius: 10px; 
                    font-size: 15px; 
                    outline: none; 
                    box-sizing: border-box;
                    margin-bottom: 20px;
                    text-align: center;
                    transition: 0.2s;
                }
                .input-field:focus { 
                    border-color: #4EA8DE; 
                    box-shadow: 0 0 8px rgba(78, 168, 222, 0.2);
                }
                .btn-join { 
                    width: 100%;
                    background: linear-gradient(90deg, #4EA8DE, #56CFE1); 
                    color: #0B132B; 
                    border: none; 
                    padding: 14px; 
                    border-radius: 10px; 
                    font-size: 15px; 
                    font-weight: 700; 
                    cursor: pointer; 
                    transition: 0.2s;
                }
                .btn-join:hover { 
                    transform: translateY(-1px); 
                    box-shadow: 0 6px 20px rgba(86, 207, 225, 0.4); 
                }
            </style>
        </head>
        <body>
            <div class="login-box">
                <h2>💬 SyncHub Workspace</h2>
                <p>Enter team handles to establish connection</p>
                <form method="post">
                    <input type="text" name="username" class="input-field" required placeholder="Enter GitHub Username" autocomplete="off">
                    <button type="submit" class="btn-join">⚡ Launch Platform</button>
                </form>
            </div>
        </body>
        </html>
    '''

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/note/create', methods=['POST'])
def create_note():
    title = request.form['title']
    content = request.form['content']
    new_note = Note(title=title, content=content, author_id=session.get('user_id'))
    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/note/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == 'POST':
        history = NoteHistory(note_id=note.id, title=note.title, content=note.content, version=note.version, edited_by=session['username'])
        db.session.add(history)
        
        note.title = request.form['title']
        note.content = request.form['content']
        note.version += 1
        note.updated_at = datetime.utcnow()
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', note=note)

@app.route('/note/<int:note_id>')
def view_note(note_id):
    note = Note.query.get_or_404(note_id)
    history = NoteHistory.query.filter_by(note_id=note_id).order_by(NoteHistory.version.desc()).all()
    comments = Comment.query.filter_by(note_id=note_id).all()
    return render_template('view.html', note=note, history=history, comments=comments)

@app.route('/note/<int:note_id>/comment', methods=['POST'])
def add_comment(note_id):
    text = request.form['text']
    comment = Comment(note_id=note_id, author=session['username'], text=text)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('view_note', note_id=note_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)