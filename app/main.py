from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import controller
from api import personal_data_controller as personal_controller
app = FastAPI()
app.include_router(controller.router)
app.include_router(personal_controller.router)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
