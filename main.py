from fastapi import FastAPI
from api.routes import router
from db.database import Base,engine

app=FastAPI( title="Dropdown menu",
    description="A combo box for teams and players",
    version="1.0.0",)
app.include_router(router)


Base.metadata.create_all(bind=engine)

# Excluding paths for bearer-token check
exclude_paths = [
    r"^/health$",
    r"^/docs$",
    r"^/openapi.json$",
    r"^/redoc$",
    r"^/docs/oauth2-redirect$",
]


