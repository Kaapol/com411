print("Program started") 
print("Please enter a standard character: ") 
character = str(input()) 
if (len(character) == 1):   
  print(" The ASCII code for {} is {}".format(character,   ord(character)))   
else:     
  print("Enter a singular Character") 
  print("Program Ended")