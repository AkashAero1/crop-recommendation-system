from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated
import pickle
import pandas as pd 

with open('model.pkl' , 'rb') as f:
    model=pickle.load(f)

app=FastAPI()

class userinput(BaseModel):

    N:Annotated[int,Field(...,description="Nitrogen content in the soil")]
    P:Annotated[int,Field(...,description="phosphorus content in the soil")]
    K:Annotated[int,Field(...,description="pottasium content in the soil")]
    temperature:Annotated[float,Field(...,description="temperature")]
    humidity:Annotated[float,Field(...,description="humidity % ")]
    ph:Annotated[float,Field(...,description="Ph-Value of the soil")]
    rainfall:Annotated[float,Field(...,description="Rainfall in mm")]


@app.get("/")
def home():
    return {"message": "Crop Recommendation API is running 🚀"}

@app.post("/predict")
def predict(data: userinput):

    input_df=pd.DataFrame([{
        'N':data.N,
        'P':data.P,
        'K':data.K,
        'temperature':data.temperature,
        'humidity':data.humidity,
        'ph':data.ph,
        'rainfall':data.rainfall
    }])
    
    prediction=model.predict(input_df)[0]
    return JSONResponse(status_code=200,content={'predicted crop': prediction})
