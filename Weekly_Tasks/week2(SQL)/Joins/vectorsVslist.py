import numpy as np
import time

# Create large array
arr = np.random.rand(10000000)

# Without Vectorization (Loop)
start = time.time()
result_loop = []
for i in range(len(arr)):
    result_loop.append(arr[i] * 2)
end = time.time()
loop_time = end - start

# With Vectorization (NumPy)
start = time.time()
result_vec = arr * 2
end = time.time()
vec_time = end - start

# Results
print(f"Loop time: {loop_time * 1000}  seconds")
print(f"Vectorized time: {vec_time *10000} seconds")
# print(f"Speedup: {loop_time / vec_time:.2f}x faster")