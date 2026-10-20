from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI()


@app.get("/")
async def root():
    return HTMLResponse(content="<h1>GroupPay</h1>")

@app.get("/health")
async def health():
    return JSONResponse(
        media_type="application/health+json",
        status_code=200,
        content={
            "status": "pass"
        }
    )

@app.get("/items/{item_id}")
async def get_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}