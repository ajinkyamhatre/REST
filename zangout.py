from pymongo import Connection
from flask import *
app=Flask(__name__)
con=Connection()
db=con.shop_database
users=db.users
@app.route('/myquery')
def homepage():
	ans=users.find()
	op=''
	for ch in ans :
		op=op+' '+str(ch)

	return op

@app.route('/mypost', methods = ['POST'])
def api_message():
	if request.headers['Content-Type'] == 'text/plain':
        	ans=users.insert(request.data)
		return str(ans)

	elif request.headers['Content-Type'] == 'application/json':

	        ans=users.insert((request.json))
		return str(ans)


	else:
	        return "415 Unsupported Media Type"

if __name__=="__main__":
        app.run('localhost',8080,debug=True)


