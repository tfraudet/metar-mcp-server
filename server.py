from mcp.server.fastmcp import FastMCP
import httpx

# APIs https://aviationweather.gov/data/api/#/Data/dataMetars

# Constants
AWI_API_BASE =  'https://aviationweather.gov/api/data' 
USER_AGENT = "weather-app/1.0"

# Create an MCP server
mcp = FastMCP("Metar")

async def make_awi_request(url: str) -> dict:
	"""Make a request to the Aviation Weather Center API and return the JSON response."""

	headers = {
		"User-Agent": USER_AGENT,
		"Accept": "application/json",
	}

	# if &format=json is not part of the url, add it
	if "format=json" not in url:
		url += "&format=json"

	async with httpx.AsyncClient() as client:
		response = await client.get(url, headers=headers, timeout=30.0)
		response.raise_for_status()
		return response.json()


@mcp.tool()
async def get_metar(icao: str) -> dict:
	"""Get METAR information for a specific airport.

	Args:
		icao: 4 letters airport code (e.g. LFLC for Clermont-Ferrand Auvergne Airport)
	"""

	url = f"{AWI_API_BASE}/metar?ids={icao}&format=json"
	data = await make_awi_request(url)

	return data[0] if data else {'error': f"No METAR data available for {icao}"}

@mcp.tool()
async def get_taf(icao: str) -> dict:
	"""Get TAF information for a specific airport.

	Args:
		icao: 4 letters airport code (e.g. LFLC for Clermont-Ferrand Auvergne Airport)
	"""

	url = f"{AWI_API_BASE}/taf?ids={icao}&format=json"
	data = await make_awi_request(url)

	return data[0] if data else {'error': f"No TAF data available for {icao}"}


# Add a dynamic greeting resource
# @mcp.resource("greeting://{name}")
# def get_greeting(name: str) -> str:
#     """Get a personalized greeting"""
#     return f"Hello, {name}!"

if __name__ == "__main__":
	# Initialize and run the server
	mcp.run(transport='stdio')

