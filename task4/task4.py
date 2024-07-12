import statistics
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Неверное количество аргументов')
    else:
        filename = sys.argv[1]

with open(filename, 'r') as file:
    numbers = file.readlines()
    numbers = [number.strip() for number in numbers]

numbers = [int(num) for num in numbers]
  
average = round(statistics.mean(numbers))

answer = sum( abs(average - number ) for number in numbers )

print(answer)
