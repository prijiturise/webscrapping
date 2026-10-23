
import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/130.0.0.0 Safari/537.36"
    )
}


def get_headlines():
    try:
        response = requests.get(
            URL,
            headers=HEADERS,
            timeout=10
        )

        # Check whether the request succeeded
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Primary selector: inspect the BBC page and verify this.
        items = soup.select('h2[data-testid="card-headline"]')

        # Fallback if the primary selector finds nothing
        if not items:
            items = soup.select(
                'a[href*="/news/articles/"] h2'
            )

        headlines = []
        seen = set()

        for item in items:
            headline = item.get_text(" ", strip=True)

            if headline and headline not in seen:
                headlines.append(headline)
                seen.add(headline)

            if len(headlines) == 5:
                break

        if not headlines:
            print("No headlines found. Check the HTML selectors.")
            return

        for number, headline in enumerate(headlines, start=1):
            print(f"{number}. {headline}")

        if len(headlines) < 5:
            print(
                f"\nOnly {len(headlines)} unique headlines were found."
            )

    except requests.exceptions.RequestException as error:
        print(f"Could not fetch the news page: {error}")


if __name__ == "__main__":
    get_headlines()
