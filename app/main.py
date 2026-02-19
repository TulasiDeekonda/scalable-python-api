from fastapi import FastAPI
from .database import engine, Base
from .routes import router

app = FastAPI(
    title="Scalable Python API",
    version="0.1.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Register API routes
app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
