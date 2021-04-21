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
        
        
