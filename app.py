from flask import Flask,render_template
import os, pickle as cPickle, json, re

app = Flask(__name__)

@app.route('/')
def hello_method():
    return render_template('login.html')

@app.route('/dashboard')
def hello_me():
    with open('resultfinal.json', 'r',encoding='utf-8') as f:
        hell = json.load(f)

    with open('tfidf_uni_new.pkl', 'rb') as h:
        tf_uni = cPickle.load(h)
        tf_uni.max_features = 50

    with open('tfidf_bi_new.pkl', 'rb') as h:
        tf_bi = cPickle.load(h)
        tf_bi.max_features = 20

    doclist = []
    corpus = []
    p = os.path.abspath('./json test')
    for path, subdirs, files in os.walk(p):
        for name in files:
            if os.path.splitext(os.path.join(path, name))[1] == ".json":
                doclist.append(os.path.join(path, name))

    for i in doclist:
        with open(i, 'r', encoding='utf-8') as f:
            datastore = json.load(f)

        for i in datastore:
            if i['title'].lower():
                # print(re.sub('[^a-zA-Z0-9-+]', ' ', i['title'].lower()))
                corpus.append(re.sub('[^a-zA-Z0-9-+]', ' ', i['title'].lower()))

    uni_X = tf_uni.fit_transform([''.join(corpus)])
    uni_idf = tf_uni.idf_

    bi_X = tf_bi.fit_transform([''.join(corpus)])
    bi_idf = tf_bi.idf_

    feature_names_uni = tf_uni.get_feature_names()
    feature_names_bi = tf_bi.get_feature_names()

    doc = -1
    feature_index = uni_X[doc, :].nonzero()[1]
    feature_index_bi = bi_X[doc, :].nonzero()[1]

    tfidf_scores = zip(feature_index, [uni_X[doc, x] for x in feature_index])
    tfidf_scores_bi = zip(feature_index_bi, [bi_X[doc, x] for x in feature_index_bi])

    # print("".join(corpus))
    ans=[]
    for w, s in [(feature_names_uni[i], s) for (i, s) in tfidf_scores]:
        ans.append([w, s*100])
    for w, s in [(feature_names_bi[i], s) for (i, s) in tfidf_scores_bi]:
        ans.append([w, s*100])
    print (ans)
    print(hell)
    return render_template('dashboard.html',ans=ans,hell=hell)



if __name__ == '__main__':
    app.run(port=4995)