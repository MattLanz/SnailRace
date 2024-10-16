import random
import os 
import time

GREN = '\033[32m'
END = '\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def snail(n1, n2, player1="Snail 1", player2="Snail 2"):
    output = []
    output.append(124*'_')
    output.append((n1 * " " + "    .----.   @   @") + "" + ((100 - n1) * " ") + "|")
    output.append((n1 * " " + "   / .--.  \. \\v/ ") + "" + ((100 - n1) * " ") + "|")
    output.append((n1 * " " + "   | | '\ \ \_/ ) ") + "" + ((100 - n1) * " ") + "|")
    output.append((n1 * " " + " ,-\ `-.' /.'  /  ") + "" + ((100 - n1) * " ") + "|")
    output.append((n1 * " " + "'---`----'----'   ") + "" + ((100 - n1) * " ") + "|")
    output.append((n1 * " " + f"{player1}".center(18)) + "" + ((100 - n1) * " ") + "|")
    output.append(124*'_')
    output.append((n2 * " " + "    .----.   @   @") + "" + ((100 - n2) * " ") + "|")
    output.append((n2 * " " + "   / .--.  \. \\v/ ") + "" + ((100 - n2) * " ") + "|")
    output.append((n2 * " " + "   | | '\ \ \_/ ) ") + "" + ((100 - n2) * " ") + "|")
    output.append((n2 * " " + " ,-\ `-.' /.'  /  ") + "" + ((100 - n2) * " ") + "|")
    output.append((n2 * " " + "'---`----'----'   ") + "" + ((100 - n2) * " ") + "|")
    output.append((n2 * " " + f"{player2}".center(18)) + "" + ((100 - n2) * " ") + "|")
    output.append(124*'_')

    return "\n".join(output)

def main():
    clear()
    print("Welcome to the snail race")
    # print("Enter the name of the first snail:")
    # player1 = input()
    # print("Enter the name of the second snail:")
    # player2 = input()
    # print("Press enter to start the race")
    input()
    time.sleep(3)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO!")

    n1 = 0
    n2 = 0

    while n1 <= 105 and n2 <= 105:
        clear()
        n1 += random.randint(1, 3)
        n2 += random.randint(1, 3)
        output = snail(n1, n2)
        print(output)
        time.sleep(0.1)
        output = []

    if n1 > n2:
        print(f"{GREN}Snail 1 wins!{END}")
    elif n2 > n1:
        print(f"{GREN}Snail 2 wins!{END}")

if __name__ == "__main__":
    main()
