from flask import Flask, request
from datetime import datetime
from lifeladderApp import ladderLogic
from UI import palletsInShipmentAsOneString
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <html><body>
            <h2>Welcome to the LifeLadderPacker</h2>
            <form action="/greet">
                How many LifeLadders? <input type='text' name='amount'><br><br>
                Length? <input type='text' name='length'><br><br>
                Include LightUnits? <input type='checkbox' name='lights'><br><br>
                <input type='submit' value='Continue'>
            </form>
        </body></html>
        """

@app.route('/greet')
def greet():
    amount = request.args.get('amount')    
    length = request.args.get('length')    
    lights = request.args.get('lights')    
    lights = (lights == 'on') ; 1, 0

    order = [[int(amount), int(length), lights]]
    myShipment = ladderLogic(order)
    palletsString = palletsInShipmentAsOneString(myShipment)
    palletsString = palletsString.replace('\n', '<br>')

    return """
        <html><body>
            You are packing <b>{0}</b> LifeLadders of length <b>{1}</b><br> 
            LightUnits included? <b>{2}</b><br><br>
            {3}
        </body></html>
        """.format(amount, length, lights, palletsString)

# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
