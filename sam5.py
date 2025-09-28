counter = 0
#string = 'hello'
while counter != 10:
    values = [0, 2, 4, 6, 8, 10]
    if counter in values:
        string = 'hello'
        string = string + ' world'
        print(string)
        string = 'hello'
        print(string)
    counter += 1
    
    