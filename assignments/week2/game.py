import time

print("🐾 Welcome to the Pet Shelter! 🐾")
name = input("What is your name? ")
print("Hello, " + name + "! Let's help you adopt a pet today.")
time.sleep(1)
pet = input("Which pet would you like to adopt? (dog/cat) ").lower()
if pet == "dog":
 print("Great! Dogs are loyal and fun.")
elif pet == "cat":
    print("Nice! Cats are independent and cute.")
else:
    print("Hmm, we only have dogs or cats right now.")

toy = input("What toy will you give your pet? (ball/string) ").lower()

if toy == "ball":
    print("Classic choice. Your pet is excited!")
elif toy == "string":
    print("Toys are ready for playtime!")
else:
    print("Your pet looks confused...")

food = input("What food will you give your pet? (fish/bone) ").lower()

if pet == "cat" and food == "fish":
    print("Your cat is purring. They love it! 🐱")
elif pet == "dog" and food == "bone":
    print("Your dog is tail-wagging happy! 🐶")
else:
    print("Your pet nibbles, but doesn't seem too happy.")

while True:
    level = input("On a scale of 1 to 10, how excited are you? ")
    if level.isdigit():
        level = int(level)
        if 1 <= level <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    else:
        print("That's not a number.")

time.sleep(1)

activity = input("Do you want to walk or cuddle your pet? ").lower()

if activity == "walk":
    print("You go outside. Your pet enjoys the fresh air.")
elif activity == "cuddle":
    print("You both feel warm and safe. So sweet.")
else:
    print("You just sit quietly. Your pet stares at you.")

if level >= 8:
    print("You and your pet are a perfect match!")
elif level >= 5:
    print("You're both still getting to know each other.")
else:
    print("Maybe you're more of a plant person.")

print("Thanks for playing, " + name + "!")


