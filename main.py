from fastapi import FastAPI, Depends
from pokemon_logic.PokemonService import PokemonService
from sqlalchemy.orm import Session
from database_configs.connection import engine, Base, SessionLocal, get_db
from database_configs import models
from parse_data import parse_pokemon_and_stats

from origins import origins
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)


#Setting up the FastAPI object
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# def startup_event():
#     db = SessionLocal()
#     parse_pokemon_and_stats(db)
#     db.close()

#Setting up home route for API requests
@app.get("/")
def home():
    return {"message": "Hello World"}

#Creating an API endpoint for all pokemon
@app.get("/pokemon")
def GetAllPokemon(db: Session = Depends(get_db)):
    return db.query(models.Pokemon).all()

@app.get("/PokemonStats)")
def GetAllPokemonStats(db: Session = Depends(get_db)):
    return db.query(models.PokemonStats).all()

@app.get("/pokemon-with-stats/")
def GetPokemonWithStats(db: Session = Depends(get_db)):
    pokemon_service = PokemonService(db)
    results = pokemon_service.GetPokemonWithStats()
    return results

@app.get("/pokemon/search/")
def search_pokemon(name: str, db: Session = Depends(get_db)):
    pokemon_service = PokemonService(db)
    results = pokemon_service.search_pokemon(name)
    return results