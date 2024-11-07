from typing import Union
import time
from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from strawberry import Schema
from strawberry.fastapi import GraphQLRouter

from configs.Enviroment import get_environment_variables
from configs.GraphQL import get_graphql_context
from configs.Auth import create_access_token
from metadata.Tags import Tags
from models.BaseModel import init
from routers.v1.BookRouter import BookRouter
from routers.v1.AuthorRouter import AuthorRouter
from schemas.graphql.Query import Query
from schemas.graphql.Mutation import Mutation
from dependencies.auth_dependency import get_current_user
from services.AuthService import authenticate_user, fake_user_db, User



env = get_environment_variables()

app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(time.time() - start_time)
    return response

app.include_router(BookRouter)
app.include_router(AuthorRouter)

@app.get("/token")
def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_user_db, form_data.username, form_data.password)
    if not user:
        return HTTPException(
            status_code=400, 
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=env.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/")
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

def get_context(current_user: User = Depends(get_current_user)):
    return {"current_user": current_user}

# # GraphQL Schema and Application Instance
# schema = Schema(query=Query, mutation=Mutation)
# graphql = GraphQLRouter(
#     schema,
#     graphiql=env.DEBUG_MODE,
#     context_getter=get_graphql_context,
# )

# # Integrate GraphQL Application to the Core one
# app.include_router(
#     graphql,
#     prefix="/graphql",
#     include_in_schema=False,
# )

init()