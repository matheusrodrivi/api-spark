from fastapi import APIRouter
from app.services.loader import load_json_lines

router = APIRouter(prefix="/problems")

problems = load_json_lines("refined/top-problems/data.json")

@router.get("/")
def get_problems():
    return problems

@router.get("/top")
def get_top_problems():
    return max(problems, key=lambda x: x["count"])