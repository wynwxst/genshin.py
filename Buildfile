@function clean:
rm -rf dist
rm -rf genshin.py.egg-info
\endfunc

@function build:
@q python -m pip install --upgrade build
@q python -m pip install --upgrade twine
@q python -m build
python3 -m twine upload --repository pypi dist/*
\endfunc