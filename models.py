from pydantic import BaseModel

class RequestBody(BaseModel):
    vec_a: list
    vec_b: list

class ResponseBody(BaseModel):
    result: float