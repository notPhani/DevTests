from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.post("/api/fetch_case")
async def fetch_case_api(
    court_code: str = Form(...),
    case_type: str = Form(...),
    reg_no: str = Form(...),
    reg_year: str = Form(...)
):
    return {
        "parties": "A vs B",
        "filing_date": "2024-09-22",
        "next_hearing": "2024-12-01",
        "latest_pdf": "https://districts.ecourts.gov.in/sample.pdf"
    } 

