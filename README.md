# Google trends search interest of 100 keywords 
100 keywords are provided in csv 'top-search-keywords.csv'

install requirements.txt
``` 
pip install -r requirements.txt 

```

## Pull search interest score of 100 keywords on a four-hour basis

```
python data_puller.py

```
The job runs in batch of 5 keywords 

the script is set to sleep for 60 secs per batch to minimize connection timeouts

The output is saved as a json file 

## API request

``` 
python app.py

```

send GET request 


api/search_interest?keyword=< keyword >

example 
```
http://127.0.0.1:5000/api/search_interest?keyword=ncis
http://34.121.1.99:5000/api/search_interest?keyword=mark harmon


```

response sample

```
{"datetime": search_interest, "datetime": search_interest, "datetime": search_interest, "datetime": search_interest}
{
    "2021-08-26T06:36:00.000Z": 47.0,
    "2021-08-26T06:37:00.000Z": 33.0
    }

```

## Cloud deployment 
`data_puller python script` and `flask api` is deployed on `GCP` using `docker` on separate docker containers. 

```
interact with a chart 

http://34.121.1.99:5000/
```

see Dockerfile and docker-compose yml

The host folder is mounted on the contianers to allow the python scripts read and write to the same json file independently.



## Github Action 


## Chart
interact with the 'tokyo olympics' search interest

```
http://34.121.1.99:5000/
```
data refreshes on the hour


## Reference
[PyTrends - Pseudo API for Google Trends]('https://github.com/GeneralMills/pytrends')
