from fastapi import APIRouter
from app.services.loader import load_json_lines

router = APIRouter(prefix="/uf")

uf = load_json_lines("refined/UF/data.json")

@router.get("/")
def get_uf():
    return uf

@router.get("/top")
def get_top_area():
    return max(uf, key=lambda x: x["count"])