
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import psycopg2


try:
    conn = psycopg2.connect("dbname='Innopolispositioning' user='postgres' host='localhost'")
    conn.autocommit = True
except:
    print "Cannot connect to db"

cur = conn.cursor()
oldDataSet = open('dataset.txt', 'r')
temp = None
data ={}
start__time = None
finish__time = None
for line in oldDataSet:
    mas = line.split(',')
    if (temp == None):
        temp = mas
    if (long(mas[0]) - long(temp[0]) == 0):
        data[int(mas[0])]=[float(mas[1]),float((mas[2])[:-1]),"green"]
        start__time = int(mas[0])
    elif (long(mas[0])-long(temp[0]) == 1):
        data[int(mas[0])] = [float(mas[1]), float((mas[2])[:-1]), "green"]
        temp = mas
    else:
        while (long(mas[0])-long(temp[0]) != 1):
            temp[0] = long(temp[0]) + 1
            data[int(temp[0])] = [float(temp[1]), float((temp[2])[:-1]),"red"]
        data[int(mas[0])] = [float(mas[1]), float((mas[2])[:-1]), "green"]
        temp = mas
finish__time = int(mas[0])
oldDataSet.close()
app = Flask(__name__)
app._static_folder = '/Users/antonzalaldinov/Desktop/Internership/python-http-server/templates/static'
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    cur.execute(
        "SELECT MIN(time) FROM anton_scema.users__postioning")
    start__time = cur.fetchone()[0]
    print start__time
    cur.execute(
        "SELECT MAX(time) FROM anton_scema.users__postioning")
    finish__time = cur.fetchone()[0]
    print finish__time
    print ("I am connected")
    socketio.emit('start', {'data': start__time})
    socketio.emit('finish', {'data': finish__time})
@socketio.on('message')
def handle_message(message):
    cur.execute(
        "SELECT x_position FROM anton_scema.users__postioning WHERE  users__postioning.time=%s AND users__postioning.username =%s", (message,'VITALY'))
    x = cur.fetchone()[0]
    cur.execute(
        "SELECT y_position FROM anton_scema.users__postioning WHERE  users__postioning.time=%s AND users__postioning.username =%s", (message,'VITALY'))
    y = cur.fetchone()[0]
    socketio.emit('on x', {'data':y})
    socketio.emit('on y', {'data':x})
    print('received message: ' + repr(message))
    print x
    print y


if __name__ == '__main__':
    socketio.run(app)
