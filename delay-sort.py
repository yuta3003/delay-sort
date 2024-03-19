import threading
import time
from typing import List


def delay_sort(random_array: List[int]) -> List[int]:
    sorted_array = []
    array_lock = threading.Lock()

    def _sleep_and_add(delay: int):
        time.sleep(delay / 100)
        with array_lock:
            sorted_array.append(delay)

    threads = []
    for random_num in random_array:
        thread = threading.Thread(target=_sleep_and_add, args=(random_num,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sorted_array


if __name__ == "__main__":
    import random

    def create_random_array(array_length: int) -> List[int]:
        rand_array = [random.randint(0, 30) for _ in range(array_length)]
        return rand_array

    ARRAY_LENGTH = 10
    random_array = create_random_array(ARRAY_LENGTH)
    print(random_array)

    print("")
    print("")
    print("    Delay-Sort start ")
    print("")
    print("")

    sorted_array = delay_sort(random_array)
    print(sorted_array)
