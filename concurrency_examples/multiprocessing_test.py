from multiprocessing import Process


# CPU-intensive function
def worker(name, start, end):
    print(f"{name} started")

    total = 0

    # Perform a heavy computation
    for i in range(start, end):
        total += i * i

    print(f"{name} finished")
    print(f"{name} Result = {total}\n")


if __name__ == "__main__":

    p1 = Process(target=worker, args=("Process-1", 1, 5_000_000))
    p2 = Process(target=worker, args=("Process-2", 5_000_001, 10_000_000))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")