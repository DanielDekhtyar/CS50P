# Learning Python with CS50
# Math Interpreter
# https://cs50.harvard.edu/python/2022/psets/1/interpreter/

def main():
  math = input("Expression: ")
  x , y , z = math.split()
  if y == "+":
    print(float(x) + float(z))
  elif y == "-":
    print(float(x) - float(z))
  elif y == "*":
    print(float(x) * float(z))
  elif y == "/":
    print(float(x) / float(z))

main()
