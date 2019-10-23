from flask import Flask, render_template, Response,redirect,request
import os
app = Flask(__name__)

users=["OOSE","DBMS","Computer Networks","TOC","Microprocessor"]
@app.route('/')
def home():
    return render_template('first_first.html')

	    
@app.route('/scan/<file_path>',methods = ['POST', 'GET'])
def tryon(file_path):
	file_path = file_path.replace(',','/')
	os.system('python test_barcode.py ')
	return render_template('first.html')
	
@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		# return '<body>hey</body>'
		# username = request.form["username"]
		username = request.form["username"]
		if  username in users :
			return render_template('first.html')
		else:
			return render_template('first_first.html')
@app.route('/check', methods=['POST','GET'])
def check():
	if request.method == 'POST':
		subject = request.form["username"]
		# return '<body>hey</body>'
		# username = request.form["username"]
		username = request.form["username"]
		if  username in users :
			return render_template('home.html')
		else:
			return render_template('first.html')
@app.route('/report.html/<file_path>',methods = ['POST', 'GET'])
def report(file_path):
	file_path = file_path.replace(',','/')
	os.system('python report.py ')
	return render_template('/report.html')
@app.route('/check/<file_path>', methods=['POST','GET'])
def complain(file_path):
	return render_template('complaint.html')
if __name__ == '__main__':
    app.run(debug=True)

