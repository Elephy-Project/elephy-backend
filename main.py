# import uvicorn
import info
import authentication

from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(authentication.router)
app.include_router(info.router, dependencies=[Depends(authentication.get_current_active_user)])

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://elephy.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def root():
  return RedirectResponse("/docs")

# if __name__ == "__main__":
#   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
