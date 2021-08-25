from flask import Flask, request, jsonify, render_template
import json

# load json data
score_file = open('interest_score.json')
score_data = json.load(score_file)


app = Flask(__name__)


# request for interest score
@app.route('/api/search_interest')
def search_interest_api():
    keyword = request.args.get('keyword')
    result = score_data[keyword]
    return result


score_file.close()

if __name__ == "__main__":
    app.run(debug=True)
