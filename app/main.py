from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>Welcome to Log Analyzer</title>
        </head>
        <body>
            <h1>Welcome to Log Analyzer</h1>
            <p>This is a simple Log Analyzer application.</p>
        </body>
    </html>
    """