import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
# prediction function
model = pickle.load(open("model.pkl", "rb"))
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 7) 
    loaded_model = pickle.load(open("model.pkl", "rb")) 
    result = loaded_model.predict(to_predict)
    print(result)
    if int(result)== 1:
        prediction ='Given transaction is fradulent'
    else:
        prediction ='Given transaction is NOT fradulent'
    print(prediction)
    return int(result)



    
       
#ValuePredictor([-9,0.44,1.41,-0.25,-0.7,-1.4,-0.2])  
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
  
    int_features = [float(x) for x in request.form.values()]
    print(int_features)
    prediction=ValuePredictor(int_features)
    if prediction == 0:
        val ='Given transaction is fradulent'
        return render_template('index.html',
                               prediction_text=val.format(
                                   val),
                               )
    else:
        val='Given transaction is NOT fradulent'
        return render_template('index.html',
                               prediction_text=val.format(
                                   val),
                               )   
                  
if __name__ == "__main__":
    app.run(debug=False)
