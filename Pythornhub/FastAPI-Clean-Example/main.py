from typing import Union
from fastapi import FastAPI, Depends
from strawberry import Schema
from strawberry.fastapi import GraphQLRouter

from configs.Enviroment import get_environment_variables
from configs.GraphQL import get_graphql_context
from metadata.Tags import Tags
from models.BaseModel import init
from routers.v1.BookRouter import BookRouter
from routers.v1.AuthorRouter import AuthorRouter
from schemas.graphql.Query import Query
from schemas.graphql.Mutation import Mutation


env = get_environment_variables()

app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags
)

app.include_router(BookRouter)
app.include_router(AuthorRouter)

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