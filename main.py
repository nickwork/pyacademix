# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 00:47:11 2016

Site: https://github.com/nickwork/pyacademix

@author: nick

EuropePMC Web Service Wrapper

Query: http://www.ebi.ac.uk/europepmc/webservices/rest/search/query={0}
PUB_YEAR:%5B{0}%20TO%20{1}%5D 
LANG:eng 
SRC:MED 
sort_cited:y&resulttype=core&pageSize={2}&format=json


"""

import requests

query = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria&format=json'

r = requests.get(query)
