## app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():

​    return '안녕하세요'

@app.route('/html')

def html():

​    return render_template("chicken.html")

@app.route('/html_name/<string:name>')

def html_name(name):

​    return render_template('chicken.html', name = name)

@app.route('/dictionary/<string:word>')

def dictionary(word):

​    word_dict = {"apple": "사과", "banana": "바나나"}

​    return render_template('word.html', word = word, word_dict = word_dict)

\# if __name__ == '__main__':

\#     app.run(host)



## workshop(word.html)

{% if word in word_dict %}

​    <h1>{{word}} 는 {{ word_dict[word] }}입니다.</h1>

{% else %}

​    <h3>{{word}} sms 없는 단어입니다.</h3>

{% endif %}



## chicken.html

<html>

​    <header>

​        <title>chicken please</title>

​    </header>

​    <body>

​        <hi>안녕하세요, {{your_name}}🥦🥦🥦🥦🥦🥦</hi>

        <p>chicken weasite</p>

​    <img src= "/static/maxresdefault.jpg ">

​    </body>

</html>