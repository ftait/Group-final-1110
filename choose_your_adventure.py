def main():
    a = 0

def f1_randomizer():
    b = 1

def f2_the_adversary():
    c = 2

def f3_guess_the_code():
    d = 3

def f4_decode_the_message():
    e = 4

def f5_the_maze():
    f = 5

def f6_combat_system():
    g = 6

def f7_potion_challenge():
    h = 7
    
print("Hello and welcome to this choose your own adventure game!\nIn this game, every decision you make will affect how your story ends, so choose wisely...")
print("Your first decision is the most important. You must choose your character to start the journey.")
choice_0 = input("Type '1' to select the dwarf riding a goat, type '2' to select the wizard raccoon, or type '3' to select the frog.")

while choice_0 not in ["1", "2", "3"]:
    print("Invalid choice. Please try again.")
    choice_0 = input("Type '1' to select the dwarf riding a goat, type '2' to select the wizard raccoon, or type '3' to select the frog.")  

if choice_0 == "1":
    print("Excellent choice! The dwarf riding a goat is a steadfast and reliable hero who will serve you well on your journey.")
    print("Your story begins on a lonely mountain trail, winding through the trees, the scent of adventure in the air.")
    print("Around a sharp corner, you come across a fork in the path. To the left, you see a wide, open valley, striped with flowing streams. To the right, the path continues deeper into the forest, where the trees are dappled with sunlight.")
    choice_1 = input("Type '1' to turn left into the valley, or type '2' to turn right into the forest.")
    if choice_1 == "1":
        print("You ride down into the valley, your goat easily traversing the rocky path. ")

elif choice_0 == "2":
    print("You have chosen the wizard raccoon.")

elif choice_0 == "3":
    print("You have chosen the frog.")

