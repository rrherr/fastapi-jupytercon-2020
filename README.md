# After model.fit, before you deploy: Prototype with FastAPI in Jupyter!

_By Ryan Herr, for JupyterCon 2020_

You want to deploy your scikit-learn model. Now what? You can make an API for your model in Jupyter! You’ll learn [FastAPI](https://fastapi.tiangolo.com/), a Python web framework with automatic interactive docs. We’ll validate inputs with type hints, and convert to a dataframe, to make new predictions with your model. You’ll have a working API prototype, running from a notebook and ready to deploy!

## Watch video

The talk was recorded in a [25 minute video on JupyterCon's YouTube channel](https://youtu.be/hGHwu1h3l6g). 

## See completed app

Go to https://penguin-predictor.herokuapp.com/

## Work on Binder

Go to https://mybinder.org/v2/gh/rrherr/fastapi-jupytercon-2020/main

## Work locally

Clone this repo and change directories
```
git clone https://github.com/rrherr/fastapi-jupytercon-2020.git

cd fastapi-jupytercon-2020
```

Create and activate a virtual environment
```
python -m venv env

source env/bin/activate
```

Install requirements into the virtual environment
```
python -m pip install -r requirements.txt
```

Install an IPython kernel for the virtual environment
```
ipython kernel install --user --name=fastapi-jupytercon-2020
```

To use notebooks, launch Jupyter Lab, then select the kernel
```
jupyter lab
```

 To use the completed app locally, run it with uvicorn
```
uvicorn app.main:app --reload
```

Deactivate the virtual environment when done
```
deactivate
```

## Deploy to Heroku

Sign up for a free Heroku account  
https://signup.heroku.com/

Download and install the Heroku Command Line Interface  
https://devcenter.heroku.com/articles/heroku-cli

Clone this repo and change directories
```
git clone https://github.com/rrherr/fastapi-jupytercon-2020.git

cd fastapi-jupytercon-2020
```

Push to Heroku
```
heroku login

heroku create

git push heroku

heroku open
```

