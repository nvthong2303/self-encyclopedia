from fastapi import FastAPI
from src.routers import products

description = """
Welcome to the E-commerce API! 🚀

This API provides a comprehensive set of functionalities for managing your e-commerce platform.

Key features include:

- **Crud**
	- Create, Read, Update, and Delete endpoints.
- **Search**
	- Find specific information with parameters and pagination.
- **Auth**
	- Verify user/system identity.
	- Secure with Access and Refresh tokens.
- **Permission**
	- Assign roles with specific permissions.
	- Different access levels for User/Admin.
- **Validation**
	- Ensure accurate and secure input data.


For any inquiries, please contact:

* Github: https://github.com/nvthong2303
"""

app = FastAPI(
    description=description,
    title="E-commerce API",
    version="0.1",
    contact={
        "name": "Thong Nguyen",
        "url": "https://github.com/nvthong2303"
    },
    swagger_ui_parameters={
        "syntaxHighlight.theme": "monokai",
        "layout": "BaseLayout",
        "filter": True,
        "tryItOutEnabled": True,
        "onComplete": "Ok"
    },
)


@app.get("/health-check")
async def root():
    return {"message": "Welcome to the E-commerce API!"}

app.include_router(products.router)
