from flask import Flask, request, render_template
import json
from datetime import datetime

# load json data
score_file = open('interest_score.json')
score_data = json.load(score_file)

app = Flask(__name__)


@app.route("/")
def chart():
    # creating charts for ncis keywords to observe its trend

    data = score_data['tokyo olympics'].items()
    x_label = [row[0] for row in data]
    # format date
    labels = []
    for x in x_label:
        stripe_time = datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ')
        labels.append(stripe_time.strftime('%H:%M:%S'))
    y_label = [row[1] for row in data]
    # replace null with zero
    values = [0 if x is None else x for x in y_label]

    return render_template("chart.html", labels=labels, values=values)


# api request for interest score
@app.route('/api/search_interest')
def search_interest_api():
    keyword = request.args.get('keyword')
    result = score_data[keyword]
    return result


score_file.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
