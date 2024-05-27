# truckoo-task

Steps to implement

1. Pull the repo. Create a python venv using

    ```shell 
    python -m venv /path/to/new/virtual/environment
    ```

    Activate the venv with 

    ```shell
    source /path/to/new/virtual/environment/bin/activate
    ```

    Install the dependecies using

    ```shell
    pip install requirements.txt
    ```

2. Run the flask app using the interpreter in the IDE or use `flask --app api run`
3. You will be now able to use the endpoints at GET http://127.0.0.1:5000/(displaystringholder)/(locale)/(context) and POST http://127.0.0.1:5000/resolve/displaystring . For the post endpoint, a sample payload would look like the following

```json
{
    "dictionary":{
    "displaystringUID": "question.tire1_r_profile.description",
		"subdocument_01": {
	    "displaystringUID": "question.tire1_r_profile.description"
		},
		"subdocument_02": {
	    "displaystringUID": "question.tire1_r_profile.description",
			"subdocuments": [
					{
					"displaystringUID": "question.tire1_r_profile.description"
					},
					["some", "weird", "other", {"displayStringUID": "question.tire1_r_profile.description"}, "subdocument"],
					{
					"displaystringUID": "question.tire1_r_profile.description"
					}
				]
		}
}
,
    "locale":"en-GB",
    "context":"assessment"
}
```
Checkout the api implementation for more details.
