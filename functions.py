def greeting() -> None:
    print("""
   ____         __  __             __  __  __            __
  / __/______  / /_/ /__ ____  ___/ /  \ \/ /__ ________/ /
 _\ \/ __/ _ \/ __/ / _ `/ _ \/ _  /    \  / _ `/ __/ _  / 
/___/\__/\___/\__/_/\_,_/_//_/\_,_/     /_/\_,_/_/  \_,_/  
                                                           
""")
   
    print("Let's play a game!")
    print("You are a detective in London.")
    print("The goal is to find the criminal.")
    print("You will be able to find tickets to use the underground and even the boat,")
    print("but be careful! The tickets are only valid two times.")
    print("Have fun!")

def command_help() -> None:
        print(" ")
        print(" ")
        print("[N] to go north")
        print("[S] to go south")
        print("[W] to go west")
        print("[E] to go est")
        print("[U] to go up(underground)")
        print("[D] to go down(underground)")
        print("[X] to drop the item in that place (You will not find it there again)")
        print("[P] to pick up the item in that place")
        print("[K] to switch the item you have with the item in that place")
        print("[Q] to quit the game")
        print("[H] to show this help again")
        print(" ")