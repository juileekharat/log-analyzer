from urllib import request
from fastapi import FastAPI, Request, UploadFile, File, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
import shutil
import os
import pandas as pd

from app.log_parser import analyse_logs

# Create the FastAPI application instance 
app = FastAPI()

# Set up Jinja2 templates to serve HTML pages from the "app/templates" directory
# This allows us to render HTML templates for our web interface.
# Jinja2 is a popular templating engine for Python that allows us 
# to create dynamic HTML pages.
templates = Jinja2Templates(directory="app/templates")

# Define the directory where uploaded files will be stored
UPLOAD_DIR = "uploads"
REPORT_DIR = "reports"

# Ensure the upload directory exists, creating it if necessary
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# Define a route for the home page that renders the "index.html" template
# The home page will be accessible at the root URL ("/") and will display the
# upload form for users to submit their files.
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request = request,
        name = "index.html"       
    )

@app.post("/upload")
# Define a route to handle file uploads. This route will accept POST requests
# UploadFile is a special type provided by FastAPI to handle file uploads. 
# The File(...) indicates that this parameter is required and should be treated as a file upload.
async def upload_log(
    request: Request,
    filex: UploadFile = File(...), 
    log_level: str = Query(default="ALL")
    ):

    if filex.filename == "":
        return { "message" : "No file uploaded." }

    # Construct the file path where the uploaded file will be saved. 
    # The file will be stored in the UPLOAD_DIR with its original filename.
    file_path = f"{UPLOAD_DIR}/{filex.filename}"

    # Open the file in binary write mode and 
    # use shutil.copyfileobj to save the uploaded file to the specified location.
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(filex.file, buffer)

    analysis = analyse_logs(file_path)

    df = pd.DataFrame(analysis['parsed_log']);
    csv_path = f"{REPORT_DIR}/log_analysis_report.csv"
    df.to_csv(csv_path, index=True)

    filtered_logs = analysis["parsed_log"]
    if log_level != "ALL":
        filtered_logs = [
            log for log in filtered_logs
            if log["level"] == log_level
        ]

    return templates.TemplateResponse(
        request=request,
        name="results.jinja",
        context={
            "analysis": analysis,
            "filtered_logs": filtered_logs,
            "selected_level": log_level
        }
    )

@app.get("/download-csv")
async def download_csv():
    csv_path = f"{REPORT_DIR}/log_analysis_report.csv"
    return FileResponse(
        path = csv_path,
        filename = "log_analysis_report.csv",
        media_type = "text/csv"
    )