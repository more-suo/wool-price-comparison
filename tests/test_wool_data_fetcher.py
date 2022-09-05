from src.wool_data_fetcher import WoolDataFetcher

wollplatz = WoolDataFetcher("https://www.wollplatz.de/wolle")


def test_get_article_links():
    for url in [
        "https://www.wollplatz.de/wolle/stylecraft/stylecraft-special-dk",
        "https://www.wollplatz.de/wolle/go-handmade/go-handmade-boheme-velvet-double",
        "https://www.wollplatz.de/artikel/45304/lana-grossa-meilenweit-100-piccolo.html",
        "https://www.wollplatz.de/wolle/pink-label/pink-label-hugg",
        "https://www.wollplatz.de/wolle/katia/katia-alaska",
        "https://www.wollplatz.de/wolle/rico/rico-luxury-volumi",
    ]:
        assert url in wollplatz.article_urls
