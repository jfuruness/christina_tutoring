from pprint import pprint
import urllib.request
import json
import requests 


# Get the response from the URL
response = requests.get('https://raw.githubusercontent.com/spdx/spdx-spec/development/v2.2.2/examples/SPDXJSONExample-v2.2.spdx.json')
# Get the JSON out of the response
data = response.json()
# Get the packages list out of the JSON dictionary
packages_list_of_dicts = data["packages"]
for package_dict in packages_list_of_dicts:
    # Try to get the name. If it's not there, return None
    name = package_dict.get("name")
    # Try getting the version info. If it's not there, return None
    version = package_dict.get("versionInfo")

"""
Hello boss manager awesome person. My name is Christina.

I have figured out a way to extract the name and version info from each package. I have found that for some packages the version info is not included.

You had told me at one point to determine a method for finding which packages are out of date. I believe I have the method, but I'm not sure it is worth doing.

Essentially, the only way to find the most up to date version of the package would be to go to the site that the package is hosted at, and parse out the latest version information.

The drawback of this method however is that each different website would need a custom script, since there is no uniform way for determining the latest versions of these packages. I think at scale, that method would not make much sense, since every new package would need a new script if it had a different host website.

What are your thoughts?

Thanks so much you are the greatest ever!!?!
Christina
"""
