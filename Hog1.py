import time

memory_hog = []
count = 0

print("⚠️메모리 점유 테스트 시작⚠️\n")

try:
    while True:
        memory_hog.append(' ' * 10**6)
        count += 1

        print(f"\r현재 갉아먹은 메모리: 약 {count} MB", end="")
        time.sleep(0.01)

except KeyboardInterrupt:
    print(f"\n\n🛑 테스트가 중지되었습니다. 최종 할당량: 약 {count} MB")
    memory_hog.clear()
    print("메모리를 성공적으로 비웠습니다.")
