import multiprocessing
import time
import os

def hog_memory(target_mb):
    """자식 프로세스: 메모리를 무한히 할당함"""
    hogs = []
    try:
        while True:
            hogs.append(' ' * (10**6 * 10))
    except MemoryError:
        pass

if __name__ == "__main__":
    core_count = multiprocessing.cpu_count()
    processes = []

    print("=" * 50)
    print(f"🔥 시스템 과부하 테스트 시작 (CPU 코어: {core_count}개)")
    print("⚠️  주의: 이 코드는 시스템을 강제로 멈추게 할 수 있습니다.")
    print("⚠️  중요한 작업은 모두 저장하고 실행하세요.")
    print("🛑 중단하려면 이 창에서 [Ctrl + C]를 누르세요.")
    print("=" * 50)
    time.sleep(2)

    try:
        for i in range(core_count):
            p = multiprocessing.Process(target=hog_memory, args=(10,))
            p.daemon = True
            p.start()
            processes.append(p)
            print(f"[{i+1}/{core_count}] 프로세스 가동 중... (PID: {p.pid})")

        print("\n🚀 모든 프로세스가 가동되었습니다. 곧 랙이 발생합니다.")

        start_time = time.time()
        while True:
            elapsed = int(time.time() - start_time)
            print(f"\r테스트 진행 중... 경과 시간: {elapsed}초 (상태: 시스템 부하 증가)", end="")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\n🛑 사용자 요청으로 테스트를 중단합니다.")
        print("자원 해제 중... 잠시만 기다려 주세요.")

        for p in processes:
            p.terminate()
            p.join()

        print("✅ 모든 테스트 프로세스가 종료되었습니다. 시스템이 곧 정상화됩니다.")
