import threading
import requests
import certifi

# Function executed by each thread
def worker(name, user_id):
    print(f"{name} started")

    # I/O operation (HTTP request)
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
        verify=False
    )

    user = response.json()

    print(f"{name} received user: {user['name']}")
    print(f"{name} finished")


# Create two threads
t1 = threading.Thread(target=worker, args=("Thread-1", 1))
t2 = threading.Thread(target=worker, args=("Thread-2", 2))

# Start both threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Done")