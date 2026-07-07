import asyncio  # Provides the event loop and utilities for asynchronous programming
import httpx    # HTTP client library with support for asynchronous requests

# An asynchronous function (coroutine) that fetches a user's details
async def worker(name, user_id):
    print(f"{name} started")

    # Create an asynchronous HTTP client
    async with httpx.AsyncClient(verify=False) as client:
        # Send a GET request and pause here until the server responds.
        # While waiting, the event loop can run other coroutines.
        response = await client.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}"
        )

    # Convert the JSON response into a Python dictionary
    user = response.json()

    # Print the fetched user's name
    print(f"{name} received user: {user['name']}")
    print(f"{name} finished\n")


# Main coroutine that starts multiple workers concurrently
async def main():
    # asyncio.gather() schedules all worker coroutines to run concurrently
    # and waits until all of them have finished.
    await asyncio.gather(
        worker("Worker A", 1),
        worker("Worker B", 2),
        worker("Worker C", 3)
    )


# Start the event loop and execute the main coroutine
asyncio.run(main())