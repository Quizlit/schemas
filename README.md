# schemas
A place to create, store and test the json schemas

## Dev Setup
Install min requirements needed to run the unit tests

```
pip install -r requirements/min.txt
```

## Run Unit Tests
```
python -m unittest discover -v
```

## Python dependencies
This project uses [pip-tools](https://github.com/jazzband/pip-tools) to manage dependencies.

If you want to add a new dependency, `cd` into the requirements directory, add the new dependency to the `min` file.
Run `pip-compile min` to create update the min.txt file.
