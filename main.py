# Hybrid SOS Trigger Analysis System
# Threshold + Minimum Duration Detection


walking = [900, 1000, 950, 1020, 980, 1010]
running = [4000, 6000, 7000, 6500, 7200]
jumping = [1000, 16000, 900, 1100]
fall = [1000, 2000, 18000, 19000, 17000, 400]
struggle = [15000, 16000, 14000, 15500, 13000]

def threshold_duration_detection(data, threshold, min_duration):
    count = 0
    for value in data:
        if value >= threshold:
            count += 1
            if count >= min_duration:
                return True
        else:
            count = 0
    return False


print("Hybrid SOS Trigger Analysis System")

threshold = int(input("Enter Threshold Value: "))
min_duration = int(input("Enter Minimum Duration (consecutive readings): "))

datasets = {
    "Walking": walking,
    "Running": running,
    "Jumping": jumping,
    "Fall": fall,
    "Struggle": struggle
}

for name, data in datasets.items():
    result = threshold_duration_detection(data, threshold, min_duration)
    print(name, "-> SOS Triggered:", result)
