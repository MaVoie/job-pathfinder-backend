from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from job_api.controller import router as controller_router
from job_api.personal_data_controller import router as personal_controller_router


app = FastAPI()
app.include_router(controller_router)
app.include_router(personal_controller_router)

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
