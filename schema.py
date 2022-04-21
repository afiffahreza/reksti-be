from schematics.models import Model
from schematics.types import IntType, DateTimeType, FloatType, StringType
from pydantic import BaseModel
from bson import ObjectId

class DataModel(Model):
    data_id = ObjectId()
    ldrLingkungan = IntType(required=True)
    ldrLampu = IntType(required=True)
    suhu = FloatType(required=True)
    cuaca = StringType(required=True)
    time = DateTimeType(required=True)

class DataCreate(BaseModel):
    ldrLingkungan: int
    ldrLampu: int
    suhu: float
    cuaca: str