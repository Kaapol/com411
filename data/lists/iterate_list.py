def directions():
  directions= ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction: ")
  movement = directions()
  for index in range(len(movement)):
    print("{} : {}.".format(index, movement[index]))
  

def run():
  menu()

run()