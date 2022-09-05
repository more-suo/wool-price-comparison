import requests
from typing import List, Dict

from bs4 import BeautifulSoup
import pandas as pd

from .utils import normalize_stock_data, get_now_timestamp


class WoolDataFetcher:
    def __init__(self, url: str):
        self.__url = url
        self.__article_urls = self.__get_all_article_links()

    def __get_article_links(
        self, page_count: int, tag: str, class_name: str
    ) -> List[str]:
        r = requests.get(self.__url + f"?page={ page_count }")
        parsed = BeautifulSoup(r.text, "html.parser")
        return [title.findChild()["href"] for title in parsed.find_all(tag, class_name)]

    def __get_all_article_links(
        self, tag: str = "h3", class_name: str = "productlist-title"
    ) -> List[str]:
        # print("get_all_article_links")
        all_links = []
        page_count = 1

        while (
            all_links[
                -len(
                    temp_links := self.__get_article_links(page_count, tag, class_name)
                ) :
            ]
            != temp_links
            or len(all_links) == 0
        ):
            all_links += temp_links
            page_count += 1
            # print(page_count)

        return all_links

    def get_article_data(self) -> Dict[str, Dict[str, str]]:
        print("get_article_data")
        articles_data = {}
        counter = 0

        for url in self.__article_urls:
            parsed = BeautifulSoup(requests.get(url).text, "html.parser")
            article_data = {
                k: "no data"
                for k in ["Stock", "Price", "Needle strength", "Compilation"]
            }
            article_data["URL"] = url

            if (
                stock := parsed.find(
                    "div", {"id": "ContentPlaceHolder1_upStockInfoDescription"}
                )
            ) is not None:
                article_data["Stock"] = normalize_stock_data(stock.text)

            if (
                price := parsed.find("span", class_="product-price-amount")
            ) is not None:
                article_data["Price"] = price.text

            if (needle := parsed.find("td", string="Nadelstärke")) is not None:
                article_data["Needle strength"] = needle.find_next("td").text

            if (
                compilation := parsed.find("td", string="Zusammenstellung")
            ) is not None:
                article_data["Compilation"] = compilation.find_next("td").text

            title = parsed.find("h1", {"id": "pageheadertitle"}).text
            articles_data[title] = article_data

            counter += 1
            # print(f"{counter}/{len(self.__article_urls)}")

        return articles_data

    def safe_data(self):
        data = self.get_article_data()
        pd.DataFrame(data).transpose().to_csv(
            f"output/wool_data_{get_now_timestamp()}.csv"
        )

    @property
    def url(self):
        return self.__url

    @property
    def article_urls(self):
        return self.__article_urls
