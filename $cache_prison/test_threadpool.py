from concurrent.futures import ThreadPoolExecutor


def task(n):
    print(f"task({n})")
    return n

executor = ThreadPoolExecutor(max_workers=5)

futures = []
for i in range(6):
    futures.append(executor.submit(task, i))

for future in futures:
    print(future.result())

# :: 쓰레드 풀 종료?
executor.shutdown()