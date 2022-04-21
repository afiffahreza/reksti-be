from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import route

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(route.router, tags=["Sensor"])

# Root
@app.get("/")
def root():
    return {"message": "Hello World"}
