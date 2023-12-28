from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    redirect,
    url_for,
    make_response,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_babel import Babel, gettext
from itertools import groupby

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///judo.db"
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQLAlchemy(app)


# your routes go her
@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/start_quiz", methods=["POST"])
def start_quiz():
    belts = request.form.getlist("belts")
    techniques = (
        JudoTechnique.query.filter(JudoTechnique.belt.in_(belts))
        .order_by(func.random())
        .all()
    )
    if not techniques:
        # Return some error message or redirect to the index with a message
        return redirect(
            url_for("index", message="No techniques found for the selected belts.")
        )

    # Convert the techniques to a list of dictionaries
    techniques_dict_list = [tech.as_dict() for tech in techniques]

    return render_template("quiz.html", techniques=techniques_dict_list)


@app.route("/check_answer", methods=["POST"])
def check_answer():
    data = request.get_json()
    user_answer = data.get("answer")
    technique_id = data.get("technique")
    technique = JudoTechnique.query.get(technique_id)
    if (
        user_answer.lower() == technique.name.lower()
        or user_answer.lower() == technique.name.lower().replace("-", " ")
    ):
        return jsonify(result="Correct!")
    else:
        return jsonify(result="Incorrect!")


@app.errorhandler(500)
def internal_server_error(error):
    response = {"error": "Internal Server Error", "message": str(error)}
    return make_response(jsonify(response), 500)


@app.errorhandler(400)
def bad_server_error(error):
    print("Request data: ", request.data)
    response = {"error": "Bad Request", "message": str(error)}
    return make_response(jsonify(response), 400)


@app.route("/congratulations")
def congratulations():
    return render_template("congratulations.html")


@app.route("/techniques")
def techniques():
    techniques = JudoTechnique.query.all()
    belt_order = ["yellow", "orange", "green", "blue", "brown"]
    techniques = sorted(techniques, key=lambda technique: belt_order.index(technique.belt))
    techniques_grouped = {k: list(v) for k, v in groupby(techniques, key=lambda x: x.belt)}
    return render_template("techniques.html", techniques_grouped=techniques_grouped)


@app.route("/single_technique")
def single_technique():
    technique_name: str = request.args.get("name")
    technique: JudoTechnique = JudoTechnique.query.filter_by(name=technique_name).one()
    return render_template("single_technique.html", technique=technique)


@app.route("/katas")
def katas():
    katas = Kata.query.all()
    return render_template("kata.html", katas=katas)

@app.route("/katas/<id>", methods = ["POST", "GET"])
def single_kata(id:str):
    kata = Kata.query.filter_by(id=id).one()
    return render_template("single_kata.html", kata=kata)

@app.route("/words")
def words():
    return render_template("words.html")


class JudoTechnique(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image_path = db.Column(db.String(100), nullable=False)
    belt = db.Column(db.String(20), nullable=False)
    alt_text = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(300), nullable=True)
    youtube_id = db.Column(db.String(200), nullable=True)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_path": self.image_path,
            "belt": self.belt,
        }


class Kata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
