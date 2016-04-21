from Bio import Entrez
#import textmining
from collections import defaultdict
import re
#from sets import set
	 
Entrez.email='drcc@vt.edu'
database='pubmed'


## alright, first we do an quick analysis of all of the literature on mild traumatic brain injury
neuroQuery = """
("functional neuroimaging" or "positron emission tomography" or PET or "functional magnetic resonance imaging" or "functional MRI" or "fMRI" or "resting state" or "functional connectivity" or "regional homogeniety") and ("biomarker" or "classifier" or "disease state")  and ("1995"[Publication Date] : "3000"[Publication Date])
"""

# perform the query the first time to determine
# the number of records
searchResult = Entrez.esearch(db = database, term = neuroQuery)
searchRecord = Entrez.read(searchResult)

# get the number of matches to the query
resultCount = searchRecord['Count']
print "Results:", resultCount

# perform the query again to get all of the PMIDs that match
searchResult = Entrez.esearch(db = database, term = neuroQuery, retmax = resultCount)
searchRecord = Entrez.read(searchResult)


for id in searchRecord['IdList']:
	print id
	continue
