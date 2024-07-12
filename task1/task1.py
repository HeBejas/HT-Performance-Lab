import sys
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Неверное количество аргументов')
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
  
array = [i for i in range(1, n + 1)]
m -= 1
position = 0
result = '1'

while(True):
    position += m
    step = array[position % n]
    if step == 1:
        break
    else:
        result += str(step)
print(result)
        



