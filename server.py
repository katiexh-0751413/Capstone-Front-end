from flask import Flask, render_template
import pyodbc
import jinja2

app = Flask(__name__)

# Database configuration
db_config = {
    'server': 'homework3db.database.windows.net',
    'database': 'capstone',
    'username': 'katiexhancock',
    'password': 'DurbanPoison99',
    'driver': '{ODBC Driver 17 for SQL Server}'
}

def get_data():
    # Establish a connection to the database
    connection = pyodbc.connect(
        f"DRIVER={db_config['driver']};"
        f"SERVER={db_config['server']};"
        f"DATABASE={db_config['database']};"
        f"UID={db_config['username']};"
        f"PWD={db_config['password']}"
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Execute your SQL query
    cursor.execute("SELECT FullName, CandidateID, Location, CurrentStatus FROM Candidate")

    # Fetch all the data from the query result
    data = cursor.fetchall()

    # Close the cursor and the connection
    cursor.close()
    connection.close()

    # Print the data
    for row in data:
        print(f"Name: {row.FullName}, Candidate ID: {row.CandidateID}, Location: {row.Location}, Status: {row.CurrentStatus}")

    return data

# @app.route('/data', methods=['GET'])
@app.route('/')
def render_data():
    # Retrieve data from the database
    data = get_data()


    # Render the data in the current-applicants.html template
    return render_template('current-applicants.html', data=data)

if __name__ == '__main__':
    app.run(host="localhost", port= 8000, debug=True)
    # get_data()
    # render_data()
