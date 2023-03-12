from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from datetime import datetime
from pytz import timezone

# class Clock(BaseModel):
#     date: str = '00.00.0000'
#     time: str = '00:00:00'

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def val_update():
    moscow = timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow)
    msc_date = moscow_time.strftime('%d.%m.%Y')
    msc_time = moscow_time.strftime('%H:%M')
    # msc_time = moscow_time.strftime('%H:%M:%S')
    d = {'date': msc_date, 'time': msc_time}
    return d

@app.get("/items/id", response_class=HTMLResponse)
async def read_time(request: Request, id: str):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})

# @app.post("/items", response_class=HTMLResponse)
# async def create_clock():
#     d = val_update()
#     clock = Clock(date=d['date'], time=d['time'])
#     return clock

@app.get("/items", response_class=HTMLResponse)
async def get_clock_data(request: Request):
    d = val_update()
    # clock = Clock(date=d['date'], time=d['time'])
    return templates.TemplateResponse("index.html", {"request": request, 'date': d['date'], 'time': d['time']})

