import string_algos
from string_algos import NaiveSearch
text ="AGTA"
pattern = "das"
 
l = NaiveSearch.NaiveSearch(text,pattern)
print l.search_pattern()
