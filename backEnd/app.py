from flask import Flask, jsonify, request, send_file, session
from flask_cors import CORS
import os
import numpy as np
import pickle
import pandas as pd
from sklearn import preprocessing
import io

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


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

df_return = pd.DataFrame()
# app.secret_key = 'my_secret_key'


@app.route('/upload', methods=['POST', 'GET'])
def predict():
    global df_return
    cal_matrics = False

    response_object = {'status': 'success'}
    if request.method == 'POST':

        # get file from post request
        file = request.files['file']

        # Read file and drop unrequired features
        df = pd.read_csv(file)
        df_return = df.copy()   #output file
        df = df.drop(['nameOrig', 'step', 'nameDest'], axis=1)

        # Convert action to numbers
        le = preprocessing.LabelEncoder()
        df.action = le.fit_transform(df.action)

        # Set up X and y
        if len(df.columns) > 6:
            # cal_matrics = True  #to calculate the accuracy, precision, recall and f1 score
            y_actual = df['isFraud']
            df = df.drop(['isFraud', 'isFlaggedFraud',
                        'isUnauthorizedOverdraft'], axis=1)

            df_return = df_return.drop(['isFraud', 'isFlaggedFraud',
                                        'isUnauthorizedOverdraft'], axis=1)

        # Reshape X to fit model
        X = df.to_numpy()
        X = X.reshape((X.shape[0], 1, X.shape[1]))

        # load model from file path /backEnd/server/model.pickle
        # modelFile = os.path.join(os.path.dirname(__file__), 'dummymodel.pickle')
        modelFile = os.path.join(os.path.dirname(__file__), 'model_lstm.sav')

        model = pickle.load(open(modelFile, 'rb'))
        prediction = model.predict(X)
        y_pred = np.round(prediction)

        isFraudCount = len(np.where(y_pred == 1)[0])

        # session['df_return'] = df.to_dict()

        #append the prediction result to the csv
        df_return['isFlaggedFraud'] = y_pred

        #calculate metrics score 
        if cal_matrics:
            accuracy = accuracy_score(y_actual, y_pred)
            precision = precision_score(y_actual, y_pred)
            recall = recall_score(y_actual, y_pred)
            f1 = f1_score(y_actual, y_pred)
        else:
            accuracy = 0.0
            precision = 0.0
            recall = 0.0
            f1 = 0.0

        # OutfileName = 'excel_file.csv'
        # df.to_csv('excel_file.csv', index=False)
        # df.to_csv('excel_file.csv', index=False)

        # file_stream = io.BytesIO(open('excel_file.csv', "rb").read())

        # response = send_file(file_stream,
        #             download_name='excel_file.csv',
        #             as_attachment=True)

        # response = f"Frauds: {isFraudCount}, Non-Frauds: {len(y_pred)-isFraudCount}. \n\nPlease download the excel file for more details"
        response = {
            'message': 'Frauds: ' + str(isFraudCount) +', ' + 'Non-Frauds: ' + str(len(y_pred)-isFraudCount),
            'metrics': 'accuracy: ' + str(round(accuracy,2)) + ', ' + 'precision: ' + str(round(precision,2)) + ', ' + 'recall: ' + str(round(recall,2)) + ', ' + 'f1: ' + str(round(f1,2)),
        }

    else:
        # df_dict = session.get('df')
        # if df_dict is None:
        # return 'DataFrame not found in session'

        # Convert the dictionary back to a DataFrame
        # df = pd.DataFrame.from_dict(df_dict)
        df_return.to_csv('excel_file.csv', index=False)

        file_stream = io.BytesIO(open('excel_file.csv', "rb").read())

        response = send_file(file_stream,
                             download_name='excel_file.csv',
                             as_attachment=True)
        # prediction_statement =  f"Please upload a valid file"

    # return_response = {
    #     'message': prediction_statement,
    # }

    # return jsonify(prediction_statement)
    # return response.status_code, jsonify(return_response)
    return response
    # return jsonify(return_response), response.status_code


@app.route('/upload', methods=['GET'])
def getFile():
    # Retrieve the DataFrame from the session
    # df_dict = session.get('df_return')
    # if df_dict is None:
    #     return 'DataFrame not found in session'

    # # Convert the dictionary back to a DataFrame
    # df1 = pd.DataFrame.from_dict(df_dict)

    excel_file = df_return.to_csv('excel_file.csv', index=False)

    # file_stream = io.BytesIO(open('excel_file.csv', "rb").read())

    # response = send_file(file_stream,
    #             download_name='excel_file.csv',
    #             as_attachment=True)
    response = jsonify({
        'message': 'Excel file downloaded successfully!'
    })

    response.headers["Content-Disposition"] = "attachment; filename=myfile.xlsx"
    response.headers["Content-Type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    return response, excel_file

# if __name__ == '__main__':
#     app.run()


if __name__ == '__main__':

    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    if (port != 5000):

        app.run(debug=False, port=port, host='0.0.0.0')

    else:

        app.run()
