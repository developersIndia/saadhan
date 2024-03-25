import requests
import requests_cache
from enum import Enum


class Levels(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Types(Enum):
    video = 1
    article = 2
    book = 3
    github = 4
    website = 5


HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Content-Type": "application/json",
}

CATEGORY_API_PATH = {
    "python": "languages/python",
    "javascript": "languages/javascript",
    "c": "languages/c",
    "cpp": "languages/c++",
    "css": "languages/css",
    "ruby": "languages/ruby",
    "sql": "languages/sql",
    "rust": "languages/rust",
    "java": "languages/java",
    "typescript": "languages/typescript",
    "go": "languages/go",
    "android": "app-development/android",
    "flutter": "app-development/flutter",
    "miscellaneous": "miscellaneous",
    "machine-learning": "artificial-intelligence/machine-learning",
    "deep-learning": "artificial-intelligence/deep-learning",
    "dsa": "dsa",
    "computer-graphics": "computer-graphics",
    "computer-science": "computer-science",
    "operating-systems": "operating-systems",
    "devops": "devops",
    "git": "tools/git",
    "linux": "tools/linux",
}

requests_cache.install_cache("resource_cache", backend="memory", expire_after=180)


class Resource:
    API: str = "https://developersIndia.github.io/resources/"

    def __init__(self, category) -> None:
        self.category = category

    def get_resource(self) -> str:
        """
        Given a URL, return response data in JSON and the response code
        """
        url = f"{Resource.API}{CATEGORY_API_PATH[self.category]}"
        res = requests.get(url).json()
        return res

    def get_resources_by_type(self, rtype: str):
        res = self.get_resource()
        filtered_res = []

        for r in res["resources"]:
            if r.get("type") == rtype:
                filtered_res.append(r)
        return filtered_res

    def get_resources_by_level(self, level: str):
        res = self.get_resource()
        filtered_res = []

        for r in res["resources"]:
            if r.get("level") == level:
                filtered_res.append(r)
        return filtered_res

    def get_resources_by_level_and_type(self, level: str, rtype: str):
        res = self.get_resource()
        filtered_res = []

        for r in res["resources"]:
            if level and r.get("level") != level:
                continue
            if rtype and r.get("type") != rtype:
                continue
            filtered_res.append(r)
        return filtered_res

    # @classmethod
    def get_resources_contributors():
        res = requests.get(
            "https://raw.githubusercontent.com/developersIndia/resources/master/.all-contributorsrc"
        ).json()
        return res

    def get_saadhan_contributors():
        res = requests.get(
            "https://raw.githubusercontent.com/developersIndia/saadhan/main/.all-contributorsrc"
        ).json()
        return res
