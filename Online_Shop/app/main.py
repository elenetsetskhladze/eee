from fastapi import FastAPI
<<<<<<< HEAD
from app.routers import categories
from app.routers import subcategories
from app.routers import brands
from app.routers import products
from app.routers import users
from app.routers import reviews
from app.routers import carts

app = FastAPI(title="Online Shop")

app.include_router(categories.router)

app.include_router(subcategories.router)

app.include_router(brands.router)

app.include_router(products.router)

app.include_router(users.router)

app.include_router(reviews.router)

app.include_router(carts.router)
=======
from app.routers import student, course, users

app = FastAPI()

app.include_router(student.router)


app.include_router(course.router)

app.include_router(users.router)

>>>>>>> 31e6cbabc407509ec51ddc3452de5676eedca4d4
