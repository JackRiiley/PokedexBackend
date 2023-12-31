import csv
from sqlalchemy.orm import Session
from database_configs.models import Pokemon, PokemonStats

def parse_pokemon_and_stats(db: Session):
    csv_file = "./Pokemon.csv"
    
    #Opens the CSV file and reads it
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            number = int(row["#"])
            name = row["Name"]
            type1 = row["Type 1"]
            type2 = row["Type 2"]
            generation = int(row["Generation"])
            legendary = row["Legendary"] == "True"
            total = int(row["Total"])
            hp = int(row["HP"])
            attack = int(row["Attack"])
            defense = int(row["Defense"])
            sp_atk = int(row["Sp. Atk"])
            sp_def = int(row["Sp. Def"])
            speed = int(row["Speed"])
            
            #create an instancec fo the pokemonStats Model
            pokemon_stats = PokemonStats(total=total, hp=hp, attack=attack, defense=defense, sp_atk=sp_atk, sp_def=sp_def, speed=speed) 
            
            #create instance of Pokemon Model and populate data
            pokemon = Pokemon(number=number, name=name, type1=type1, type2=type2, generation=generation, legendary=legendary, stats=pokemon_stats)
            
            db.add(pokemon)
            db.add(pokemon_stats)
            
        db.commit()
        db.close()