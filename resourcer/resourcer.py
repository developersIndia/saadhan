import urllib
import json


HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Content-Type": "application/json",
}

CATEGORY_API_PATH = {
    "python": "languages/python",
    "javascript": "languages/javascript",
    "git": "tools/git",
    "android": "app-development/android",
    "flutter": "app-development/flutter",
    "miscellaneous": "miscellaneous",
    "machine-learning": "artificial-intelligence/machine-learning",
    "deep-learning": "artificial-intelligence/deep-learning",
    "dsa": "dsa",
    "computer-graphics": "computer-graphics",
    "computer-science": "computer-science",
}


class Resource:
    API: str = "https://developersIndia.github.io/resources/"

    def get_resource(param) -> str:
        # https://developersindia.github.io/resources/languages/javascript/
        """
        Given a URL, return response data in JSON and the response code
        """
        url = f"{Resource.API}{CATEGORY_API_PATH[param.get('category')]}"
        req = urllib.request.Request(url, headers=HEADERS)

        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode("utf-8"))
        return res, response.code
