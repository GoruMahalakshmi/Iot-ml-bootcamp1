from flask import Flask,request#import Flask, request
from models import generateAI#  from models.py
import pickle
generateAI()
ai=pickle.load(open('ai.pkl', 'rb'))
app=Flask(__name__)#create server
@app.route('/')
def home():
    return "Server is running"
@app.route('/predict')#GET
def predict():#http://
    ir=request.args.get('ir')
    ir=int(ir)#convert to int
    data=[[ir]]#2D array
    result=ai.predict(data)[0]#predict[0]['object']
    return result
if __name__=='__main__':
    app.run(host='0.0.0.0',port=4000)#run server


