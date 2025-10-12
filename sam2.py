

def best_result(arr):
    sorted_arr = sorted(arr)
    best_three = sorted_arr[:3]
    worst_three = sorted_arr[-3:]
    from_10 = [r for r in sorted_arr if r >= 10]
    print(best_three)
    print(worst_three)
    print(from_10)
    
    
    
if __name__ == '__main__':
    best_result([10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
           27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4])