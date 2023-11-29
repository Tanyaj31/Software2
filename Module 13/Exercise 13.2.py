from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

#MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'flightgameuser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Tanya'
app.config['MYSQL_DATABASE_DB'] = 'flight_game'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

#route to fetch data from the database
@app.route('/airport/<ICAO_code>', methods=['GET'])
def airport(ICAO_code):
    try:
        #creating a MySQL cursor
        cur = mysql.get_db().cursor()

        #executing a sample query
        cur.execute("SELECT ident, name, municipality FROM airport WHERE ident = '" + ICAO_code + "'")

        #fetching all of the rows from the query result
        data = cur.fetchall()
        result = {}
        result['ICAO'] = data[0][0]
        result['Name'] = data[0][1]
        result['Location'] = data[0][2]

        return result

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)