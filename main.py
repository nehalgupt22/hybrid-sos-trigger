import pandas as pd
import numpy as np
import random
import time

data = pd.read_csv("train1.csv", low_memory=False)
data = data.iloc[:, :3]
data = data.apply(pd.to_numeric, errors='coerce').dropna()

if data.empty:
    print("Error: dataset empty")
    exit()

x = data.iloc[:, 0]
y = data.iloc[:, 1]
z = data.iloc[:, 2]

values = np.sqrt(x**2 + y**2 + z**2).tolist()

print("min:", min(values))
print("max:", max(values))

threshold = max(values) * 0.9
duration_limit = 3
inactivity_threshold = min(values) * 1.2
inactivity_limit = 3


def detect_duration(data):
    count = 0
    for val in data:
        if val >= threshold:
            count += 1
            if count >= duration_limit:
                return True
        else:
            count = 0
    return False


def detect_inactivity(data):
    count = 0
    for val in data:
        if val <= inactivity_threshold:
            count += 1
            if count >= inactivity_limit:
                return True
        else:
            count = 0
    return False


if random.random() < 0.5:
    spike_index = random.randint(0, len(values) - 6)
    values[spike_index] = max(values) * 1.5
    values[spike_index + 1] = max(values) * 1.6
    values[spike_index + 2] = max(values) * 1.4
    values[spike_index + 3] = min(values)
    values[spike_index + 4] = min(values)


start = random.randint(0, len(values) - 50)
window = values[start:start + 50]

print("\nreading values:")

for i, val in enumerate(window[:20]):
    print(f"value {i+1}: {val:.3f}")
    time.sleep(0.05)


duration_flag = detect_duration(window)
inactivity_flag = detect_inactivity(window)

print("\nduration:", duration_flag)
print("inactivity:", inactivity_flag)

result = duration_flag and inactivity_flag

print("\nfinal result:")
print("SOS triggered" if result else "all good ")
