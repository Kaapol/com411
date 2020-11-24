def gang():
    print("Loading gang...")
    friends = ["Scooby Doo", "Shaggy Rogers", "Fred Jones", "Daphne Blake", "Velma Dinkley"]
    print(friends)
    print("Done!")
    return friends
gang()

def phrases(friends):
    quotes = {}
    for friend in friends:
        print(f"What does {friend} say?")
        quote = input()
        if friend in quotes:
            quotes[friend].append(quote)
        else:
            quotes[friend] = [quote]
    return quotes    
friends = gang()
quotes = phrases(friends)
print(f"\nPhrases: {quotes}\n")

def save(quotes):
  with open("quotes.txt", "w") as file:
    for friend in quotes:
          file.write("{}: {}\n".format(friend, quotes.get(friend)))
save(quotes) 
print("The file contains...")
file = open("quotes.txt")
print(file.read())
file.close()