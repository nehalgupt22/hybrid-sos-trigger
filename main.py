import pandas as pd
import numpy as np

data = pd.read_csv("train1.csv")

print("columns:", data.columns)

# take first 3 columns as x, y, z
x = data.iloc[:, 0]
y = data.iloc[:, 1]
z = data.iloc[:, 2]

# compute magnitude
values = np.sqrt(x**2 + y**2 + z**2).tolist()

threshold = 2
duration_limit = 3
inactivity_threshold = 0.5
inactivity_limit = 5
spike_limit = 5


def detect_duration(data):
    count = 0
    for val in data:
        # check sustained spike
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
        # check low movement after spike
        if val <= inactivity_threshold:
            count += 1
            if count >= inactivity_limit:
                return True
        else:
            count = 0
    return False


def detect_repeated_spikes(data):
    # count spikes overall
    spikes = sum(1 for val in data if val >= threshold)
    return spikes >= spike_limit


def hybrid_detection(data):
    duration_flag = detect_duration(data)
    inactivity_flag = detect_inactivity(data)
    spike_flag = detect_repeated_spikes(data)

    print("\nduration:", duration_flag)
    print("inactivity:", inactivity_flag)
    print("spikes:", spike_flag)

    # final decision
    return (duration_flag and inactivity_flag) or spike_flag


result = hybrid_detection(values)

print("\nfinal result:")
print("SOS triggered 🚨" if result else "all good ✅")
