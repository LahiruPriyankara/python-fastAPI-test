import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
# Doing CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get_end_point():
    print("Called get_end_point..!")
    return "Called get_end_point..!"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
