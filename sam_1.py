import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\nВремя выполнения: {end - start:.4f} сек")
        return result
    return wrapper

@measure_time
def fibonacci():
    fib1 = fib2 = 1
    print(fib1, fib2, end=' ')
    
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')
        
if __name__ == '__main__':
    fibonacci()