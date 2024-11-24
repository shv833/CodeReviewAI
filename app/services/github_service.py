import aiohttp


async def fetch_repo_contents(repo_url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(str(repo_url)) as response:
            if response.status != 200:
                raise Exception(f"GitHub API error: {response.status}")
            return await response.json()
