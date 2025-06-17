from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router  # ou directement tes endpoints

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
    "http://localhost:5173/employe/",
    "*"
]

# Ajout du middleware CORS *avant tout autre ajout*
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ← Utilise "*" pour test. Ensuite tu pourras mettre http://localhost:5173
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
