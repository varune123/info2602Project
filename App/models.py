from flask_sqlalchemy import SQLAlchemy
from flask_login import UserLog
db = SQLAlchemy()

class User(db.Model, UserLog,):
    id = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(300), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)

    def toDict(self):
        return{
            "id": self.id,
            "User Id": self.userId,
            "Email:": self.email,
            "password": self.password
        } 
    

class Exercise(db.Model):
    exercise_ID = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(120), nullable=False)
    exercise_equipment = db.Column(db.String(120), nullable=False)
    exercise_type = db.Column(db.String(120), nullable=False)
    muscle_work = db.Column(db.String(120), nullable=False)
    example = db.Column(db.String(200), nullable=False)
    modify = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {
            "id": self.exercise_ID,
            "Exercise": self.exercise_name,
            "Equipment": self.exercise_equipment,
            "Exercise Type": self.exercise_type,
            "Example": self.example,
            "Modifications": self.mods
        }

        
