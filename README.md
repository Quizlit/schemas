# schemas
JSON Schemas for Quizlit data

## Description
The goal is to have Quizlit be a quiz application that is driven by json files that hold all the information needed for the quizzes.

These JSON files will be validated by the schemas in this repo with the goal of standardizing that acceptable input data for Quizlit applications.

## Dev Setup
Install min requirements needed to run the unit tests

```
pip install -r requirements/dev.txt
```

## Unit Tests
### Run Unit Test for only 3.12
```
tox -e py312
```

### Run Unit tests for multiple versions of Python
```
tox
```

## Run linters
```
tox -e lint
```

## Python dependencies
This project uses [pip-tools](https://github.com/jazzband/pip-tools) to manage dependencies.

If you want to add a new dependency, `cd` into the requirements directory, update the appropriate file and run `pip-compile` on that file.

For example, add the new dependency to the `dev` file. Then Run `pip-compile min` to create update the `dev.txt` file.
