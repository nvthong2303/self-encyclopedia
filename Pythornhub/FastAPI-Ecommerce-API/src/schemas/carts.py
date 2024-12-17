from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from src.schemas.products import ProductBase, CategoryBase


class BaseConfig:
    from_attributes = True


class ProductBaseCart(ProductBase):
    category: CategoryBase = Field(exclude=True)

    class Config(BaseConfig):
        pass


class CartItemBase(BaseModel):
    id: int
    product_id: int
    quantity: int
    subtotal: float
    product: ProductBaseCart


class CartBase(BaseModel):
    id: int
    user_id: int
    total_mount: float
    cart_items: List[CartItemBase]
    created_at: datetime

    class Config(BaseConfig):
        pass


class CartOut(BaseModel):
    message: str
    data: CartBase

    class Config(BaseConfig):
        pass
