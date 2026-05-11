import time

memory_hog = []
count = 0

print("⚠️ Start ⚠️\n")

try:
    while True:
        memory_hog.append(' ' * 10**6)
        count += 1

        print(f"\rMemory Used: About {count} MB", end="")
        time.sleep(0.01)

except KeyboardInterrupt:
    print(f"\n\n🛑 Stopped. Memory Used: About {count} MB")
    memory_hog.clear()
    print("Cleaned")
