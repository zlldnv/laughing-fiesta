import time
import psycopg2


try:
    conn = psycopg2.connect("dbname='Innopolispositioning' user='postgres' host='localhost'")
    conn.autocommit = True
except:
    print "Cannot connect to db"


cur = conn.cursor()
i = 0
a= 11.669
b = 46.713
an_x=a
an_y=b
ay_x=a
ay_y=b
vi_x=a
vi_y=b
ma_x=a
ma_y=b
while i<1000:
    time.sleep(1)
    print "%.0f" % time.time()
    an_x +=0.001
    an_y +=0.001
    ay_x +=0.001
    ay_y -=0.001
    vi_x -=0.001
    vi_y +=0.001
    ma_x -=0.001
    ma_y -=0.001
    mytime = int(time.time())
    try:
        cur.execute(
            """INSERT INTO anton_scema.users__postioning ("username","x_position","y_position","time") VALUES (%s,%s,%s,%s)""",("ANTON", an_x, an_y, mytime))
        cur.execute(
            """INSERT INTO anton_scema.users__postioning ("username","x_position","y_position","time") VALUES (%s,%s,%s,%s)""",('AYAZ',ay_x,ay_y,mytime))
        cur.execute(
            """INSERT INTO anton_scema.users__postioning ("username","x_position","y_position","time") VALUES (%s,%s,%s,%s)""",('VITALY',vi_x,vi_y,mytime))
        cur.execute(
            """INSERT INTO anton_scema.users__postioning ("username","x_position","y_position","time") VALUES (%s,%s,%s,%s)""",('MARAT',ma_x,ma_y,mytime))
    except:
        print "Cannot insert"
    i+=1


