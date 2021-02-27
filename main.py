#ask for the word to be converted

#Nat Alphabet in a nice dictionary
NATO = {"A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray"', "Y": "Yankee"', "Z": "Zulu", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "0": "0"}
wordtoconvert = input("Please put in the word to convert: ").upper()

for x in wordtoconvert:
    print(NATO[x])