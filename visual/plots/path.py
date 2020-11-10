import matplotlib.pyplot as plt

def coordinate():
  print("Enter an x value: ", end="")
  x = input()
  print("Enter an y value: ", end="")
  y = input()

  tuple1 = (x, y)
  return tuple1

def path():
  print("Retrieving path...")
  x_values = []
  y_values = []
  i = 0
  while i <= 3:
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
    i +=1
  
  list1 = (x_values, y_values)
  return list1

def run():
  values = path()
  plt.plot(values[0], values[1], "rx--")
  plt.show()
run()