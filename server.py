from fastapi import FastAPI
from mcp.server.lowlevel.server import Server

# Initialize standard MCP server
app = FastAPI()
mcp_server = Server("Uber Trips MCP")

@mcp_server.list_tools()
async def handle_list_tools() -> list:
    return [{
        "name": "get_driver_trips",
        "description": "Fetch the driver's past trips and earnings history from Uber.",
        "inputSchema": {"type": "object", "properties": {}}
    }]

# Mount standard ASGI endpoint
app.mount("/", mcp_server.create_initialization_options()) # Or handle via standard transport

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
