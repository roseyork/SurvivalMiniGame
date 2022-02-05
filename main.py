# This is a text based survival game created by Rose York.
# First draft created on 05.02.22.
# You must navigate through a series of options to try and survive the zombie outbreak.

while True:
    answer = input("You are on the 10th floor of your workplace, you hear a scream coming from the hallway. Do you check to see where the noise is coming from? (yes/no) ").lower().strip()

    if answer == "yes":

        answer = input("You head over to the door and peer out of the room and look left. You see people running towards you. Do you run left or right? ")

        if answer == "right":
            answer = input("You begin running right, down the hallway. You have the option to take the elevator or the stairs, which do you choose? ")

            if answer == "elevator":
                print("You reach the elevator and the doors open, out pours a zombie hoard that overpowers you and you die. Game over.")

            else:
                print("You make it to the stairs and begin to run down them. You hear the screams from those who headed towards the elevator above you.")

                answer = input("You continue to run down the stairs to floor 7, however you begin to hear noises from the floor below. Do you continue to head down to floor 6 or exit at floor 7? ")

                if answer == "floor 6":
                    print("You continue to head down to floor 6, right into the mouths of the zombies. Game over.")
                    
                else:
                    print("You exit onto floor 7, there is blood all over the walls but not a zombie in sight. You hide in a storage room and await rescue. Congratulations, you have beaten the game. Please feel free to play again")

        elif answer == "left":
            print("You run left, people run past you fearing for their lives. A strange person staggers towards you, you notice something is up with their eyes. They lunge at you, biting you in the throat. Game over. ")

        else:
            print("You took to long to decide, and you were caught and eaten by zombies.")

    else:
         print("You stay put, and the screaming gets closer. Suddenly a hoard of zombies burst into the room and begin to attack you and your co-workers. You die, getting eaten alive. Game over. ")
         break

# Please look out for future projects at https://github.com/roseyork
