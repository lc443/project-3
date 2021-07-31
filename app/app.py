from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'mlbTeamsData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Mlb Teams'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM teams')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, teams=result)


@app.route('/view/<int:team_id>', methods=['GET'])
def record_view(team_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM teams WHERE id=%s', team_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', team=result[0])


@app.route('/edit/<int:team_id>', methods=['GET'])
def form_edit_get(team_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM teams WHERE id=%s', team_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', team=result[0])


@app.route('/edit/<int:team_id>', methods=['POST'])
def form_update_post(team_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('team_name'), request.form.get('salary_in_millions'), request.form.get('wins'),
                 team_id)
    sql_update_query = """UPDATE teams t SET t.team_name = %s, t.salary_in_millions = %s, t.wins = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/teams/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Team Form')


@app.route('/teams/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('team_name'), request.form.get('salary_in_millions'), request.form.get('wins'))
    sql_insert_query = """INSERT INTO teams (team_name,salary_in_millions,wins) VALUES (%s, %s,%s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:team_id>', methods=['POST'])
def form_delete_post(team_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM teams WHERE id = %s """
    cursor.execute(sql_delete_query, team_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/teams', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM teams')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/teams/<int:team_id>', methods=['GET'])
def api_retrieve(team_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM teams WHERE id=%s', team_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/teams/', methods=['POST'])
def api_add() -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/teams/<int:team_id>', methods=['PUT'])
def api_edit(team_id) -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/teams/<int:team_id>', methods=['DELETE'])
def api_delete(team_id) -> str:
    resp = Response(status=210, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
