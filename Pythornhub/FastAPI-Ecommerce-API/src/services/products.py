from sqlalchemy.orm import Session
from src.models import Product, Category
from src.schemas.products import ProductCreate, ProductUpdate
from src.utils.response import ResponseHandler


class ProductService:
    @staticmethod
    def get_all_products(db: Session, page: int, limit: int, search: str):
        products = db.query(Product).order_by(Product.id.asc()).filter(
            Product.name.contains(search).limit(limit).offset((page - 1) * limit).all()
        )
        return {
            "message": f"Page {page} with {limit} products",
            "data": products
        }
