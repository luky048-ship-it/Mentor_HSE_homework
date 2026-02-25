from typing import List, Optional
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# ====== Модель данных (для примера — в памяти) ======
@strawberry.type
class User:
    id: int
    name: str
    email: str

USERS = [
    User(id=1, name="Valera", email="valera@example.com"),
    User(id=2, name="Anna", email="anna@example.com"),
]

# ====== Query (чтение данных) ======
@strawberry.type
class Query:
    @strawberry.field
    def hello(self, name: Optional[str] = None) -> str:
        name = (name or "").strip() or "world"
        return f"Hello, {name}!"

    @strawberry.field
    def add(self, a: int, b: int) -> int:
        return a + b

    @strawberry.field
    def users(self) -> List[User]:
        return USERS

    @strawberry.field
    def user(self, id: int) -> Optional[User]:
        return next((u for u in USERS if u.id == id), None)

# ====== Mutation (изменение данных) ======
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:
        new_id = max(u.id for u in USERS) + 1 if USERS else 1
        u = User(id=new_id, name=name, email=email)
        USERS.append(u)
        return u

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()
graphql_app = GraphQLRouter(schema)  # дает /graphql + GraphiQL
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def root():
    return {"ok": True, "graphql": "http://localhost:8000/graphql"}

