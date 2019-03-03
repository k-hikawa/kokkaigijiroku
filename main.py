from flask import *

#可視化に必要なライブラリをインポート
import matplotlib.pyplot as plt 
from sklearn.manifold import TSNE
import numpy as np
import pandas as pd

#モデルの読み込み
from gensim.models import word2vec

def search(year, word):
    try:
        model = word2vec.Word2Vec.load("./gijirokumodel/gijiroku" + year + ".model")
        results = model.most_similar(positive = [word], topn = 10)
        name = []
        num = []
        for result in results:
            print(result[0],result[1])
            name.append(result[0])
            num.append(result[1])
            
        df = pd.DataFrame({
                '名前' : name,
                '類似度' : num
            })
    except:
        df = None
    return df


app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def main():
    if request.method == 'POST':
        word = request.form['Word']
        years = ["1940", "1950", "1960", "1970", "1980", "1990", "2000", "2010"]
        result_html = "<form action = '/' method = 'POST'><table>"
        result_html += "<tr class='big_tr'>"
        for year in years:
            result = search(year, word)
            if result is not None:
                #result_html += "<h4>" + year + "年</h4>"
                result_html += "<td><table border=1  align='left' class='table'>"
                result_html += "<tr><th class='year'>"+year+"年</th><th class='word'>単語</th><th class='value'>類似度</th></tr>"
                for row in result.itertuples(name = None):
                    result_html += "<tr>"
                    result_html += "<td>"+str(row[0]+1)+"</td>"
                    result_html += "<td><input type='submit' name='Word' value='"+row[1]+"'></td>"
                    result_html += "<td>"+str(row[2])+"</td>"
                    result_html += "</tr>"
                result_html += "</td></table>"
        result_html += "</tr></table></form>"
        return render_template("form.html")+"""
        <h3>
        """ + word + """
        の検索結果</h3>
        """ + result_html
    else:
        return render_template("form.html")


# @app.route('/result', methods = ['POST', 'GET'])
# def confirm():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html", result = result)

if __name__ == '__main__':
    app.run(port='5000')