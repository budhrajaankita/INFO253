from operator import methodcaller
from flask import Flask, jsonify, make_response, request
import json
app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return "This route doesn't exist! {}".format(e)

def checkValidDay(day):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if day.lower() in days:
        return True
    else:
        return False


def writeNewJson(new_quotes):
    updatedData = {}
    updatedData["quotes"] = new_quotes
    with open("quotes.json", "w") as f:
        json.dump(updatedData, f)
    return 


def getAllData():
    try:
        file = open('quotes.json')
        data = json.load(file)
        quotes = data['quotes']
        file.close()
        return quotes
    except:
        return ""

@app.route("/", methods=["GET", "PUT", "DELETE"])
def index():
    try:
        if request.method == "PUT" or request.method == "DELETE":
            return "", 400
        all_quotes = getAllData()
        if all_quotes:
            return make_response(all_quotes, 200)
        else:
            return make_response("", 204)
    except Exception as e:
        return "Unexpected error in index. Details: {}".format(e), 500

    

@app.route("/<day>", methods=["GET"])
def getQuoteByDay(day):
    quotes = getAllData()
    if checkValidDay(day):
        quoteOfTheDay = { k: v for k, v in quotes.items() if k == day.lower() }
        if quoteOfTheDay:
            return jsonify(quoteOfTheDay), 200
        else:
            # Return an error message if the day does not exist in json
            return make_response("", 204)
    else:
        # Return an error message if the day is invalid
        return "", 400


@app.route("/", methods=["POST"])
@app.route("/<day>", methods=["PUT"])
def addQuoteByDay(day=None):
    statusCode = 400
    try:
        json_data = request.get_json()

        if day == None:
            if not json_data:
                return "", 400
            new_day = json_data["day"].lower()
        else:
            new_day = day.lower()
        
        if checkValidDay(new_day):
            quotes = getAllData()
            if new_day.lower() in quotes.keys():
                if request.method == "PUT":
                    statusCode = 200
                elif request.method == "POST":
                    return "", statusCode
            else:
                statusCode = 201

            if not json_data:
                return "",400

            new_quote = request.get_json()["quote"]
            quotes[new_day] = new_quote
            writeNewJson(quotes)
            return jsonify({ new_day: new_quote }), statusCode
        else:
            # Return an error message if the day is invalid
            return "", 400
    except Exception as e:
        return "", 400


@app.route("/<day>", methods=["DELETE"])
def deleteQuoteByDay(day):
    try:
        if checkValidDay(day):
            quotes = getAllData()
            #Delete an entry by day
            if request.method == "DELETE":
                if day.lower() in quotes.keys():
                    del quotes[day.lower()]
                    writeNewJson(quotes)
                    return "", 200
                else:
                    return "", 404
        else:
            # Return an error message if the day is invalid
            return "", 400
    except Exception as e:
        return str(e), 500



if __name__ == '__main__':
    app.run(debug=True)