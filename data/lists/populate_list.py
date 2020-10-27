def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction: ")
  movement = directions()
  for index in range(len(movement)):
    print("{} : {}.".format(index, movement[index]))
  
  direction_index = int(input())
  
  return movement[direction_index]

def run():
  route = []
  print("Working out escape route...")
  for count in range(5):
    direction = menu()
    route.append(direction)
  print("Escape route: {}".format(route))

run()