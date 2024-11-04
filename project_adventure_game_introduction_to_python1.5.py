# Title: Adventure Game
# Version: 1.5.1
# Date: October 15, 2024 - November xx, 2024
# 
# Author: Lena Weinstock
# Linter: Paul Jonas Dohle
# Course: Computer Science ICS 3u
# School: Glebe Collegiate Institute, Ottawa
# Teacher: Mr Giassante
# 
# Description: This Python Program creates an immercive adventure
#               located in London. The players goal is to find a fugitive
#               criminal while having the possibility to take the underground
#               and the boat to catch the criminal with the help of so called
#               "passes" the player needs to find. After two travels, the pass
#               is not valid anymore and the player needs to switch it with a
#               new one.


from random import randint

# create blank list with 80 items

Desc = list(range(81))
Objects = list(range(81))
North = list(range(81))
South = list(range(81))
East = list(range(81))
West = list(range(81))
Down = list(range(81))
Up = list(range(81))

Desc[1] = "Paddington Station"
Objects[1] = randint(1,6)
North[1] = 0
South[1] = 0 
East[1] = 0
West[1] = 0
Down[1] = 71
Up[1] = 0

Desc[2] = "Regent's Park"
Objects[2] = randint(1,6)
North[2] = 0
South[2] = 0 
East[2] = 3
West[2] = 0
Down[2] = 0
Up[2] = 0

Desc[3] = "Regent's Park"
Objects[3] = randint(1,6) 
North[3] = 0
South[3] = 13 
East[3] = 0
West[3] = 2
Down[3] = 0
Up[3] = 0

Desc[4] = "Gower Street"
Objects[4] = randint(1,6)
North[4] = 0
South[4] = 14 
East[4] = 5
West[4] = 0
Down[4] = 0
Up[4] = 0

Desc[5] = "Euston Road"
Objects[5] = randint(1,6) 
North[5] = 0
South[5] = 0 
East[5] = 6
West[5] = 4
Down[5] = 0
Up[5] = 0

Desc[6] = "King's Cross Station"
Objects[6] = randint(1,6)
North[6] = 0
South[6] = 0 
East[6] = 0
West[6] = 5
Down[6] = 72
Up[6] = 0

Desc[7] = "Prime Meridian"
Objects[7] = randint(1,6) 
North[7] = 0
South[7] = 0 
East[7] = 8
West[7] = 0
Down[7] = 0
Up[7] = 0

Desc[8] = "Royal Observatorium"
Objects[8] = randint(1,6) 
North[8] = 0
South[8] = 0 
East[8] = 9
West[8] = 7
Down[8] = 0
Up[8] = 0

Desc[9] = "Greenwhich Park"
Objects[9] = randint(1,6) 
North[9] = 0
South[9] = 19 
East[9] = 10
West[9] = 8
Down[9] = 0
Up[9] = 0

Desc[10] = "Greenwhich Park"
Objects[10] = randint(1,6) 
North[10] = 0
South[10] = 0 
East[10] = 0
West[10] = 9
Down[10] = 0
Up[10] = 0

Desc[11] = "Hyde Park"
Objects[11] = randint(1,6) 
North[11] = 0
South[11] = 21 
East[11] = 12
West[11] = 0
Down[11] = 0
Up[11] = 0

Desc[12] = "Brook Street"
Objects[12] = randint(1,6) 
North[12] = 0
South[12] = 22
East[12] = 13
West[12] = 11
Down[12] = 0
Up[12] = 0

Desc[13] = "Regent Street"
Objects[13] = randint(1,6)
North[13] = 3
South[13] = 23 
East[13] = 0
West[13] = 12
Down[13] = 0
Up[13] = 0

Desc[14] = "British Museum"
Objects[14] = randint(1,6) 
North[14] = 4
South[14] = 24 
East[14] = 0
West[14] = 0
Down[14] = 0
Up[14] = 0

Desc[15] = "Queen Victoria Street"
Objects[15] = randint(1,6) 
North[15] = 0
South[15] = 25 
East[15] = 16
West[15] = 0
Down[15] = 0
Up[15] = 0

Desc[16] = "King William Street"
Objects[16] = randint(1,6) 
North[16] = 0
South[16] = 0 
East[16] = 17
West[16] = 15
Down[16] = 0
Up[16] = 0

Desc[17] = "Tower Hill Station"
Objects[17] = randint(1,6) 
North[17] = 0
South[17] = 27 
East[17] = 0
West[17] = 16
Down[17] = 73
Up[17] = 0

Desc[18] = "National Maritim Museum"
Objects[18] = randint(1,6) 
North[18] = 0
South[18] = 0 
East[18] = 19
West[18] = 0
Down[18] = 0
Up[18] = 0

Desc[19] = "King William Walk"
Objects[19] = randint(1,6) 
North[19] = 9
South[19] = 29 
East[19] = 20
West[19] = 18
Down[19] = 0
Up[19] = 0

Desc[20] = "Greenwhich Market"
Objects[20] = randint(1,6) 
North[20] = 0
South[20] = 0 
East[20] = 0
West[20] = 19
Down[20] = 0
Up[20] = 0

Desc[21] = "Hyde Park Corner (Station)"
Objects[21] = randint(1,6)
North[21] = 11
South[21] = 31 
East[21] = 22
West[21] = 0
Down[21] = 74
Up[21] = 0

Desc[22] = "Picadilly Street"
Objects[22] = randint(1,6)
North[22] = 12
South[22] = 32 
East[22] = 23
West[22] = 21
Down[22] = 0
Up[22] = 0

Desc[23] = "Picadilly Circus Station"
Objects[23] = randint(1,6)
North[23] = 13
South[23] = 0 
East[23] = 24
West[23] = 22
Down[23] = 75
Up[23] = 0

Desc[24] = "Shaftesbury Avenue"
Objects[24] = randint(1,6)
North[24] = 14
South[24] = 0 
East[24] = 0
West[24] = 23
Down[24] = 0
Up[24] = 0

Desc[25] = "White Lion Hill"
Objects[25] = randint(1,6) 
North[25] = 15
South[25] = 0 
East[25] = 26
West[25] = 0
Down[25] = 0
Up[25] = 0

Desc[26] = "Upper Thames Street"
Objects[26] = randint(1,6) 
North[26] = 0
South[26] = 0 
East[26] = 27
West[26] = 25
Down[26] = 0
Up[26] = 0

Desc[27] = "Lower Thames Street"
Objects[27] = randint(1,6) 
North[27] = 17
South[27] = 0 
East[27] = 28
West[27] = 26
Down[27] = 0
Up[27] = 0

Desc[28] = "Tower of London"
Objects[28] = randint(1,6) 
North[28] = 0
South[28] = 38 
East[28] = 0
West[28] = 27
Down[28] = 0
Up[28] = 0

Desc[29] = "Greenwhich Pier"
Objects[29] = randint(1,6)
North[29] = 19
South[29] = 50 
East[29] = 30
West[29] = 0
Down[29] = 0
Up[29] = 0

Desc[30] = "Cutty Sark"
Objects[30] = randint(1,6)
North[30] = 0
South[30] = 0 
East[30] = 0
West[30] = 29
Down[30] = 0
Up[30] = 0

Desc[31] = "Constitution Hill (Street)"
Objects[31] = randint(1,6)
North[31] = 21
South[31] = 41
East[31] = 0
West[31] = 0
Down[31] = 0
Up[31] = 0

Desc[32] = "St. James Park"
Objects[32] = randint(1,6)
North[32] = 22
South[32] = 42
East[32] = 0
West[32] = 0
Down[32] = 0
Up[32] = 0

Desc[33] = "White Hall (Street)"
Objects[33] = randint(1,6)
North[33] = 0
South[33] = 43
East[33] = 0
West[33] = 0
Down[33] = 0
Up[33] = 0

Desc[34] = "River"
Objects[34] = " "
North[34] = 0
South[34] = 0 
East[34] = 0
West[34] = 0
Down[34] = 0
Up[34] = 0

Desc[35] = "River"
Objects[35] = " "
North[35] = 0
South[35] = 0 
East[35] = 0
West[35] = 0
Down[35] = 0
Up[35] = 0

Desc[36] = "River"
Objects[36] = " "
North[36] = 0
South[36] = 0 
East[36] = 0
West[36] = 0
Down[36] = 0
Up[36] = 0

Desc[37] = "River"
Objects[37] = " "
North[37] = 0
South[37] = 0 
East[37] = 0
West[37] = 0
Down[37] = 0
Up[37] = 0

Desc[38] = "Tower Bridge"
Objects[38] = randint(1,6)
North[38] = 28
South[38] = 48 
East[38] = 0
West[38] = 0
Down[38] = 0
Up[38] = 0

Desc[39] = "River"
Objects[39] = " "
North[39] = 0
South[39] = 0 
East[39] = 0
West[39] = 0
Down[39] = 0
Up[39] = 0

Desc[40] = "River"
Objects[40] = " "
North[40] = 0
South[40] = 0 
East[40] = 0
West[40] = 0
Down[40] = 0
Up[40] = 0

Desc[41] = "Buckingham Palace"
Objects[41] = randint(1,6)
North[41] = 31
South[41] = 51 
East[41] = 42
West[41] = 0
Down[41] = 0
Up[41] = 0

Desc[42] = "Birdcage Walk"
Objects[42] = randint(1,6)
North[42] = 32
South[42] = 52 
East[42] = 43
West[42] = 41
Down[42] = 0
Up[42] = 0

Desc[43] = "Palace of Westminister"
Objects[43] = randint(1,6) 
North[43] = 33
South[43] = 53 
East[43] = 44
West[43] = 42
Down[43] = 0
Up[43] = 0

Desc[44] = "Westminister Bridge"
Objects[44] = randint(1,6)
North[44] = 0
South[44] = 0 
East[44] = 45
West[44] = 43
Down[44] = 0
Up[44] = 0

Desc[45] = "London Eye"
Objects[45] = randint(1,6)
North[45] = 0
South[45] = 55 
East[45] = 46
West[45] = 44
Down[45] = 0
Up[45] = 0

Desc[46] = "Waterloo Road"
Objects[46] = randint(1,6)
North[46] = 0
South[46] = 56 
East[46] = 0
West[46] = 45
Down[46] = 0
Up[46] = 0

Desc[47] = "Tooley Street"
Objects[47] = randint(1,6)
North[47] = 0
South[47] = 57 
East[47] = 48
West[47] = 0
Down[47] = 0
Up[47] = 0

Desc[48] = "Tower Bridge Road"
Objects[48] = randint(1,6)
North[48] = 38
South[48] = 58 
East[48] = 49
West[48] = 47
Down[48] = 0
Up[48] = 0

Desc[49] = "Tooley Street"
Objects[49] = randint(1,6)
North[49] = 0
South[49] = 0 
East[49] = 0
West[49] = 48
Down[49] = 0
Up[49] = 0

Desc[50] = "City Cruises London Office"
Objects[50] = randint(1,6)
North[50] = 29
South[50] = 60 
East[50] = 0
West[50] = 0
Down[50] = 0
Up[50] = 0

Desc[51] = "Buckingham Gate"
Objects[51] = randint(1,6)
North[51] = 41
South[51] = 61 
East[51] = 52
West[51] = 0
Down[51] = 0
Up[51] = 0

Desc[52] = "St. James Park Station"
Objects[52] = randint(1,6)
North[52] = 42
South[52] = 0 
East[52] = 53
West[52] = 51
Down[52] = 76
Up[52] = 0

Desc[53] = "Tothill Street"
Objects[53] = randint(1,6)
North[53] = 43
South[53] = 0 
East[53] = 0
West[53] = 52
Down[53] = 0
Up[53] = 0

Desc[54] = "River"
Objects[54] = randint(1,6)
North[54] = 0
South[54] = 0 
East[54] = 0
West[54] = 0
Down[54] = 0
Up[54] = 0

Desc[55] = "Westminister Bridge Road "
Objects[55] = randint(1,6)
North[55] = 45
South[55] = 65 
East[55] = 0
West[55] = 0
Down[55] = 0
Up[55] = 0

Desc[56] = "London Road"
Objects[56] = randint(1,6)
North[56] = 46
South[56] = 66
East[56] = 0
West[56] = 0
Down[56] = 0
Up[56] = 0

Desc[57] = "Abbey Street"
Objects[57] = randint(1,6)
North[57] = 47
South[57] = 0 
East[57] = 58
West[57] = 0
Down[57] = 0
Up[57] = 0

Desc[58] = "Tower Bridge Road"
Objects[58] = randint(1,6)
North[58] = 48
South[58] = 68 
East[58] = 59
West[58] = 57
Down[58] = 0
Up[58] = 0

Desc[59] = "Abbey Street"
Objects[59] = randint(1,6)
North[59] = 0
South[59] = 0 
East[59] = 60
West[59] = 58
Down[59] = 0
Up[59] = 0

Desc[60] = "Abbey Street"
Objects[60] = randint(1,6)
North[60] = 50
South[60] = 0 
East[60] = 0
West[60] = 59
Down[60] = 0
Up[60] = 0

Desc[61] = "Victoria Street"
Objects[61] = randint(1,6)
North[61] = 51
South[61] = 0 
East[61] = 62
West[61] = 0
Down[61] = 0
Up[61] = 0

Desc[62] = "Victoria Street"
Objects[62] = randint(1,6)
North[62] = 0
South[62] = 0 
East[62] = 63
West[62] = 61
Down[62] = 0
Up[62] = 0

Desc[63] = "Victoria Street"
Objects[63] = randint(1,6)
North[63] = 43
South[63] = 0 
East[63] = 0
West[63] = 62
Down[63] = 0
Up[63] = 0

Desc[64] = "River"
Objects[64] = " "
North[64] = 0
South[64] = 0 
East[64] = 0
West[64] = 0
Down[64] = 0
Up[64] = 0

Desc[65] = "Kennington Road"
Objects[65] = randint(1,6)
North[65] = 55
South[65] = 0 
East[65] = 66
West[65] = 0
Down[65] = 0
Up[65] = 0

Desc[66] = "Kennington Station"
Objects[66] = randint(1,6)
North[66] = 56
South[66] = 0 
East[66] = 67
West[66] = 65
Down[66] = 77
Up[66] = 0

Desc[67] = "New Kent Road"
Objects[67] = randint(1,6) 
North[67] = 0
South[67] = 0 
East[67] = 68
West[67] = 66
Down[67] = 0
Up[67] = 0

Desc[68] = "Tower Bridge Road"
Objects[68] = randint(1,6) 
North[68] = 58
South[68] = 0 
East[68] = 69
West[68] = 67
Down[68] = 0
Up[68] = 0

Desc[69] = "New Cross Road"
Objects[69] = randint(1,6)
North[69] = 0
South[69] = 0 
East[69] = 70
West[69] = 68
Down[69] = 0
Up[69] = 0

Desc[70] = "New Cross Road"
Objects[70] = randint(1,6)
North[70] = 0
South[70] = 80 
East[70] = 0
West[70] = 69
Down[70] = 0
Up[70] = 0

Desc[71] = "Paddington Station (underground)"
Objects[71] = " "
North[71] = 72
South[71] = 78 
East[71] = 75
West[71] = 0
Down[71] = 0
Up[71] = 1

Desc[72] = "King's Cross Station (underground)"
Objects[72] = " "
North[72] = 73
South[72] = 78 
East[72] = 74
West[72] = 76
Down[72] = 0
Up[72] = 6

Desc[73] = "Tower Hill Station (underground)"
Objects[73] = " "
North[73] = 72
South[73] = 0 
East[73] = 0
West[73] = 71
Down[73] = 0
Up[73] = 17

Desc[74] = "Hyde Park Corner Station (underground)"
Objects[74] = " " 
North[74] = 72
South[74] = 0 
East[74] = 75
West[74] = 0
Down[74] = 0
Up[74] = 21

Desc[75] = "Picadilly Circus Station (underground)"
Objects[75] = " "
North[75] = 71
South[75] = 78 
East[75] = 72
West[75] = 74
Down[75] = 0
Up[75] = 23

Desc[76] = "St. James Park Station (underground)"
Objects[76] = " "
North[76] = 72
South[76] = 0 
East[76] = 73
West[76] = 0
Down[76] = 0
Up[76] = 52

Desc[77] = "Kennington Station (underground)"
Objects[77] = " "
North[77] = 72
South[77] = 0 
East[77] = 78
West[77] = 0
Down[77] = 0
Up[77] = 66

Desc[78] = "Elefant & Castle Station (underground)"
Objects[78] = " "
North[78] = 71
South[78] = 0 
East[78] = 0
West[78] = 77
Down[78] = 0
Up[78] = 79

Desc[79] = "Elefant & Castle Station"
Objects[79] = randint(1,6)
North[79] = 0
South[79] = 0 
East[79] = 80
West[79] = 0
Down[79] = 78
Up[79] = 0

Desc[80] = "Old Kent Road"
Objects[80] = randint(1,6)
North[80] = 70
South[80] = 0 
East[80] = 0
West[80] = 79
Down[80] = 0
Up[80] = 0


# setting beginning variables of payer and computer

position = 0 # position at beginning
while position == 0 or position == 1 or position == 7 or position == 8 or position == 9 or position == 10 or position == 18 or position == 19 or position == 20 or position == 29 or position == 30 or position == 34 or position == 35 or position == 36 or position == 37 or position == 38 or position == 39 or position == 40 or position == 54 or position == 64 or position == 71 or position == 72 or position == 73 or position == 74 or position == 75 or position == 76 or position == 77 or position == 78:
    position = randint(1,81)


pos_com = 0 # position of computer

while pos_com == 0 or pos_com == position or pos_com == 34 or pos_com == 35 or pos_com == 36 or pos_com == 37 or pos_com == 38 or pos_com == 39 or pos_com == 40 or pos_com == 54 or pos_com == 64 or pos_com == 71 or pos_com == 72 or pos_com == 73 or pos_com == 74 or pos_com == 75 or pos_com == 76 or pos_com == 77 or pos_com == 78:
    pos_com = randint(1,81)
    while pos_com + 2 == position or pos_com - 2 == position:
        pos_com = randint(1,81)
    while pos_com + 20 == position or pos_com -20 == position:
        pos_com = randint(1,81)

# defining some variables for later
quitting = False
command = " "
boat_or_train = 0
inhand = " "
transition = " "
moves = 0



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


while quitting == False:
    while command != "N" and command != "S" and command != "W" and command != "E" and command != "U" and command != "D" and command != "X" and command != "P" and command != "K" and command != "Q" :     
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
        print(" ")

        # where am I + thief
        print(" ")
        print("You are in/on/at " + Desc[position] + ".")
        print(" ")
        print("The thief is in/on/at " + Desc[pos_com] + ".")
        print(" ")

        # position directions and options

        if North[position] != 0:
            print("You can go North to " + Desc[North[position]] + ".")
            print(" ")
        else:
            print("You cannot go North.")
            print(" ")
        if South[position] != 0:
            print("You can go South to " + Desc[South[position]] + ".")
            print(" ")
        else:
            print("You cannot go South.")
            print(" ")
        if East[position] != 0:
            print("You can go East to " + Desc[East[position]] + ".")
            print(" ")
        else:
            print("You cannot go East.")
            print(" ")
        if West[position] != 0:
            print("You can go West to " + Desc[West[position]] + ".")
            print(" ")
            print(" ")
        else:
            print("You cannot go West.")
            print(" ")
            print(" ")
        if Down[position] != 0:
            print("You can go down to " + Desc[Down[position]] + ".")
            print(" ")
            print(" ")
        else:
            print("There is no (other) underground station here.")
            print(" ")
            
        if Up[position] != 0:
            print("You can go up to " + Desc[Up[position]] + ".")
            print(" ")
            print(" ")
        else:
            print("You are currently not in an underground station.")
            print(" ")
            print(" ")

        second_digit_com = 0

        # Explain where the thief is: 
        pos_com_str = str(pos_com)
        pos_com_list = list(pos_com_str)

        position_str = str(position)
        position_list = list(position_str)

        if pos_com < 10:
            pos_com_list = [0] + pos_com_list
        if position < 10:
            position_list = [0] + position_list


        first_digit_com = int(pos_com_list[0])
        second_digit_com = int(pos_com_list[1])

        first_digit_player = int(position_list[0])
        second_digit_player = int(position_list[1])

        if pos_com == position:
            print(" ")
            print(" ")
            print("Congratulations! You have successfully caught the thief!")
            print("Good job!")
            print(" ")
            exit()

        if first_digit_player < first_digit_com:
            print("The thief is more in the South.")
            print(" ")
        elif first_digit_player > first_digit_com:
            print("The thief is more in the North.")
            print(" ")        
        elif first_digit_player == first_digit_com:
            print("The thief is on the same height as you. You are close, try to go West or East.")
            print(" ")


        if second_digit_player > second_digit_com:
            print("The thief is more in the West.")
            print(" ")
            print(" ")
        elif second_digit_player < second_digit_com:
            print("The thief is more in the East.")
            print(" ")
            print(" ")
        elif second_digit_player == second_digit_com:
            print("The thief is on the same height as you. You are close, try to go North or South.")
            print(" ")
            print(" ")

        # random object

        if Objects[position] == 5:
            str(Objects[position])
            boat_or_train = randint(1,4)
            if boat_or_train == 1:
                Objects[position] = "boat-ticket"
            else:
                Objects[position] = "underground-ticket"
        elif Objects[position] != 5:
            str(Objects[position])
            Objects[position] = " "

       
        # inventary
        if inhand == " ":
            print("You have currently nothing in your hand.")
            print(" ")
            print(" ")
        else:
            print("You are currently in possession of a/an " + inhand + ".")
            print(" ")
            print(" ")

        # Objects

        if Objects[position] == ("underground-ticket" or Objects[position] == "boat-ticket") and inhand == " ":
            print("You can pick-up the: " + Objects[position] + " ")
            print(" ")
        elif Objects[position] == ("underground-ticket" or Objects[position] == "boat-ticket") and inhand != " ":
            print("You can switch the: " + inhand + " with a/an " + Objects[position] + ".")
            print(" ")


        # Choice after information
        command = input("select a command out of the list above: ")
        print(" ")

        ### Validity boat tickets


        if inhand == "Used_once_boat-ticket":
            if position == 29 and command != "S":
                inhand = inhand
            if position == 50 and command != "N":
                inhand = inhand
            if position == 50 and command == "N":
                inhand = " "
            elif position == 29 and command == "S":
                inhand = " "
        

        if inhand == "boat-ticket":
            if position == 29 and command != "S":
                inhand = inhand
            if position == 50 and command != "N":
                inhand = inhand        
            elif position == 29 and command == "S":
                inhand = "Used_once_boat-ticket"
            elif position == 50 and command == "N":
                inhand = "Used_once_boat-ticket"
        

        # atempt nr. 3 validity of tickets
            
        if inhand == "Used_once_underground-ticket":
            if position == 71 and (command == "N" or command == "S" or command == "E"):
                inhand = " "
            if position == 72 and (command == "N" or command == "S" or command == "E" or command == "W"):
                inhand = " "
            if position == 73 and (command == "N" or command == "W"):
                inhand = " "
            if position == 74 and (command == "N" or command == "E"):
                inhand = " "
            if position == 75 and (command == "N" or command == "S" or command == "E" or command == "W"):
                inhand = " "
            if position == 76 and (command == "N" or command == "E"):
                inhand = " "
            if position == 77 and (command == "N" or command == "E"):
                inhand = " "
            if position == 78 and (command == "N" or command == "W"):
                inhand = " "
            
        if inhand == "underground-ticket":
            if position == 71 and (command == "N" or command == "S" or command == "E"):
                inhand = "Used_once_underground-ticket"
            elif position == 72 and (command == "N" or command == "S" or command == "E" or command == "W"):
                inhand = "Used_once_underground-ticket" 
            elif position == 73 and (command == "N" or command == "W"):
                inhand = "Used_once_underground-ticket"
            elif position == 74 and (command == "N" or command == "E"):
                inhand = "Used_once_underground-ticket"
            elif position == 75 and (command == "N" or command == "S" or command == "E" or command == "W"):
                inhand = "Used_once_underground-ticket"
            elif position == 76 and (command == "N" or command == "E"):
                inhand = "Used_once_underground-ticket"
            elif position == 77 and (command == "N" or command == "E"):
                inhand = "Used_once_underground-ticket"
            elif position == 78 and (command == "N" or command == "W"):
                inhand = "Used_once_underground-ticket"
            
            

        # What happens with selected command:

        if command == "N" and North[position] != 0:
            position = North[position]

        elif command == "S" and South[position] != 0:
            position = South[position]

        elif command == "W" and West[position] != 0:
            position = West[position]

        elif command == "E" and East[position] != 0:
            position = East[position]

        elif command == "U" and Up[position] != 0:
            position = Up[position]

        elif command == "D" and Down[position] != 0:
            position = Down[position]

        elif command == "X" and inhand != " " and Objects[position] == " ":
            Objects[position] = inhand
            inhand = " "

        elif command == "P" and inhand == " " and Objects[position] != " ":
            inhand = Objects[position]
            Objects[position] = " "

        elif command == "K" and inhand != " " and Objects[position] != " ":
            transition = inhand
            inhand = Objects[position]
            Objects[position] = transition

        elif command == "Q":
            print(" ")
            print("Good bye! I hope you had fun playing this game!")
            print(" ")
            exit()
        
        else:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("This command is not possible in/on/at " + Desc[position] + "." + " Please try again")



        

        # fix problem with free rides underground and boat

        if position == 71 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 1
        elif position == 72 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 6
        elif position == 73 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 17
        elif position == 74 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 21
        elif position == 75 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 23
        elif position == 76 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 52
        elif position == 77 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 66
        elif position == 78 and inhand != "underground-ticket" and inhand != "Used_once_underground-ticket":
            print(" ")
            print("You cannot take the underground without a valid ticket.")
            print("Please try again.")
            print(" ")
            position = 79
        elif position == 50 and inhand != "boat-ticket" and inhand != "Used_once_boat-ticket":
            print(" ")
            print("You cannot take the boat without a valid ticket.")
            print("Please try again.")
            print(" ")
        elif position == 29 and inhand != "boat-ticket" and inhand != "Used_once_boat-ticket":
            print(" ")
            print("You cannot take the boat without a valid ticket.")
            print("Please try again.")
            print(" ")
            
        
        # thief position(pos_com)
        moves += 1
        
        # emptying command for while loop
        command = " "


        if moves == 3:
            pos_com_random = randint(1,5)
            if pos_com_random == 1 and West[pos_com] != 0:
                pos_com -= 1
                moves = 0
            elif pos_com_random == 2 and pos_com == 50:
                pos_com = 29
                moves = 0
            elif pos_com_random == 2 and North[pos_com] != 0:
                pos_com -= 10
                moves = 0
            elif pos_com_random == 3 and East[pos_com] != 0:
                pos_com += 1
                moves = 0
            elif pos_com_random == 3 and pos_com == 29:
                pos_com = 50
                moves = 0
            elif pos_com_random == 4 and South[pos_com] != 0:
                pos_com += 10
                moves = 0

            elif pos_com_random == 1 and West[pos_com] == 0:
                break
            elif pos_com_random == 2 and North[pos_com] == 0:
                break
            elif pos_com_random == 3 and East[pos_com] == 0:
                break
            elif pos_com_random == 4 and South[pos_com] == 0:
                break
            
        
       
