from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return {"Hello World" }

@app.get("/items")
def read_items():
    return{"items":["item1",'item2','item3']}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}



@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id, "name":"JohnDoe"}


@app.post("/items/{items_id}")
def create_items(item:str, price:float):
    return{"Item":item, "Price":price}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: str, price: float):
    return {"item_id": item_id, "item": item, "price": price}

@app.delete('/items/{item_id}')
def delete_item(item_id: int):
    return {"message": "Item deleted"}


