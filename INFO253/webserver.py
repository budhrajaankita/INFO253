from flask import Flask
app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return "This route doesn't exist! {}".format(e)


#Function accepts two numbers (both int and float) as url parameters and displays the result after adding them
@app.route('/add/<string:num1>/<string:num2>', methods=['GET'])
def add(num1, num2):
    try:
        temp_num1 = float(num1)
        temp_num2 = float(num2)

        if temp_num1.is_integer():
            if not isinstance(temp_num1, float):
                temp_num1 = int(num1)
                
        if temp_num2.is_integer():
            if not isinstance(temp_num2, float):
                temp_num2 = int(num2)

        return str(temp_num1 + temp_num2)

    except ValueError as v:
        return "Invalid or non-numeric parameters : {} or {}. Error : {}".format(num1, num2, v), 400
    except Exception as e:
        return "Unexpected error. Details: {}".format(e), 500


#Function accepts two numbers (both int and float) as url parameters and displays the result after subtracting them
@app.route('/sub/<string:num1>/<string:num2>', methods=['GET'])
def sub(num1, num2):
    try:
        temp_num1 = float(num1)
        temp_num2 = float(num2)

        if temp_num1.is_integer():
            if not isinstance(temp_num1, float):
                temp_num1 = int(num1)
                
        if temp_num2.is_integer():
            if not isinstance(temp_num2, float):
                temp_num2 = int(num2)

        return str(temp_num1 - temp_num2)

    except ValueError as v:
        return "Invalid or non-numeric parameters : {} or {}. Error : {}".format(num1,num2,v), 400
    except Exception as e:
        return "Unexpected error. Details: {}".format(e), 500



#Function accepts two numbers (both int and float) as url parameters and displays the result after multiplying them
@app.route('/mul/<string:num1>/<string:num2>', methods=['POST'])
def mul(num1, num2):
    try:
        temp_num1 = float(num1)
        temp_num2 = float(num2)

        if temp_num1.is_integer():
            if not isinstance(temp_num1, float):
                temp_num1 = int(num1)
                
        if temp_num2.is_integer():
            if not isinstance(temp_num2, float):
                temp_num2 = int(num2)

        return str(temp_num1 * temp_num2)

    except ValueError as v:
        return "Invalid or non-numeric parameters : {} or {}. Error : {}".format(num1,num2,v), 400
    except Exception as e:
        return "Unexpected error. Details: {}".format(e), 500



#Function accepts two numbers (both int and float) as url parameters and displays the result after dividing them
@app.route('/div/<string:num1>/<string:num2>', methods=['POST'])
def div(num1, num2):
    try:
        temp_num1 = float(num1)
        temp_num2 = float(num2)

        if temp_num1.is_integer():
            if not isinstance(temp_num1, float):
                temp_num1 = int(num1)
                
        if temp_num2.is_integer():
            if not isinstance(temp_num2, float):
                temp_num2 = int(num2)

        return str(temp_num1 / temp_num2)

    except ValueError as v:
        return "Invalid or non-numeric parameters : {} or {}. Error : {}".format(num1,num2,v), 400
    except Exception as e:
        return "Unexpected error. Details: {}".format(e), 500



if __name__ == '__main__':
    app.run(debug=True)