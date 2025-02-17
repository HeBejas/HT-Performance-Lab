import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Неверное количество аргументов")
    else:
        circle_file = sys.argv[1]
        dot_file = sys.argv[2]
        
input_circle = open(circle_file, 'r').readlines()
input_dot = open(dot_file, 'r').readlines()

circleR = int(input_circle[1])
circleY = int(input_circle[0].split()[0])
circleX = int(input_circle[0].split()[1])

for i in range( len(input_dot) ):
    dotX = int(input_dot[i].split()[0])
    dotY = int(input_dot[i].split()[1])

    calc = (circleX - dotX)**2 + (circleY - dotY)**2
    if calc == circleR**2:
        print(0)
        continue
    elif calc < circleR**2:
        print(1)
        continue
    elif calc > circleR**2:
        print(2)
        continue

