from fastapi import APIRouter
from app.services.loader import load_json_lines

router = APIRouter(prefix="/sentimento")

router = APIRouter(
    prefix="/sentimento",
    tags=["Sentimento"]
)

sentimento = load_json_lines("refined/sentimento/data.json")

@router.get("/")
def get_sentimento():
    return sentimento

@router.get("/top")
def get_top_area():
    return max(sentimento, key=lambda x: x["count"])

@router.get("/bottom")
def get_bottom_sentimento():
    return min(sentimento, key=lambda x: x["count"])

@router.get("/average")
def get_average_sentimento():
    average = sum(c["count"] for c in sentimento) / len(sentimento)

    formatted = f"{average:,.2f}" \
        .replace(",", "X") \
        .replace(".", ",") \
        .replace("X", ".")

    return {
        "average": formatted
    }