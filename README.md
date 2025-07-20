# metar-mcp-server

A lightweight MCP server providing METAR and TAF information over the stdio transport protocol.

## Requirements

- Python 3.12 or later
- Docker
- VS Code, Warp or another MCP Client

## How to run it locally

We suggest you to create a virtual environment for running this app with Python 3. Clone this repository and open your terminal/command prompt in a folder.

```bash
git clone https://github.com/tfraudet/PyGliderCG.git
cd ./PyGliderCG
python3 -m venv .venv
```

Then, activate the virtual environment:

On Unix systems

```bash
source .venv/bin/activate
```

On Window systems

```bash
.venv\scripts\activate
```

Then, install the requirements:

```bash
pip install -r requirements.txt
```

Build the MCP server as a docker image:

```bash
docker build -t metar-mcp-server .
```

And install the mcp-server package:

<details>
<summary>Install in VS Code (to run it locally)</summary>

On VS Code, add the following JSON block to your workspace ```.vscode/mcp.json``` file

```json
{
  "servers": {
    "Aviation Weather Center": {
      "type": "stdio",
      "command": "python",
      "args": [
        "${workspaceFolder}/server.py"
      ]
    }
  }
}
```
</details>

<details>
<summary>Install on Warp</summary>

See Warp [Model Context Protocol Documentation](https://docs.warp.dev/knowledge-and-collaboration/mcp#adding-an-mcp-server) for details.

1. Navigate Settings > AI > Manage MCP servers.
2. Add a new MCP server by clicking the + Add button.
3. Paste the configuration given below:

```json
{
  "Aviation Weather Center": {
    "command": "docker",
    "args": [
      "run",
      "-i",
      "--rm",
      "metar-mcp-server"
    ],
    "env": {},
    "working_directory": null,
    "start_on_launch": true
  }
}
```
</details>