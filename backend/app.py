from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "mypassword"
POSTGRES_DB = "postgres"
POSTGRES_HOST = "db"
POSTGRES_PORT = "5432"

SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

    def serialize(self):
        return {"id": self.id, "username": self.username, "email": self.email}


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "use /add_user to add a user"})


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    new_user = User(username=data["username"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully"})


def initialize_db():
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    initialize_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
