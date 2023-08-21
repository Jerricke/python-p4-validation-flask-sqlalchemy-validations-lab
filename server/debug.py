#!/usr/bin/env python3

from app import app
from models import db, Author, Post


if __name__ == "__main__":
    with app.app_context():
        author = Author(name="", phone_number="1231144321")
        # import ipdb; ipdb.set_trace()
