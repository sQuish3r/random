from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse



def get_record(id: str = 108374010):
    html_buff  = requests.get(
        f'https://ru.dotabuff.com/players/{id}',
        headers={'User-Agent': 'APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)'}
    ).text
    soup = BeautifulSoup(html_buff, 'html.parser')
    game_record = soup.find_all("span", {"class": "game-record"})[0]
    wins = game_record.find_all("span", {"class": "wins"})[0].get_text()
    losses = game_record.find_all("span", {"class": "losses"})[0].get_text()
    abandons = game_record.find_all("span", {"class": "abandons"})[0].get_text()
    return wins, losses, abandons

app = FastAPI(
    title='Monitoring app',
    docs_url='/docs'
)
router = APIRouter()

@router.get("/records/{id}", response_class=HTMLResponse)
def get_player_record(id: str):
    w, l , a = get_record(id)
    return f"""
    <html>
        <head>
            <title>Plyers record</title>
        </head>
        <body>
            <h1> wins {w} </h1>
            <h1> losses {l} </h1>
            <h1> abandons {a} </h1>
        </body>
    </html>
    """

app.include_router(router)