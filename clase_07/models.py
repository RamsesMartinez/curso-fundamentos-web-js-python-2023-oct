import hashlib
import os

from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

# UserMixin es una clase proporcionada por Flask-Login que incluye implementaciones
# genéricas apropiadas para la mayoría de los modelos de usuario.

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    # Relación uno a muchos: Un usuario puede tener muchos posts
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def generate_password_hash(self, password):
        """Generate a hash for a password with an added salt."""
        # Generar sal aleatoria
        salt = os.urandom(16)
        # Preparar la contraseña con la sal. Usamos b para asegurar que es un bytes literal.
        password_salt = password.encode('utf-8') + salt
        # Crear un hash con SHA-256 (de nuevo, no es recomendado para producción)
        password_hash = hashlib.sha256(password_salt).hexdigest()
        # Convertir la sal a una representación hex para guardarla
        salt_hex = salt.hex()
        # Devolver el hash y la sal
        return password_hash, salt_hex


    def set_password(self, password):
            # self.password_hash = generate_password_hash(password)
            self.password_hash = self.generate_password_hash(password)

    def check_password_hash(self, stored_password_hash, stored_salt, password_to_check):
        """Check if a password matches the stored hash and salt."""
        # Convertir la sal almacenada de hex a bytes
        salt = bytes.fromhex(stored_salt)
        # Preparar la contraseña con la sal
        password_salt = password_to_check.encode('utf-8') + salt
        # Calcular el hash de la contraseña proporcionada
        password_hash = hashlib.sha256(password_salt).hexdigest()
        # Comparar los hashes
        return password_hash == stored_password_hash


    def check_password(self, password):
        # return check_password_hash(self.password_hash, password)
        return self.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.body}>'

# Necesitas inicializar la base de datos antes de usarla, lo cual normalmente sucede en tu archivo principal
# Por ejemplo, en tu app.py, después de crear la aplicación y antes de ejecutarla, harías:
# from models import db
# db.init_app(app)
