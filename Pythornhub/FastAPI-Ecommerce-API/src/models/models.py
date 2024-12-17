from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Float, ARRAY, Enum
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from src.db.database import Base


class User(Base):
    __table__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    is_active = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP, server_default=text('NOW()'), nullable=False)
    role = Column(Enum('admin', 'user', name='user_roles'), nullable=False, server_default='user')
    carts = relationship('Cart', back_populates='user')


class Cart(Base):
    __table__ = 'carts'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text('NOW()'), nullable=False)
    total_amout = Column(Float, nullable=False)
    user = relationship('User', back_populates='carts')
    cart_items = relationship('CartItem', back_populates='cart')


class CartItem(Base):
    __table__ = 'cart_items'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('carts.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
    quantity = Column(Integer, nullable=False)
    subtotal = Column(Float, nullable=False)
    cart = relationship('Cart', back_populates='cart_items')
    product = relationship('Product', back_populates='cart_items')


class Category(Base):
    __table__ = 'categories'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String, nullable=False)
    products = relationship('Product', back_populates='category')


class Product(Base):
    __table__ = 'products'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    discount_percentage = Column(Float, nullable=False)
    rating = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    thumbnail = Column(String, nullable=False)
    image = Column(ARRAY(String), nullable=False)
    is_published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP, server_default=text('NOW()'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    category = relationship('Category', back_populates='products')
    cart_items = relationship('CartItem', back_populates='product')
