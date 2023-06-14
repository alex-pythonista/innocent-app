from fastapi import FastAPI
from enum import Enum

class ModelName(Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get('/health')
async def health_status():
    return {
        'message': '200 OK',
    }

@app.get('/models/{model_name}')
async def select_model(model_name: ModelName):
    data = {
        'model_name': ModelName.lenet,
        'message': "LeCNN all the images",
    }
    if model_name is ModelName.alexnet:
        data['message'] = "Deep Learning FTW!"
        data['model_name'] = model_name
        return data
    elif model_name is ModelName.resnet:
        data['message'] = "Have some residuals"
        data['model_name'] = model_name
        return data
    return 

@app.get('/items/{item_id}')
async def root(item_id: int):
    return {
        'message': {
            'hello': 'world',
            'item_id': item_id,
        },
    }
