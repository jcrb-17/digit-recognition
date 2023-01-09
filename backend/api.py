from flask import Flask,request,jsonify
import numpy as np
import pickle
from flask_cors import CORS, cross_origin

x = pickle.load(open('x.pkl','rb'))
y = pickle.load(open('y.pkl','rb'))

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/",methods=['POST'])
@cross_origin()
def f2():
	p0,p1,p2,p3,p4,p5,p6,p7,p8,p9 = 0,0,0,0,0,0,0,0,0,0
	d = request.get_json()
	print(d)
	for i in range(len(d["data"])):
		d["data"][i] = int(d["data"][i]) 
	value = np.array([d['data']])
	distances = np.sqrt(np.sum((x-value)**2,axis=1))
	k = 7
	n_i = distances.argsort()[:k]
	n = np.take(y,n_i)
	for i in n:
		if i == 0:
			p0 += 1
		elif i == 1:
			p1 += 1
		elif i == 2:
			p2 += 1
		elif i == 3:
			p3 += 1
		elif i == 4:
			p4 += 1
		elif i == 5:
			p5 += 1
		elif i == 6:
			p6 += 1
		elif i == 7:
			p7 += 1
		elif i == 8:
			p8 += 1
		elif i == 9:
			p9 += 1
	return jsonify({"p0":p0,"p1":p1,"p2":p2,"p3":p3,"p4":p4,"p5":p5,"p6":p6,"p7":p7,"p8":p8,"p9":p9})

if __name__ == '__main__':
	app.run(debug=True) 
