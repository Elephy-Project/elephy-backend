import uvicorn
import info

from fastapi import FastAPI

app = FastAPI()
app.include_router(info.router)

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
