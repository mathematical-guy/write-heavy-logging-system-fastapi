import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI


app: FastAPI = FastAPI()


@app.get(path='/home/')
async def home():
    return {"message": "hello world"}


if __name__ == "__main__":
    DOT_ENV_PATH = os.path.join(os.getcwd(), ".env")
    load_dotenv(dotenv_path=DOT_ENV_PATH)

    HOST = os.getenv('HOST')
    PORT = int(os.getenv('PORT'))

    uvicorn.run(
        app=app, host=HOST, port=PORT,
        # reload=True
    )
