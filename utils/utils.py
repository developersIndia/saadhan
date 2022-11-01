import urllib
import json

def get(url) -> str:
    """
    Given a URL, return response data in JSON and the response code
    """
    req = urllib.request.Request(url, headers=HEADERS)

    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode("utf-8"))
    return res, response.code
