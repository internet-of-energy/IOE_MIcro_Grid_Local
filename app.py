from flask import Flask
from flaskext.mysql import MySQL
from flask import jsonify
from flask import request

app = Flask(__name__)

mysql = MySQL(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'AKILAN1999'
app.config['MYSQL_DATABASE_DB'] = 'relay_electricity'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/',methods = ['GET'])
def home():
   send_batt = request.args.get('send_batt')
   get_batt = request.args.get('get_batt')
   conn = mysql.connect()
   cur = conn.cursor()
   cur.execute("SELECT * from relays_design_2 where (global_batt_id = %s AND type = 'send') OR (global_batt_id = %s AND type = 'send');",[send_batt,get_batt])
   rv = cur.fetchall()
   json_data = []
   content = {}
   for result in rv:
      content = {'grid_relay': result[0], 'global_batt_id': result[1], 'type': result[2]}
      json_data.append(content)
      content = {}
   return jsonify(json_data)



