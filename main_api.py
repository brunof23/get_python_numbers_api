from webbrowser import get
from flask import Flask
import src.main_get as main_get

all_numbers = main_get.getFullNumbers()
app = Flask(__name__)

@app.route('/num')
def numbers():
    lista =  str(all_numbers)
    return lista 



app.run(host='0.0.0.0')