import math
import threading

def is_prime(n):
    root = int(math.sqrt(n))
    for i in range(2, root+1):
        if n % i == 0:
            return False
    return True

class CountPrime(threading.Thread):
    def __init__(self, list_num, list_lock, out_lock, output):
        threading.Thread.__init__(self)
        self.__list = list_num # list of numbers from 2 to n
        self.__list_lock = list_lock # lock for list_num
        self.__out_lock = out_lock # lock for output
        self.__output = output # list of prime numbers
        
    def run(self):
        while True:
            self.__list_lock.acquire()
            try:
                n = next(self.__list)
            except StopIteration:
                return
            finally:
                self.__list_lock.release()
            
            if not is_prime(n):
                continue
            
            self.__out_lock.acquire()
            self.__output.append(n)
            self.__out_lock.release()
            
def parallel_primes(n, num_threads=None):
    list_num = (i for i in range(2, n+1))
    list_lock = threading.Lock()
    out_lock = threading.Lock()
    output = []
    threads = []
    
    
            
        
        

