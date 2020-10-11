import multiprocessing
import time

start = time.perf_counter()

def power_nap():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('...yawn....')
    print('...Awake')

# every call of the func. will execute the sleep method within time module
# cpu bound task run synchronously - or one at a time...
# if we were to run the methods on two diff. processors we could have both run concurrently

# here is the synchronous way of running a method twice ...
    # power_nap()
    # power_nap()  # the code will excute twice and sleep for a total of 2 seconds

#  here is an example using the imported multiprocessing module
p1 = multiprocessing.Process(target=power_nap) # p1 as process-1
p2 = multiprocessing.Process(target=power_nap)

p1.start()
p2.start()

# to give the p1,p2 time to finish before the interpeter executes the print() we must use .join()

# p1.join()
# p2.join()

finish = time.perf_counter() # perf_counter() function always returns the float value of time in seconds

print(f'Finished in {round(finish-start, 2)}) seconds(s)')
