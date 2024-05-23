from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    username = db.Column(db.String(150), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self) -> str:
        return f"<User {self.username}"
    
    