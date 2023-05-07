import MySQLdb
from flask import *


def db():
    return MySQLdb.connect('localhost', 'root', 'qwerty@123', 'test')


def get_user_list(user_id=None):
    connection = db()
    cursor = connection.cursor()
    query = 'select * from mytable;'
    cursor.execute(query)
    data = cursor.fetchall()
    output = []
    for user in data:
        user_data = {'user_id': user[0], 'name': user[1], 'address': user[2], 'phone': user[3]}
        if user_id and user_id == user_data['user_id']:
            output.append(user_data)
        else:
            output.append(user_data)
    connection.close()
    return output


app = Flask(__name__)


@app.route('/UserService/Users')
def get_all_users():
    output = get_user_list()
    return jsonify(output)


@app.route('/UserService/Users/<int:user_id>')
def get_user(user_id):
    output = get_user_list(user_id)
    return jsonify(output)


@app.route('/UserService/Users', methods=['GET', 'PUT'])
def update_user():
    connection = db()
    cursor = connection.cursor()
    if request.method == 'PUT':
        data = request.json
        query = f"insert into mytable (name,address,phone) values ('{data['name']}','{data['address']}','{data['phone']}')"
        cursor.execute(query)
        connection.commit()
    connection.close()
    return jsonify({"response": "ok"})


if __name__ == "__main__":
    app.run('localhost', 8080, debug=True)
