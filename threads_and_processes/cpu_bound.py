import datetime
import math
import multiprocessing
import threading


def main():
    t0 = datetime.datetime.now()
    cpu_count = multiprocessing.cpu_count()
    # threads = []
    # for n in range(1, cpu_count + 1):
    #     threads.append(
    #         threading.Thread(target=do_math, args=(30_000_000 * (n - 1) / cpu_count, 30_000_000 * n / cpu_count))
    #     )
    # [thread.start() for thread in threads]
    # [thread.join() for thread in threads]
    pool = multiprocessing.Pool()
    tasks = []
    for n in range(1, cpu_count + 1):
        task = pool.apply_async(do_math, args=(30_000_000 * (n - 1) / cpu_count, 30_000_000 * n / cpu_count))
        tasks.append(task)
    pool.close()
    pool.join()

    dt = datetime.datetime.now() - t0
    print(f'Done in {dt.total_seconds()}')
    for t in tasks:
        print(t.get())


def do_math(start=0, num=10):
    pos = start
    k_sq = 1000 * 1000
    ave = 0
    while pos < num:
        pos += 1
        val = math.sqrt((pos - k_sq) * (pos - k_sq))
        ave += val / num
    return int(ave)


if __name__ == '__main__':
    main()
