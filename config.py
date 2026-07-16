import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI',
        'postgresql://usuario:contraseña@localhost:5432/mi_base_de_datos'
    )
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', "crear_contraseña")
