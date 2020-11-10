import os

def search(locations):
  print("Searching...")
  sections = []
  books = []
  with open(locations, "r") as file:
    for line in file:
      if (line.startswith("Section")):
        sections.append(line.split(":", 1)[1].replace("\n",""))
      else:
        books.append(line.replace("\n",""))
  print("Done!")
  data = (sections, books)
  return data

def save(locations, data):
  print("Saving...")
  
  sections = ""
  books = ""

  with open(locations, "w") as file:
    sections+= "Sections: "
    for section in data[0]:
      sections += section +", "
    books += "\nBooks: "
    for book in data[1]:
      books += book +", "

    file.write(sections[:-2])
    file.write(books[:-2])
    print("Done!")

def run():
  data = search("data/files/txt/books.txt")

  save("data/files/txt/sections-books.txt", data)

run()