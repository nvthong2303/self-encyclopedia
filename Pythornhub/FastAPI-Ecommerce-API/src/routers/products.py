from fastapi import APIRouter, Depends, Query, status
from src.core.security import get_current_user
from src.db.database import get_db
from src.services.products import ProductService
from sqlalchemy.orm import Session
from src.schemas.products import ProductCreate, ProductUpdate, ProductOut, ProductOutDelete

router = APIRouter(tags=["Products"], prefix="/products")


@router.get("/", status_code=status.HTTP_200_OK, response_model=ProductOut)
def get_all_products(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=0, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Limit of products"),
    search: str = Query("", description="Search by product name"),
):
    return ProductService.get_all_products(db, page, limit, search)
