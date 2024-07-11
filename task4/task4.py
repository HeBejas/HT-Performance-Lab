import statistics

filename = input('Введите название файла - ')
with open(filename, 'r') as file:
    numbers = file.readlines()
    numbers = [number.strip() for number in numbers]

numbers = [int(num) for num in numbers]
  
average = round(statistics.mean(numbers))

answer = sum( abs(average - number ) for number in numbers )

print(answer)
