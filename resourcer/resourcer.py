import requests
import requests_cache

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

requests_cache.install_cache("resource_cache", backend="memory", expire_after=180)

class Resource:
    API: str = "https://developersIndia.github.io/resources/"

    def get_resource(param) -> str:
        """
        Given a URL, return response data in JSON and the response code
        """
        url = f"{Resource.API}{CATEGORY_API_PATH[param.get('category')]}"
        res = requests.get(url).json()
        return res
