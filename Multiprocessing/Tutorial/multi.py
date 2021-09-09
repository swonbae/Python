import time
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, as_completed


def do_something(seconds=1):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

def non_multi(seconds):
    for sec in seconds:
        print(do_something(sec))

def multi(seconds):
    # processes = []
    # for sec in seconds:
    #     p = multiprocessing.Process(target=do_something, args=[sec])
    #     p.start()
    #     processes.append(p)
    # for process in processes:
    #     process.join()

    with multiprocessing.Pool() as pool:
        print(pool.map(do_something, seconds))          # returns results in the order that they were started
    
def concur(seconds):
    with ThreadPoolExecutor() as executor:
        # results = [executor.submit(do_something, sec) for sec in seconds]
        # for f in as_completed(results):               # returns results in the order that they were finished
        #     print(f.result())

        results = executor.map(do_something, seconds)   # returns results in the order that they were started
        for result in results:
            print(result)


if __name__ == '__main__':
    start = time.perf_counter()

    seconds = [5, 4, 3, 2, 1]

    # non_multi(seconds)    # slowest (around 15 secs)
    # multi(seconds)        # (around 10 secs)
    concur(seconds)       # fastest (around 5 secs)

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
