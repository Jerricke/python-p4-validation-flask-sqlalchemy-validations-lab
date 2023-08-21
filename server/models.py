from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = "authors"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("name")
    def validate_name(self, key, value):
        names = [a.name for a in Author.query.all()]
        # names = db.session.query(Author.name).all()
        print(not value)
        if not value:
            raise ValueError("Name must be included")
        elif value in names:
            raise ValueError("Name must be unique")
        return value

    # @validates("name")
    # def validate_name(self, key, name):
    #     names = db.session.query(Author.name).all()
    #     if not name:
    #         raise ValueError("Name field is required.")
    #     elif name in names:
    #         raise ValueError("Name must be unique.")
    #     return name

    @validates("phone_number")
    def validate_phone_number(self, key, value):
        if len(value) != 10:
            raise ValueError("Invalid phone number")
        return value

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name})"


class Post(db.Model):
    __tablename__ = "posts"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("title")
    def validate_title(self, key, value):
        if value == None:
            raise ValueError("Title must be included")
        elif value not in ["Won't Believe", "Secret", "Top", "Guess"]:
            raise ValueError("Ttle must be clickbait-y")
        return value

    @validates("content")
    def validate_content(self, key, value):
        if len(value) <= 250:
            raise ValueError("Post content must be longer than 250 characters")
        return value

    @validates("summary")
    def validate_summary(self, key, value):
        if len(value) >= 250:
            raise ValueError("Post summary must be shorter than 250 characters")
        return value

    @validates("category")
    def validate_categiry(self, key, value):
        if value not in ["Fiction", "Non-Fiction"]:
            raise ValueError("Post category is not valid")
        return value

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})"
