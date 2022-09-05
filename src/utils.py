from datetime import datetime


def normalize_stock_data(x: str):
    if "Lieferbar" in x:
        return "in stock"

    if "In Kürze wieder auf Vorrat" in x:
        return "in stock soon"

    if "Der Artikel ist nicht mehr im Sortiment" in x:
        return "out of product range"

    if "Halten Sie mich auf dem Laufenden" in x:
        return "out of stock for now"

    if "Begrenzter Vorrat:" in x:
        return f"{[s for s in x.split() if s.isdigit()][0]} left"

    return x


def get_now_timestamp():
    return datetime.now().strftime("%d-%b-%Y_%H-%M-%S")
