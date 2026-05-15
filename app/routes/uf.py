from fastapi import APIRouter
from app.services.loader import load_json_lines

router = APIRouter(
    prefix="/uf",
    tags=["UF"]
)

uf = load_json_lines("refined/UF/data.json")

@router.get("/")
def get_uf():
    return uf

@router.get("/top")
def get_top_area():
    return max(uf, key=lambda x: x["count"])

@router.get("/bottom")
def get_bottom_uf():
    return min(uf, key=lambda x: x["count"])

@router.get("/average")
def get_average_uf():
    average = sum(c["count"] for c in uf) / len(uf)

    formatted = f"{average:,.2f}" \
        .replace(",", "X") \
        .replace(".", ",") \
        .replace("X", ".")

    return {
        "average": formatted
    }