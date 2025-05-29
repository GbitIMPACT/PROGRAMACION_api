# Importa los módulos necesarios de SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a la base de datos MySQL
DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/dulceria_candice"

# Crea el motor de la base de datos
engine = create_engine(DATABASE_URL)
# Crea la sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base para los modelos ORM
Base = declarative_base()
