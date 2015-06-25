import sys
import os
sys.path.append(os.path.join('..', 'src'))

from flask import Flask, render_template
import dbwrapper
import prettytable
import string

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello():
    return "Hello World!"


@app.route("/prod")
def prod():
    """ show whole ProducedMsg table on the web """ 
    query = "SELECT * FROM ProducedMsg;"
    tablestr = dbwrapper._query_pretty(query)
    result = string.replace(str(tablestr),'\n','<br>')
    return result

@app.route("/con")
def con():
    """ show whole ConsumedMsg table on the web """
    query = "SELECT * FROM ConsumedMsg;"
    tablestr = dbwrapper._query_pretty(query)
    result = string.replace(str(tablestr),'\n','<br>')
    return result

@app.route("/bootstrap_hello")
def bootstrap_hello():
    """ show a super simple example of a bootstrapped page """
    return render_template('Bootstrap_hello.html', some_name="Insight")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    
