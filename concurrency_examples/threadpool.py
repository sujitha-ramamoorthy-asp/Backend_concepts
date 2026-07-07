from concurrent.futures import ThreadPoolExecutor
import requests


# Function executed by a thread from the thread pool
def worker(user_id):
    print(f"Task {user_id} started")

    # I/O Operation: Send an HTTP GET request
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
        verify=False
    )

    # Convert JSON response to a Python dictionary
    user = response.json()

    print(f"Task {user_id} received user: {user['name']}")
    print(f"Task {user_id} finished")

    # Return the user's name
    return user["name"]


# Create a thread pool with only 3 worker threads
with ThreadPoolExecutor(max_workers=3) as executor:

    # Submit 5 tasks to the thread pool
    futures = [
        executor.submit(worker, i)
        for i in range(1, 6)
    ]

    print("\nReturned Results:")

    # Wait for each task to complete and print its return value
    for future in futures:
        print(future.result())