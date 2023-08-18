from fastapi import FastAPI

app = FastAPI()

animals = [
        
            {
                "name": "tiger",
                "dato1": "feline",
                "dato2": "mainly asian",
                "dato3": "Stripes"
                
            },
            
            {
                "name": "turtle",
                "dato1": "reptile",
                "dato2": "Can't run, but sure can hide",
                "dato3": "This animal is very slow"
                 
            },
        
            {
                "name": "dog",
                "dato1": "mammal",
                "dato2": "omnivore",
                "dato3": "Best friend"
                 
            },

            {
                "name": "cat",
                "dato1": "mammal",
                "dato2": "feline pet",
                "dato3": "meow!"  
            },

            {
                "name": "ant",
                "dato1": "There are many different species of this insect around the world.",
                "dato2": "They can be brown, red and black",
                "dato3": "They live in soil and cavities in wood and plants"
            },

            {
                "name": "cow",
                "dato1": "Its stomach contains four separate compartments",
                "dato2": "Their flautulence is responsible for a lot of the greenhouse gases.",
                "dato3": "Their milk is very popular among human populations"
            },

            {
                "name": "crocodile",
                "dato1": "It eats fish, turtle and mammals.",
                "dato2": "lives solitarily in murky, warm and quiet waters",
                "dato3": "This reptile was around in times of the dinousaurs"
                
            },

            {
                "name": "bird",
                "dato1": "There are many different species of this animal, almost everywhere in the world",
                "dato2": "often omnivore",
                "dato3": "peak and wings"
            },

            {
                "name": "pig",
                "dato1": "Loves belly scratches",
                "dato2": "It's one of the smartest animals on Earth, equivalent to a 3 year old child",
                "dato3": "oink!"
            },
        
            {
                "name": "flea",
                "dato1": "an insect",
                "dato2": "there used to be circuses where they acted",
                "dato3": "cats and dogs are like 24/7 buses for these tiny tiny creatures"
            }
]


@app.get("/animals")
def get_all():
    return  animals


@app.get("/animal/{name}")
def get_by_name(name: str):
    animal = {}
    for item in animals:
        if item['name'] == name:
            animal = item
            break
    return animal

