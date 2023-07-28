# Chata.ai_CodingExercise
This is a python coding exercise at Chata.ai.

## Installation

**Prerequisites:**
- Python 3.7+
- or you have Docker installed on your local machine

**Setup and activete the virtual environment:**

```shell
$ pip install nltk flask
$ python app.py
```
or build the docker image based on the Dockerfile

```shell
$ docker build -t your-image-name .
$ docker run -p 8001:8001 your-image-name
```
or even more simply pull the docker image from the Docker Hub
```shell
$ docker pull aishangchixiang/chata.ai-coding-exercise
$ docker run -p 8001:8001 chata.ai-coding-exercise
```

**Run Unit Tests**
```shell
$ python test.py
```


## API Documentation
This section describes how to interact with the API of this application.

### Base URL
'http://localhost:8001/search'

### Parameter
'string': query text

### API details

'http://localhost:8001/search?string=Now%20is'  
Query with a parameter string = 'Now is'.


### Response
- `200 OK` on success
- `400 Bad Request` error: "Please provide a search string using 'string' parameter"
- `404 Not Found` error: "File not found"

```json
{
	“query_text” : “Now is”,
	“number_of_occurrences” : 3,
	“occurences” : [
		{
			“line” : 45,
			“start” : 17,
			“end” : 23,
			“in_sentence” : “Now is the time to rise from the dark and desolate valley of segregation to the sunlit path of racial justice.”
		},
		{
			“line” : 46,
			“start” : 62,
			“end” : 68,
			“in_sentence” : “Now is the time to open the doors of opportunity to all of God’s children.”
		},
		{
			“line” : 48,
			“start” : 1,
			“end” : 7,
			“in_sentence” : “Now is the time to lift our nation from the quicksands of racial injustice to the solid rock of brotherhood.”
		}
	]
}
```
### Postman
More details you can check and run the requests in Postman.
Here is the [scripts](Chata.ai.postman_collection.json) you can import to your Postman.


