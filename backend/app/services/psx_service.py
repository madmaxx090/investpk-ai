import requests
from bs4 import BeautifulSoup


class PSXService:
    BASE_URL = "https://dps.psx.com.pk"

    def __init__(self):
        self.session = requests.Session()

    def get_symbols(self):
        """
        Returns only listed companies (excluding ETFs and debt).
        """

        url = f"{self.BASE_URL}/symbols"

        response = self.session.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        companies = []

        for item in data:
            if not item["isETF"] and not item["isDebt"]:
                companies.append({
                    "symbol": item["symbol"],
                    "name": item["name"],
                    "sector": item["sectorName"]
                })

        return companies

    def search_company(self, query: str):
        """
        Search companies by symbol or company name.
        """

        query = query.strip().lower()

        return [
            company
            for company in self.get_symbols()
            if query in company["symbol"].lower()
            or query in company["name"].lower()
        ]

    def get_market_watch(self):
        """
        Returns the live Market Watch as structured JSON.
        """

        url = f"{self.BASE_URL}/market-watch"

        response = self.session.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table")

        if table is None:
            return []

        tbody = table.find("tbody")

        if tbody is None:
            return []

        rows = tbody.find_all("tr")

        stocks = []

        for row in rows:

            cols = row.find_all("td")

            if len(cols) < 10:
                continue

            try:
                stock = {
                    "symbol": cols[0].get_text(strip=True),
                    "sector": cols[1].get_text(strip=True),
                    "listed_in": cols[2].get_text(strip=True),
                    "ldcp": cols[3].get_text(strip=True),
                    "open": cols[4].get_text(strip=True),
                    "high": cols[5].get_text(strip=True),
                    "low": cols[6].get_text(strip=True),
                    "current": cols[7].get_text(strip=True),
                    "change": cols[8].get_text(strip=True),
                    "change_percent": cols[9].get_text(strip=True),
                }

                stocks.append(stock)

            except Exception:
                continue

        return stocks

    def get_top_performers(self):
        """
        Returns Top Active, Top Gainers and Top Losers
        as structured JSON.
        """

        url = f"{self.BASE_URL}/performers"

        response = self.session.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        tables = soup.find_all("table")

        result = {
            "top_active": [],
            "top_gainers": [],
            "top_losers": []
        }

        sections = [
            "top_active",
            "top_gainers",
            "top_losers"
        ]

        for section, table in zip(sections, tables):

            tbody = table.find("tbody")

            if tbody is None:
                continue

            rows = tbody.find_all("tr")

            for row in rows:

                cols = row.find_all("td")

                if len(cols) < 4:
                    continue

                try:
                    stock = {
                        "symbol": cols[0].get_text(strip=True),
                        "price": cols[1].get_text(strip=True),
                        "change": cols[2].get_text(strip=True),
                        "volume": cols[3].get_text(strip=True),
                    }

                    result[section].append(stock)

                except Exception:
                    continue

        return result

    def get_kse100_chart(self):
        """
        Returns KSE100 historical chart data.
        """

        url = f"{self.BASE_URL}/timeseries/int/KSE100"

        response = self.session.get(url, timeout=10)
        response.raise_for_status()

        return response.json()

    def get_stock(self, symbol):
        """
        Placeholder for individual stock details.
        """

        return {
            "symbol": symbol.upper(),
            "message": "Stock details will be implemented next."
        }