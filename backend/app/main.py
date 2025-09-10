from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users as users_router, auth as auth_router
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.utils import get_openapi

app = FastAPI()

# Define the token URL (this is where you’ll create login later)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

# Example: Protected route
@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token_received": token}


app = FastAPI(title="Codemonk Backend")

# QUICK (dev) - create DB tables from models
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(users_router.router)
app.include_router(auth_router.router)

@app.get("/")
def root():
    return {"message": "backend is running 🚀"}
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Codemonk Backend",
        version="0.1.0",
        description="API with JWT auth",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    openapi_schema["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
