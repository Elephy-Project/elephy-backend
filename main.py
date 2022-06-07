import uvicorn
import info

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()
app.include_router(info.router)

@app.get("/")
def root():
  return RedirectResponse("/docs")

if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
