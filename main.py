import fastapi
import uvicorn
from typing import Optional
#httpstatuses.com

api = fastapi.FastAPI()

@api.get('/')
def index():
    body="<html>" \
         "<body>" \
         "<h3>try /api/calculate</h3>" \
         "</body>" \
         "</html>"
    return fastapi.responses.HTMLResponse(content=body)

@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.responses.JSONResponse(content={"error": "ERROR: Z cannot be zero"}, status_code=400)

    value = (x + y)

    if z is not None:
        value /= z

    return{
        'x': x,
        'y': y,
        'z': z,
        'value': value
    }


uvicorn.run(api, port=8000, host="127.0.0.1")
