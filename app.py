from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Folder for HTML templates
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": ""})

@app.post("/", response_class=HTMLResponse)
async def home_post(request: Request, name: str = Form(...)):
    message = f"Hello {name}, Welcome to the Kubernetes test application!!!"
    return templates.TemplateResponse("index.html", {"request": request, "message": message})

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=5000)