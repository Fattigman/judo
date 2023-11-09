# Import the app, db, JudoTechnique, and Kata classes from app.py
from ..app import app, db, JudoTechnique, Kata

# Import the pytest library
import pytest


# Define a pytest fixture to set up and tear down the database
@pytest.fixture
def setup_db():
    # Use the app context
    with app.app_context():
        # Drop all tables
        db.drop_all()
        # Create all tables
        db.create_all()
        # Yield the db object
        yield db
        # Drop all tables
        db.drop_all()


# Define a pytest function to test the JudoTechnique model
def test_judo_technique_model(setup_db):
    # Use the setup_db fixture
    db = setup_db
    # Create a JudoTechnique instance
    technique = JudoTechnique(
        name="seoi-nage", belt="yellow", image_path="static/images/seoi_nage.jpeg"
    )
    # Add and commit the technique to the db
    db.session.add(technique)
    db.session.commit()
    # Use the pytest assert statement to check if the technique is in the db
    assert technique in db.session
    # Use the pytest assert statement to check if the technique attributes are correct
    assert technique.name == "seoi-nage"
    assert technique.belt == "yellow"
    assert technique.image_path == "static/images/seoi_nage.jpeg"


# Define a pytest function to test the Kata model
def test_kata_model(setup_db):
    # Use the setup_db fixture
    db = setup_db
    # Create a Kata instance
    kata = Kata(name="Nage-no-kata")
    # Add and commit the kata to the db
    db.session.add(kata)
    db.session.commit()
    # Use the pytest assert statement to check if the kata is in the db
    assert kata in db.session
    # Use the pytest assert statement to check if the kata attributes are correct
    assert kata.name == "Nage-no-kata"
