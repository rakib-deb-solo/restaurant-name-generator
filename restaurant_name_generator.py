# -------------------------------------------------------
# 🍽️ Restaurant Name Generator
# Author: MD Rakibul Islam
# Description:
# This program randomly generates restaurant name ideas
# based on the user's selected restaurant type (Fast Food,
# Cafe, or Fine Dining). It reads names from text files,
# combines two random words, and displays 5 creative names.
# -------------------------------------------------------

# Import the random module for random word selection
import random

# Import Fore and Style from colorama for colorful terminal output
from colorama import Fore, Style

# -------------------------------------------------------
# STEP 1: Display a colorful welcome message
# -------------------------------------------------------
print(Fore.YELLOW + "Welcome To Restaurant Name Generator!" + Style.RESET_ALL)

# -------------------------------------------------------
# STEP 2: Ask the user which type of restaurant they want
# -------------------------------------------------------
print("\nChoose restaurant type:")
print("1. Fast Food")
print("2. Cafe")
print("3. Fine Dining")

# Take user input
choice = input("Enter your choice (1/2/3): ")

# -------------------------------------------------------
# STEP 3: Load the correct text file based on user choice
# -------------------------------------------------------
# Each text file should contain a list of words related to that restaurant type.
# Example: "Cafe.txt" may contain cozy or artistic names.

if choice == "1":
    # Open Fast Food name list
    with open("Fast Food.txt", "r") as file:
        words = file.read().splitlines()  # Reads all lines into a list
        restaurant_type = "Fast Food"

elif choice == "2":
    # Open Cafe name list
    with open("Cafe.txt", "r") as file:
        words = file.read().splitlines()
        restaurant_type = "Cafe"

elif choice == "3":
    # Open Fine Dining name list
    with open("Fine Dining.txt", "r") as file:
        words = file.read().splitlines()
        restaurant_type = "Fine Dining"

else:
    # If user enters an invalid number
    print("Invalid choice! Please run the program again.")
    exit()  # Exit the program safely

# -------------------------------------------------------
# STEP 4: Generate 5 creative restaurant names
# -------------------------------------------------------

# Print header message in cyan color
print(Fore.CYAN + f"\n🍽️  Here are 5 {restaurant_type} restaurant names:\n" + Style.RESET_ALL)

# Loop 5 times to generate 5 random restaurant names
for i in range(5):
    # Pick 2 random words from the text file list
    word1, word2 = random.sample(words, 2)

    # Combine and capitalize them to create a stylish restaurant name
    restaurant_name = word1.title() + " " + word2.title()

    # Display the generated restaurant name
    print(f"{i + 1}. {restaurant_name}")

# -------------------------------------------------------
# STEP 5: Thank the user and exit
# -------------------------------------------------------
print(Fore.GREEN + "\n✨ Thank you for using Restaurant Name Generator!" + Style.RESET_ALL)
