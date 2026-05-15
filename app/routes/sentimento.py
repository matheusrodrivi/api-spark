from fastapi import APIRouter
from app.services.loader import load_json_lines

router = APIRouter(prefix="/sentimento")

sentimento = load_json_lines("refined/sentimento/data.json")

@router.get("/")
def get_sentimento():
    return sentimento

@router.get("/top")
def get_top_area():
    return max(sentimento, key=lambda x: x["count"])