from fastapi import APIRouter
from app.services.loader import load_json_lines

router = APIRouter(prefix="/areas")

areas = load_json_lines("refined/area/data.json")

@router.get("/")
def get_area():
    return areas

@router.get("/top")
def get_top_area():
    return max(areas, key=lambda x: x["count"])