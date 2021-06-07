

## Usage

```sh
trigram -i <test_file>
```

## Tests

```sh
pip install tox
tox
```


For the active Python version, just tests:

```sh
# Test
pip install tox
tox -e py
```

Styling:

```sh
tox -e style
```


[pytest](https://docs.pytest.org/en/latest/) runs the tests:

```sh
# Test
pytest
```

`test_requirements.txt` must be installed.

```sh
# Install test requirements
pip install -r test_requirements.txt
```

