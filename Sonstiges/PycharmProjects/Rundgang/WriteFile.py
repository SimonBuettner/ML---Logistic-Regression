

userInput = """
ToDo:
1. Schlafen
2. Aufstehen
3. Frühstücken
"""

'''
1. Buchstabe
r = read
w = write
x = write (nur neues Files)
a = append (nur wenn schon existiert)

2. Buchstabe:
t = text
b = binary
'''

# Write:
with open("File1.txt", "wt") as fileOutput:
    fileOutput.write(userInput)

# Read;
with open("File1.txt", "rt") as fileInput:

    while True:
        ausgabe = fileInput.readline()

        if not ausgabe:
            break
        print(ausgabe, end='')
