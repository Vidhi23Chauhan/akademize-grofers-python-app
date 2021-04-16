# Python App

## Create Virtual Environment

```bash
python3 -m venv .venv
```

```.venv``` is the name of the virtual environment.
You will see a folder created with the name .venv

## Checking the python interpreter source
For unix based systems

```bash
which python3
/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
```

For windows

```bash
where python
/Users/sravan/miniconda3/bin/python
```

## Activate the virtual environment

### For Unix based systems

```bash
source .venv/bin/activate
```
### For windows

```bash
.venv\Scripts\activate
```

## Checking the python interpreter source after activating the virtual environment

```bash
which python3
/Users/vidhichauhan/Documents/akademize-grofers-python-app/.venv/bin/python3
```

For windows

```bash
where python
/Users/sravan/workapce/akademize/akademize-grofers-python-app/.venv/bin/python
```

## Deactivate virtual environment

```bash
deactivate
```

## Installing numpy

```bash
source .venv/bin/activate  # If virtual environment is not activated
```

```bash
pip install numpy
```

## Installing Jupyter and Ipykernel

```bash
pip install ipykernel jupyter
```

## Open Jupyter Notebook

```bash
jupyter notebook
```
