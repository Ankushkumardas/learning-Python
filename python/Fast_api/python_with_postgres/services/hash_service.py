import bcrypt

class HashService:
  
    secret="hashpasword"
    def __init__(self, pwd_context=None):
        pass
    
    def hash_password(self, password: str) -> str:
        password_bytes = (password + self.secret).encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed.decode('utf-8')

    def verify_hash_password(self, password: str, db_hash_pass: str) -> bool:
        password_bytes = (password + self.secret).encode('utf-8')
        db_hash_bytes = db_hash_pass.encode('utf-8')
        return bcrypt.checkpw(password_bytes, db_hash_bytes)