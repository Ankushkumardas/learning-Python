from datetime import timedelta
from datetime import timezone
from datetime import datetime
from jose import jwt,JWTError

class JwtService:
    SECRET="pythonjswtsecret"
    ALGO='SHA256'
    EXPIREY_TIME=5
    def __init__(self):
        pass
    def jwt_encode(self, email: str):
        expire = datetime.now(timezone.utc) + timedelta(minutes=JwtService.EXPIREY_TIME)
        data = {
            "email": email,
            "exp": expire
        }
        return jwt.encode(data, JwtService.SECRET, algorithm=JwtService.ALGO)
    def jwt_decode(self,token:str):
        try:
            return jwt.decode(token,JwtService.SECRET,algorithms=JwtService.ALGO)
        except JWTError as ex:
            print(f"exception in jwt decode :{str(ex)}")
            return None