from flask import Flask, render_template, request, url_for, redirect
from werkzeug.datastructures import FileStorage
from calculation import sakana_weight
from calculation import sakana_wight_list
import pandas as pd
import os


app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html')
#--------------------------------------#

@app.route("/calc",methods=['GET','POST'])
def calculation():
    if request.method == "GET":
        return render_template('calculation.html')
    elif request.method  == "POST":
        species = request.form['species']
        length  = request.form['length']
        # 魚体重の計算
        answer = sakana_weight(species,length)

        return render_template('calculation.html', result=answer)       
#--------------------------------------#

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # URLでhttp://127.0.0.1:5000/uploadを指定したときはGETリクエストとなるのでこっち
    if request.method == 'GET':
        return render_template('upload.html')
    # formでsubmitボタンが押されるとPOSTリクエストとなるのでこっち
    elif request.method == 'POST':
        csv_data = request.files['data']
        if isinstance(csv_data, FileStorage) and csv_data.content_type == 'text/csv':
            df = pd.read_csv(csv_data,index_col=None,header=None)
            df.to_csv(os.path.join('./static/csv', csv_data.filename),header=False,index=False)
            return redirect(url_for('uploaded_file', filename=csv_data.filename))
        else:
            raise ValueError('data is not csv')
#--------------------------------------#

@app.route('/uploaded_file/<string:filename>')
def uploaded_file(filename):
    return render_template('uploaded_file.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
#--------------------------------------#
@app.route('/upload', methods=['GET', 'POST'])
def clcsv():
    if request.method == 'GET':
        return render_template('calculation2.html')