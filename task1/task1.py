def factorial( n ):
    if n == 0:
        return 1
    else:
        result = ''
        for i in range(1, n + 1):
            result += str(i)
        return result

n = int(input('Введите n: '))
m = int(input('Введите m: '))    
array = factorial(n)

if n == m:
    print('n не может быть равен m')
if n < 2:
    print('n не может быть меньше 2')
else:
    answer = ''
    i = 0
    while(True):
        step = array[i:m+i]
        answer += step[0]
        i += m-1
        array += array
        if step[-1] == '1': 
            break
    print(answer)

input()


