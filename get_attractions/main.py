import math
from typing import List
from fastapi import FastAPI, HTTPException
import googlemaps
from haversine import haversine, Unit
from pydantic import BaseModel
from google.cloud import secretmanager

app = FastAPI()

def get_secret(secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/YOUR_PROJECT_ID/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

GOOGLE_MAPS_API_KEY = get_secret("google-maps-api-key")

class Attraction(BaseModel):
    name: str
    address: str
    distance_km: float
    bearing_degrees: int

# ... (rest of your existing code for calculate_bearing and find_attractions functions)

@app.get("/attractions/", response_model=List[Attraction])
async def get_attractions(lat: float, lon: float) -> List[Attraction]:
    try:
        return find_attractions(lat, lon)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

def start():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    start()