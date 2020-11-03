def cwd():
  import os
  path = os.getcwd()
  print(f"Current Working Folder Path: {path}")
  print("The folder contains following: ")
  for file in os.listdir(path):
    print(file)

cwd()