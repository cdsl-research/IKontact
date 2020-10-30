import time

import requests

result = []
print("input your API(Gateway) IP")
ip = input()
print("input request number of try for evaluation. (default=10)")
try_num = input() if input() is None else 10

for i in range(int(try_num)):
    arr = []
    start = time.time()
    response = requests.get(ip)
    response_time = response.elapsed.total_seconds()  # 0.002
    end = time.time()
    process_time = end - start
    arr.append(i)
    arr.append(response_time)
    arr.append(process_time)
    result.append(arr)

print(result)