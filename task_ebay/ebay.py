import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from bs4 import BeautifulSoup
import requests


class EbayCollector:
    """Collects information from ebay"""

    url: str = ("https://www.ebay.com/sch/"
                "i.html?_from=R40&_trksid"
                "=p2380057.m570.l1313&_nkw=shirt&_sacat=0")

    def __init__(self, cache_dir: Path = Path("/tmp")):
        """Stores vars"""

        self.cache_dir: Path = cache_dir
        # Creating a directory to cache files in
        self.cache_dir.mkdir(exist_ok=True, parents=True)

    def run(self,
            url: Optional[str] = None,
            out_path: Path = Path("/tmp/out.json")
            ) -> Path:
        """Scrapes Ebay"""

        # If url is not specified, use the default
        if url is None:
            url = self.url

        # Downloads a file and returns the path of the file
        path = self._download_file(self.url)
        # input(path)
        data = self._extract_data(path)

        return self._save_data(data, out_path)

    def _download_file(self, url: str) -> Path:
        """Downloads a file and returns a path"""

        # Remove bad characters from URL to make it a file
        url_file_name = url.replace("/", "").replace(":", "") + ".html"
        # Full path to the downloaded file
        # The numerator is a Path object which is a directory
        # If you divide a directory by a file name, it creates
        # the full path
        # Ex: Path("/tmp/") / "test.txt" -> "/tmp/test.txt"
        cache_path = self.cache_dir / url_file_name
        html = requests.get(url).text
        with cache_path.open("w") as f:
            f.write(html)

        return cache_path

    def _extract_data(self, path: Path) -> Dict[str, Tuple[float, float]]:
        """Extracts data from a path"""

        data = dict()

        with path.open() as f:
            soup = BeautifulSoup(f, "html.parser")
            # Get all sections
            for section in self._get_sections(soup):
                name = self._get_name(section)
                start, end = self._get_price(section)
                data[name] = (start, end)

        return data

    def _get_sections(self, soup: BeautifulSoup) -> List[BeautifulSoup]:
        """Takes in soup, returns all items/sections on the page"""

        return soup.find_all("div", {"class": "s-item__info clearfix"})

    def _get_name(self, section: BeautifulSoup) -> str:
        """Takes in a section, returns the name of the section"""

        return section.find("h3", {"class": "s-item__title"}).text

    def _get_price(self, section: BeautifulSoup) -> Tuple[float, float]:
        """Takes a section and gets start and end price range"""

        price_text = section.find("span", {"class": "s-item__price"}).text
        try:
            # Price is typically ex: $13.99
            start = float(price_text.replace("$", "").strip())
            return start, start
        # Couldn't convert because price is Ex: $12.74 to $14.99
        except ValueError:
            price_text = price_text.replace("$", "").replace(" ", "")
            price_start_str, price_end_str = price_text.split("to")
            return float(price_start_str), float(price_end_str)
            # return [float(x) for x in price_text.split("to")]

    def _save_data(self,
                   data: List[Dict[str, str]],
                   out_path: Path,
                   ):
        """"Saves the data into a JSON and returns the path"""

        # from pprint import pprint
        # pprint(data)
        # input()
        with out_path.open("w") as f:
            json.dump(data, f)


if __name__ == "__main__":
    EbayCollector().run()
