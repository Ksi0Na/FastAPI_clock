from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
from pytz import timezone

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_time(request: Request, id: str):
    moscow = timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow)
    msc_date = moscow_time.strftime('%d.%m.%Y')
    msc_time = moscow_time.strftime('%H:%M:%S')
    return templates.TemplateResponse("index.html", {"request": request, "id": id})

