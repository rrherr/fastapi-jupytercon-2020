import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
import pandas as pd
from pydantic import BaseModel, confloat

description = """
Deploys a logistic regression model fit on the [Palmer Penguins](https://github.com/allisonhorst/palmerpenguins) dataset.

<img src="https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png" width="40%" /> <img src="https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/culmen_depth.png" width="30%" />

Artwork by [@allison_horst](https://twitter.com/allison_horst)
"""

app = FastAPI(
    title='🐧 Penguin predictor API',
    description=description, 
    docs_url='/'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*']
)

classifier = load('app/classifier.joblib')


class Penguin(BaseModel):
    """Parse & validate penguin measurements"""
    bill_length_mm: confloat(gt=32, lt=60)
    bill_depth_mm: confloat(gt=13, lt=22)

    def to_df(self):
        """Convert to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])


@app.post('/predict')
def predict_species(penguin: Penguin):
    """Predict penguin species from bill length & depth
    
    Parameters
    ----------
    bill_length_mm : float, greater than 32, less than 60  
    bill_depth_mm : float, greater than 13, less than 22  

    Returns
    -------
    str "Adelie", "Chinstrap", or "Gentoo"  
    """
    species = classifier.predict(penguin.to_df())
    return species[0]


@app.get('/random')
def random_penguin():
    """Return a random penguin species"""
    species = random.choice(['Adelie', 'Chinstrap', 'Gentoo'])
    return species
