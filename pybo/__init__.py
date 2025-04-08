from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myworkout.db'  # 또는 다른 DB

    db.init_app(app)
    migrate.init_app(app, db)  # ← 이 줄이 중요!

    return app
