import os
import matplotlib.pyplot as plt

def read_data(path_name):
  data = []
  with open(path_name, "r") as file:
    for line in file:
      data.append(line)
    return data
  
def run():
  data = read_data("visual/subplots/temps.txt")
  fig, axes = plt.subplots(2,2)
  axes[0,0].plot(data)
  axes[1,1].plot(data)
  plt.show()
run()