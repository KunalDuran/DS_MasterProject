from flask import Flask, render_template
import pandas as pd
from utils import recommender


app = Flask(__name__)

df = pd.read_json('cleaned.json')
@app.route('/')
def home():
    N = 9
    random6 = df.sample(N)
    random6 = [dict(random6.iloc[i]) for i in range(N)]

    return render_template('index.html', books=random6)


@app.route('/output/<bookTitle>')
def output(bookTitle):
    result = dict(df[df['book_title']==bookTitle].squeeze())
    recommended_book= recommender(df, result['genre'])
    return render_template('output.html', result=result, recommended_book=recommended_book)



if __name__ == "__main__":
    app.run(debug=True)