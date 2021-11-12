# print(f"Hello, {input('Enter your name: ')}")

def do_something():
  print("chris")

def sum(A):
  res = 0
  for num in A:
    res += num
  return res

def runner():
  print(f'sum = {sum([1, 2, 3])}')

print(__name__)

if __name__ == '__main__':
  runner()
  do_something()

  #To run go in Shell > python test1.py