from bson.objectid import ObjectId
from fastapi import APIRouter
import db as connection
from bson import ObjectId, json_util
import json
import schema
from datetime import datetime

router = APIRouter()

def create_sensor_data(ldrLingkungan, ldrLampu, suhu, humidity):
    data = schema.DataModel()
    data.data_id = ObjectId()
    data.ldrLingkungan = ldrLingkungan
    data.ldrLampu = ldrLampu
    data.suhu = suhu
    data.humidity = humidity
    data.time = datetime.now()
    return dict(data)

@router.get("/data")
async def get_data():
    data = connection.db.sensor.find({},{'_id': 0})
    return json.loads(json_util.dumps(data))

@router.post("/data")
async def post_data(add_data: schema.DataCreate):
    new_data = add_data.dict()
    sensor_data = create_sensor_data(new_data['ldrLingkungan'], new_data['ldrLampu'], new_data['suhu'], new_data['humidity'])
    connection.db.sensor.insert_one(sensor_data)
    return {'message': 'success'}

@router.delete("/data/{id}")
async def delete_data(id: str):
    if connection.db.sensor.find({'_id': ObjectId(id)}).count() == 0:
        return {"message":"Data doesn't exists"}
    else:
        data = connection.db.sensor.find_one_and_delete({'_id': ObjectId(id)})
        data = json.loads(json_util.dumps(data))
        return {"message":"Successfully deleted", "data":data}