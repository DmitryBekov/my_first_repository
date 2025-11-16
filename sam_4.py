class Logger:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(f"Начало {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"Конец {self.func.__name__}")
        return result

class Validator:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not (self.min_val <= result <= self.max_val):
                print(f"Значение {result} вне диапазона [{self.min_val}, {self.max_val}]")
            return result
        return wrapper

@Logger
def calculate(x, y):
    return x * y

@Validator(0, 100)
def process_score(score):
    return score

if __name__ == '__main__':
    calculate(5, 3)
    process_score(85)
    process_score(150)