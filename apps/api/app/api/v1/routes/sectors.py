from fastapi import APIRouter

from app.schemas.common import SectorEnum

router = APIRouter()


@router.get("")
def list_sectors() -> dict[str, list[dict[str, str]]]:
    return {
        "items": [
            {"name": sector.value, "ticker": ticker}
            for sector, ticker in {
                SectorEnum.INDUSTRIALS: "XLI",
                SectorEnum.MATERIALS: "XLB",
                SectorEnum.ENERGY: "XLE",
                SectorEnum.INFORMATION_TECHNOLOGY: "XLK",
            }.items()
        ]
    }

