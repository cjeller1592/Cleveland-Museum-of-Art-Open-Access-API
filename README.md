# Cleveland-Museum-of-Art-Open-Access-API
A simple library of the [Cleveland Museum of Art Open Access API](http://openaccess-api.clevelandart.org/) for Python

# **Getting Started**

_Importing and Instanstiating:_

```
import cma

c = cma.openAccess()

```

# **Using the API**

The Open Access API can take two requests: 

_Search:_ 
A general query that returns a list of artworks and metadata.

All you need is a keyword/phrase and the limit of how many results you want in the response

```
search = c.search("Van Gogh", "1")

print search

# Returns artworks and metadata that fit search result
```

_Find:_
A query that returns a specific artwork and its metadata.

All you need is either the artwork's id or accession number.

```
vg = c.find("125249")

# Returns artwork and metadata
# You can even look up specific metadata

print vg["images"]["web"]["url"]

https://openaccess-cdn.clevelandart.org/1947.209/1947.209_web.jpg
```

