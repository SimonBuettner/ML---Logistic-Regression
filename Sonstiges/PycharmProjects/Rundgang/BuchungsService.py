import csv
import json



with open("Hotel.csv", newline ='') as fileInput:
        fields = ['ID', 'Anzahl_Zimmer', 'QM', 'Preis/Nacht', 'Status']
        csvReader = csv.reader(fileInput)
        frei = []

        for row in csvReader:
            if (row[4] == "frei"):
                frei.append(row)
        # roomsHotel = [zeile for zeile in csvReader]
        dictR = csv.DictReader(frei, fields)
        # jsonausgabe = json.dumps(dictR, indent=4)
       # return jsonausgabe
        print(frei)