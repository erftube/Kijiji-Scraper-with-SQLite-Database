import requests
from bs4 import BeautifulSoup
from db import DB


def scrape_kijiji(search_url, max_results=None):
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/91.0.4472.124 Safari/537.36")
    }
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve data")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    listings = []

    # Find all title containers using the data-testid attribute.
    title_containers = soup.find_all("h3", attrs={"data-testid": "listing-title"})

    # Limit the number of results if max_results is specified.
    if max_results is not None:
        title_containers = title_containers[:max_results]

    for container in title_containers:
        # Extract title and link from the anchor tag.
        link_tag = container.find("a", attrs={"data-testid": "listing-link"})
        title = link_tag.text.strip() if link_tag else "No Title"
        link = link_tag["href"] if link_tag and link_tag.has_attr("href") else ""
        # Prepend base URL if the link is relative.
        if link and not link.startswith("http"):
            link = "https://www.kijiji.ca" + link

        # Find the price container.
        price_container = container.find_previous_sibling("div", attrs={"data-testid": "listing-price-container"})
        price_tag = price_container.find("p", attrs={"data-testid": "listing-price"}) if price_container else None
        price = price_tag.text.strip() if price_tag else "No Price"

        listings.append({
            "title": title,
            "price": price,
            "link": link
        })

    return listings


if __name__ == "__main__":
    db = DB()
    search_url = "https://www.kijiji.ca/b-room-rental-roommate/canada/c36l0"
    # Change max_results to the number you want or set it to None to scrape all listings.
    results = scrape_kijiji(search_url, max_results=20)

    for idx, item in enumerate(results, 1):
        print(f"{idx}. {item['title']} - {item['price']}")
        print(f"   {item['link']}")
        print("-")
        db.insert_item(item["title"], item["price"], item["link"])

    db.close()
