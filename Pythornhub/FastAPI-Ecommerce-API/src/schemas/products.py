from pydantic import BaseModel, validator
from datetime import datetime
from typing import List, Optional, ClassVar
from src.schemas.categories import CategoryBase


class BaseConfig:
    from_attributes = True


class ProductBase(BaseModel):
    id: int
    title: str
    description: Optional[str]
    price: int

    @validator('discount_percentage', pre=True)
    def validator_discount_percentage(cls, v):
        if v < 0 or v > 100:
            raise ValueError('Discount percentage must be between 0 and 100')
        return v

    discount_percentage: float
    rating: float
    stock: int
    brand: str
    thumbnail: str
    image: List[str]
    is_published: bool
    created_at: datetime
    category_id: int
    category: CategoryBase

    class Config(BaseConfig):
        pass


class ProductCreate(ProductBase):
    id: ClassVar[int]
    category: ClassVar[CategoryBase]

    class Config(BaseConfig):
        pass


class ProductUpdate(ProductBase):
    pass


class ProductOut(BaseModel):
    message: str
    data: List[ProductBase]

    class Config(BaseConfig):
        pass


class ProductDelete(ProductBase):
    category: ClassVar[CategoryBase]


class ProductOutDelete(BaseModel):
    message: str
    data: ProductDelete
