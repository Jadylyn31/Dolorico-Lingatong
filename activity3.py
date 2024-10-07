hero = ["lapu-lapu", "magellan", "rizal", "bonifacio"]

users = input("Do you want to remove a hero?")

if users == "yes":
    users = input("What i want to remove:")
    hero.remove(users)
print(hero)