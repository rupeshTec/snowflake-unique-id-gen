from fastapi import FastAPI
from snowflake import SnowflakeGenerator

app = FastAPI()
generator = SnowflakeGenerator(machine_id=1)

@app.get("/generate-id")
def generate_id():
    unique_id = generator.generate_id()
    return {"id": unique_id}
