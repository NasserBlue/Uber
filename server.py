from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Uber Trips MCP")

# Configuration credentials from your Uber Developer Dashboard
CLIENT_ID = "YXR16Ql_jralhFHU45SFbz2eK7PlQLMm"
CLIENT_SECRET = "NP_lhlxDJnbTuNTFyftUVrL4DmXKa31dJ5MCyg_J"
REDIRECT_URI = "http://localhost:8000/callback"

@mcp.tool()
def get_driver_trips() -> str:
    """Fetch the driver's past trips and earnings history from Uber."""
    return "Placeholder: Uber API connection active."

# Expose MCP over HTTP/SSE for Gemini using sse_app()
app = FastAPI()
app.mount("/mcp", mcp.sse_app())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
