from flask import Flask
import main

all_numbers = main.getFullNumbers()
app = Flask(__name__)

@app.route('/num')
def numbers():
    lista =  str(all_numbers)
    return lista 



app.run(host='0.0.0.0')