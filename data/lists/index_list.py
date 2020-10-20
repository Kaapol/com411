def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  directions = movements()
  print("{} for {} steps".format(directions[0], directions[1]))
  print("{} for {} steps".format(directions[2], directions[3]))
  print("{} for {} steps".format(directions[4], directions[5]))
  print("{} for {} steps".format(directions[6], directions[7]))

run()