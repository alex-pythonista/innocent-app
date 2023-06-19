from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel


class Item(BaseModel):
    title: str
    description: str | None = None
    price: float
    # tax: float | None = None
    isAvaialable: bool | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.price >= 3000:
        price_with_tax = item.price + (item.price * 0.15)
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict