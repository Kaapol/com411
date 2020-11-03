import os

def search(locations):
  print("Searching...")

  with open(locations, "r") as file:
    for line in file:
      print("Looked in the {}".format(line).replace("\n",""))

  print("Done!")

def run():
  search("data/files/txt/locations.txt")

run()