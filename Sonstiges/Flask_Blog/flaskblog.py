from flask import Flask
import json
import csv
import html

app = Flask(__name__)

@app.route('/all')
def all():
     with open("hotel.csv", "rt") as fileInput:
            fields = ['ID', 'Anzahl_Zimmer', 'QM', 'Preis/Nacht', 'Status']
            csvReader = csv.DictReader(fileInput, fields)
            roomsHotel = [zeile for zeile in csvReader]
            jsonAusgabe = json.dumps(roomsHotel, indent=4)
     return jsonAusgabe

@app.route('/free')
def free():

    with open("hotel.csv", newline ='') as fileInputFrei:
        csvReaderFrei = csv.reader(fileInputFrei)
        frei = []
        for row in csvReaderFrei:
            if (row[4] == "frei"):
                frei.append(row)
        
        jsonausgabeFrei = json.dumps(frei, indent=4)
        return jsonausgabeFrei

@app.route('/booked')
def booked():

    with open("hotel.csv", newline ='') as fileInputFrei:
        csvReaderGeb = csv.reader(fileInputFrei)
        gebucht = []
        for row in csvReaderGeb:
            if (row[4] == "gebucht"):
                gebucht.append(row)
        
        jsonausgabeGeb = json.dumps(gebucht, indent=4)
        return jsonausgabeGeb

@app.route('/book/<string:roomID>')
def bookID(roomID):

    with open("hotel.csv", newline ='') as fileInputBook:
        csvReaderBook = csv.reader(fileInputBook)
        book = []
        for row in csvReaderBook:
            if (row[0] == roomID):
                row[4] = "gebucht"
                book.append(row)
                  
        jsonausgabeBook = json.dumps(book, indent=4)
        return jsonausgabeBook

@app.route('/unBook/<string:roomID>')
def unBookID(roomID):

    with open("hotel.csv", newline ='') as fileInputUnBook:
        csvReaderUnBook = csv.reader(fileInputUnBook)
        unBook = []
        for row in csvReaderUnBook:
            if (row[0] == roomID):
                row[4] = "frei"
                unBook.append(row)
                  
        jsonausgabeBook = json.dumps(unBook, indent=4)
        return jsonausgabeBook

if __name__ == '__main__':
	app.run(debug=True)