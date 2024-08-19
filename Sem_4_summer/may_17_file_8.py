# *******************************************************************
# Python multiprocessing
# *******************************************************************
import time
# multiprocessing - running tasks in parallel in different CPU cores, bypasses GIL used for threading
#                   multiprocessing - better for CPU bound tasks (heavy CPU usage)
#                   multithreading - better for IO bound tasks (waiting around)

from multiprocessing import Process, cpu_count


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())
    a = Process(target=counter, args=(62500000,))
    b = Process(target=counter, args=(62500000,))
    c = Process(target=counter, args=(62500000,))
    d = Process(target=counter, args=(62500000,))
    e = Process(target=counter, args=(62500000,))
    f = Process(target=counter, args=(62500000,))
    g = Process(target=counter, args=(62500000,))
    h = Process(target=counter, args=(62500000,))
    i = Process(target=counter, args=(62500000,))
    j = Process(target=counter, args=(62500000,))
    k = Process(target=counter, args=(62500000,))
    l = Process(target=counter, args=(62500000,))
    m = Process(target=counter, args=(62500000,))
    n = Process(target=counter, args=(62500000,))
    o = Process(target=counter, args=(62500000,))
    p = Process(target=counter, args=(62500000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    i.start()
    j.start()
    k.start()
    l.start()
    m.start()
    n.start()
    o.start()
    p.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    i.join()
    j.join()
    k.join()
    l.join()
    m.join()
    n.join()
    o.join()
    p.join()


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    print("It took " + str(time.perf_counter() - start) + " sec to count to a total of Billion for 16 processes")
