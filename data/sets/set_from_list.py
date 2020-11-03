z = 3
def observed():
  observations = []
  for n in range(z):
    print("Plase enter an observation: ")
    observation = input()
    observations.append(observation)

  return observations

def run():
  print("Counting observations")
  observations_set = set()
  observations = observed()
  for observation in observations:
    num_obs = observations.count(observation)
    num_names = count(num_obs)
    observations_set.add((observation, num_obs))
    
  for m in range(num_names):  
    print("{} observed {}".format(observation, num_obs))


run()

  
