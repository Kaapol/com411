z = 3
def observed():
  observations = []
  for n in range(z):
    print("Plase enter an observation: ")
    observation = input()
    observations.append(observation)

  return observations

def remove_observations(observations):
  print("Do you wish to remove an observation (yes/no): ")
  if (input() == "yes"):
    observations.remove(observation)


remove_observations()



