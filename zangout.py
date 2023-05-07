import MySQLdb
from flask import *
def db():
	return MySQLdb.connect('localhost','root','qwerty@123','test')
app=Flask(__name__)

@app.route('/UserService/Users')
def userall():
	connection = db()
	cursor = connection.cursor()
	query = 'select * from mytable;'
	cursor.execute(query)
	data = cursor.fetchall()
	output = []
	for user in data:
		user_data = {'id': user[0], 'name': user[1], 'address': user[2], 'phone': user[3]}
		output.append(user_data)
	connection.close()
	return jsonify(output)
@app.route('/UserService/Users/<int:id>')
def userone(id):
	con = db()
	cr = con.cursor()
	query = 'select * from mytable;'
	cr.execute(query)
	data = cr.fetchall()
	ans =[]
	for i in data:
		j = {'id' : i[0], 'name' : i[1], 'address' : i[2], 'phone' : i[3] }
		ans.append(j)
	if (id > len(ans)) or (id < 1):
		op = {'error' : 'array index out of order'}
	else :
		op = ans[id-1]
	con.close()
	return jsonify(op)

@app.route('/UserService/Users', methods =['GET','PUT'])
def userput():
	con = db()
	cr = con.cursor()
	if request.method == 'PUT':
		data = request.json
		query = "insert into mytable (name,address,phone) values ('%s','%s','%s')"%(data['name'],data['address'],data['phone'])
		cr.execute(query)
		con.commit()
	con.close()
	return "ok"
if __name__=="__main__":
        app.run('localhost',8080,debug=True)


