from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///career.db"
db = SQLAlchemy(app)

class Career(db.Model):
    Sno = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(200), nullable = False)
    Phone = db.Column(db.BigInteger, nullable = False)
    Email = db.Column(db.String(200), nullable = False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.fname}"
    
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/allcareers')
def all_car():
    return 'These are all the available careers'

if __name__ == '__main__':
    app.run(debug = True)