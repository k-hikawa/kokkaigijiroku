#可視化に必要なライブラリをインポート
import matplotlib.pyplot as plt 
from sklearn.manifold import TSNE
import numpy as np
import pandas as pd

#モデルの読み込み
from gensim.models import word2vec

def search():
    model = word2vec.Word2Vec.load("./gijirokumodel/gijiroku1990.model")

    results = model.most_similar(positive=["日本"],topn=10)
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
    return df