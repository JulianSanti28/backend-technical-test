import sys
import os

# Ajuste para que Python encuentre el directorio 'app'
sys.path.append(os.getcwd())

from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash

def init_db():
    db = SessionLocal()
    try:
        # Si ya existe el admin
        user = db.query(User).filter(User.username == "admin").first()
        
        password_to_hash = "admin123"
        hashed = get_password_hash(password_to_hash)

        if user:
            print(f"Usuario 'admin' ya existe. Actualizando su contraseña a '{password_to_hash}'...")
            user.hashed_password = hashed
        else:
            print(f"Creando usuario 'admin' con contraseña '{password_to_hash}'...")
            new_user = User(username="admin", hashed_password=hashed)
            db.add(new_user)
        
        db.commit()
        print("Usuario inicializado correctamente")
        
    except Exception as e:
        print(f"Error al crear datos iniciales: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    print("Iniciando carga de datos...")
    init_db()