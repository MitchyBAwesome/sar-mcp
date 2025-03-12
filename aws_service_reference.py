from mcp.server.fastmcp import FastMCP
import httpx
import json
from typing import List, Dict, Any

# Initialize FastMCP server
mcp = FastMCP("aws-service-reference")

# Constants
SERVICE_LIST_URL = "https://servicereference.us-east-1.amazonaws.com/"

# Helper function to fetch service list
async def fetch_service_list() -> List[Dict[str, str]]:
    """Fetch the list of AWS services and their API reference URLs."""
    async with httpx.AsyncClient() as client:
        response = await client.get(SERVICE_LIST_URL)
        response.raise_for_status()
        return response.json()

# Helper function to fetch service actions
async def fetch_service_actions(url: str) -> List[str]:
    """Fetch the list of API actions for a specific service."""
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        return [action["Name"] for action in data.get("Actions", [])]

@mcp.tool()
async def list_aws_services() -> str:
    """List all available AWS services."""
    try:
        services = await fetch_service_list()
        service_names = [service["service"] for service in services]
        return "Available AWS services:\n" + "\n".join(service_names)
    except Exception as e:
        return f"Error fetching AWS services: {str(e)}"

@mcp.tool()
async def get_service_actions(service_name: str) -> str:
    """Get API actions for a specific AWS service.
    
    Args:
        service_name: Name of the AWS service (e.g., "s3", "ec2")
    """
    try:
        services = await fetch_service_list()
        service_info = next((s for s in services if s["service"].lower() == service_name.lower()), None)
        
        if not service_info:
            return f"Service '{service_name}' not found. Use list_aws_services to see available services."
            
        actions = await fetch_service_actions(service_info["url"])
        return f"API actions for {service_name}:\n" + "\n".join(actions)
    except Exception as e:
        return f"Error fetching actions for {service_name}: {str(e)}"

if __name__ == "__main__":
    mcp.run() 