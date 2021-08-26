# no official api for google trends, using pytrends

from pytrends.request import TrendReq
import pandas as pd
import time


def search_interest():
    col = ['kw_header']
    keywords = pd.read_csv("top-search-keywords.csv", names=col)
    keywords = keywords.kw_header.to_list()

    # using google trends api
    pytrends = TrendReq()

    # pytrend API supports upto 5 keywords per search only.

    df = []
    for x in range(int(len(keywords)/5)):
        pytrends.build_payload(kw_list=keywords[:5], timeframe='now 4-H')
        print("Batch keywords: ", keywords[:5])
        del keywords[:5]
        dt = pytrends.interest_over_time()
        dt.drop('isPartial', axis=1, inplace=True)
        df.append(dt)
        print('please wait...')
        print("keywords are processed in batches to minimize connection timeouts ..")
        time.sleep(60)

    k_data = pd.concat(df, axis=1)
    # k_data.to_csv('interest_score.csv', encoding='utf_8_sig')
    k_data.to_json('interest_score.json', orient='columns', date_format="iso")


# restart the script after a timeout

while True:
    time.sleep(5)
    try:
        search_interest()
    except Exception as e:
        print(e)
        continue
