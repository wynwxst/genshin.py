# Genshin.py

A simple wrapper for the genshin api for python

### Installation:
`pip install genshin.py`


### Usage:
```python
import genshin
### Currently avaliable types for 2022
#['artifacts', 'boss', 'characters', 'consumables', 'domains', 'elements', 'enemies', 'materials', 'nations', 'weapons']
g = genshin.Genshin(local=False) # set local to true to use local storage
print(g.types)
o = g.api("type") # replace type with any value from g.types
# methods for api object
print(o.values)
print(o.get("query")) #get json formatted data for a query eg. if the type is characters then albedo would return stats for albedo
print(o.search("query")) # experimental searching through the api
```

### Development:
Install buildproj:

`pip install buildproj`

`build`

In case of the binary not working:

`python buildbinary.py`

All processes are automated except for the sign in for pip, please be sure to also change the version and name in `setup.py

### Tests:
Install buildproj:

`pip install buildproj`

`build test`

In case of the binary not working:

`python buildbinary.py test`