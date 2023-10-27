from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///judo.db'
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)

class JudoTechnique(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image_path = db.Column(db.String(100), nullable=False)
    belt = db.Column(db.String(20), nullable=False)
    alt_text = db.Column(db.String(50), nullable=True)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image_path': self.image_path,
            'belt': self.belt
        }

class Kata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }


@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    belts = request.form.getlist('belts')
    techniques = JudoTechnique.query.filter(JudoTechnique.belt.in_(belts)).order_by(func.random()).all()
    print(belts, techniques)
    if not techniques:
        # Return some error message or redirect to the index with a message
        return redirect(url_for('index', message="No techniques found for the selected belts."))

    # Convert the techniques to a list of dictionaries
    techniques_dict_list = [tech.as_dict() for tech in techniques]

    return render_template('quiz.html', techniques=techniques_dict_list)




@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.form['answer']
    technique_id = request.form['technique_id']
    technique = JudoTechnique.query.get(technique_id)
    if user_answer.lower() == technique.name.lower() or user_answer.lower().replace(' ','-') == technique.name.lower():
        return jsonify(result="Correct!")
    else:
        return jsonify(result="Incorrect!")

@app.route('/congratulations')
def congratulations():
    return render_template('congratulations.html')

@app.route('/techniques')
def techniques():
    techniques = JudoTechnique.query.all()
    return render_template('techniques.html', techniques=techniques)

@app.route('/katas')
def katas():
    katas = Kata.query.all()
    return render_template('kata.html', katas=katas)


@app.route('/words')
def words():
    return render_template('words.html')



if __name__ == '__main__':
    app.run(debug=True)
