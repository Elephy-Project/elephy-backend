# Elephy Backend

## Set up .env
```
Database
PGUSER
PGPASSWORD
PGPORT
PGDATABASE
PGHOST

SECRET_KEY
- Secret key to generate jwt token
ALGORITHM
- Algorithm to generate jwt token
```
To access to the resources, a user must already recorded in the database with username and hashed password field

Visit `https://elephy-backend.vercel.app/docs`


## Run the web application
### 1. Create visual environment
`python3 -m venv env`

### 2. Activate the environment
`. env/bin/activate`

### 3. Install requirements
`pip install -r requirements.txt`


## Run application
`uvicorn --port 8000 --host 127.0.0.1 main:app --reload`

## UI Interface
Visit 
`http://127.0.0.1:8000/docs/` or `http://127.0.0.1:8000/redoc`