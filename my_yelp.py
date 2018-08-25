#Maintainer Qamber Mehdi
# Created on August 25, 2018

import requests 

api_key = "az6Ki-01wJkXzlDyFkdLMp-uhkqdC5ZnMJmQH2QdXfpYU3Z15zh5HbVhCM24LNiQ1BVib8rwP5PLMPATJblk3tuAVjfw_rp5w37w1SiXSKR1YXp0mOmCY-ZCVvotWW3Yx"

url = "https://api.yelp.com/v3/businesses/search"

my_headers = {
    "Authorization": "Bearer %s" % api_key
}

my_params = {
    "term": "restaurants",
    "location": "chicago",
    "limit": 3,
}

businesses_object = requests.get(url, headers=my_headers, params=my_params)

businesses_dict = businesses_object.text

print(businesses_dict)