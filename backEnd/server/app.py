from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import numpy as np
import pickle


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
# @app.route('/upload', methods=['GET'])
# def ping_pong():
#     return jsonify('pon11g!')


@app.route('/upload', methods=['POST','GET'])
def predict():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        #get data from post request
        data = request.get_json()
        #convert dict data to int
        data = int(data['text'])
        print(data)
        # data=float(request.form['model_input'])
        
        features = np.array([[data**3, data**2, data**1, data**0]])
        
        #load model from file path /backEnd/server/model.pickle
        file = os.path.join(os.path.dirname(__file__), 'model.pickle')
        model=pickle.load(open(file,'rb'))
        pred = model.predict(features)[0][0]

        prediction_statement =  f"The output of the model is {pred}"
    
    else:
        prediction_statement =  f"Please enter a valid input"

    
    return jsonify(prediction_statement)



# if __name__ == '__main__':
#     app.run()

if __name__ == '__main__':

    port = int(os.getenv('PORT', 5000))



    print("Starting app on port %d" % port)

    if(port!=5000):

        app.run(debug=False, port=port, host='0.0.0.0')

    else:

        app.run()