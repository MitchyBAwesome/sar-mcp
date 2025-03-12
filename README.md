# AWS Service Reference MCP Server

This MCP server provides tools to interact with the AWS Programmatic Service Reference, allowing you to:
- List all available AWS services
- Get API actions for specific AWS services

## Installation

1. Make sure you have Python 3.10 or higher installed
2. Install the required dependencies:

```bash
# Using uv (recommended)
uv venv
source .venv/bin/activate  # On Unix/macOS
.venv\Scripts\activate     # On Windows
uv pip install -r requirements.txt

# Or using pip
pip install -r requirements.txt
```

## Usage

### Running the Server

You can run the server directly:

```bash
python aws_service_reference.py
```

### Using with Claude Desktop

1. Open your Claude Desktop configuration file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. Add the server configuration:

```json
{
    "mcpServers": {
        "aws-service-reference": {
            "command": "python",
            "args": ["/ABSOLUTE/PATH/TO/aws_service_reference.py"]
        }
    }
}
```

Replace `/ABSOLUTE/PATH/TO/` with the actual path to where you saved the server file.

3. Restart Claude Desktop

### Available Tools

The server provides two tools:

1. `list_aws_services`: Lists all available AWS services
2. `get_service_actions`: Gets API actions for a specific AWS service

### Example Usage in Claude

Once connected, you can ask Claude questions like:

- "What AWS services are available?"
- "Show me all the API actions for the S3 service"
- "What operations can I perform with EC2?"

## Development

### Requirements

The project uses a requirements.txt file to manage dependencies. The main dependencies are:
- mcp[cli] - For the FastMCP server functionality
- httpx - For asynchronous HTTP requests

### Testing with MCP Inspector

You can test the server using the MCP Inspector:

```bash
mcp dev aws_service_reference.py
```

## Troubleshooting

If you encounter issues:

1. Verify your Python version is 3.10 or higher
2. Ensure all dependencies are installed correctly
3. Check the Claude Desktop logs:
   - macOS: `~/Library/Logs/Claude/mcp*.log`
   - Windows: `%APPDATA%\Claude\logs\mcp*.log`
4. Make sure you're using absolute paths in the Claude Desktop configuration

## License

This project is licensed under the MIT License. 