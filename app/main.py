from fastapi import FastAPI

app = FastAPI(
    title="FileProcessor",
    summary="API for control big data file upload, processing and lifecycle.",
)


@app.get("/")
async def root():
    return {"message": "project init"}
