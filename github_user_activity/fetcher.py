import asyncio
from typing import Optional

import httpx


async def get_user_data_async(username: str) -> Optional[httpx.Response]:
    async with httpx.AsyncClient() as client:
        try:
            result = await client.get(f"https://api.github.com/users/{username}/events")
            result.raise_for_status()
            return result.json()
        except httpx.HTTPError as e:
            print(f"An error ocurred: {e}")
            return None


def get_user_data(username: str) -> Optional[httpx.Response]:
    with httpx.Client() as client:
        try:
            result = client.get(f"https://api.github.com/users/{username}/events")
            result.raise_for_status()
            return result.json()
        except httpx.HTTPError as e:
            print(f"An error ocurred: {e}")
            return None


if __name__ == "__main__":
    name = input()
    user_data = asyncio.run(get_user_data_async(name))
    print(user_data)
