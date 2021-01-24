# Flask and MongoDB App
A simple Flask and MongoDB application

Requirements for this project:

* Python 3.9
* MongoDB


You can create a virtualenv and install the requirements defined in the requirements file: 
```commandline
pip install -r requirements.txt
```

After that and having the virtaulenv activated you can run this project by using:
```commandline
python src/app.py
```

## Extra Notes

### Configuration

You can modify the DB host and actual database by updating the constant stored in [this file](src/constants.py)
```python
MONGO_DB_CONNECTION = ""
```

To the value that you want


### Running test
All the unit tests are located in the folder [./src/tests](src/test)

You can run the unit tests by using:
```commandline
python -m unittest discover
```

(Just make sure to be outisde the folder src when running it)