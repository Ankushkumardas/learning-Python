
# When Do We Use Request?

# Use Request when you need:

# ✅ Headers

# ✅ Cookies

# ✅ Query Parameters

# ✅ Client IP

# ✅ Request URL

# ✅ Raw Request Data

# When Do We Use Response?

# Use Response when you need:

# ✅ Set Status Codes

# ✅ Set Cookies

# ✅ Add Headers

# ✅ Redirect Users

# ✅ Return Custom Responses


# implementing rate limiting using teh pacjage "slowapi"

from fastapi import APIRouter,Request
from fastapi import FastAPI, status, HTTPException
from user import router as user_router
from todo import router as todo_router
from slowapi import Limiter 
from slowapi.util import get_remote_address 
from slowapi.middleware import SlowAPIMiddleware 
from slowapi.errors import RateLimitExceeded

app = FastAPI()
# state varible -> and if you wnat to accessthis variable in any otehr file you can acces it from teh request of teh fast api module [Request->Request.app]
app.state.count=0

routers=[user_router,todo_router]

@app.middleware("http")
async def my_middleware(request, call_next):
    print("initial router ")
    print("Middleware Running")
    
    response = await call_next(request)
    return response
    
    
# app.include_router(user_router)
# app.include_router(todo_router)

for router in routers:
    app.include_router(router=router,prefix="/api")
    