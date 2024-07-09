def factorial( n ):
    if n == 0:
        return 1
    else:
        result = ''
        for i in range(1, n + 1):
            result += str(i)
        return result

n = int(input())
    
array = factorial(n)

if n < 2:
    print('n не может быть меньше 2')
else:
    if n == 2:
        m = 2
    else:
        m = n - 1
        
    answer = ''
    i = 0
    while(True):
        answer += array[i:m+i]
        i += m-1
        array += array
        if answer[-1] == '1': 
            break
    print(answer)


