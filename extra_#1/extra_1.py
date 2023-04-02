import requests
from bs4 import BeautifulSoup
import json
import sys

def main():
    
    url = sys.argv[1]

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")


    properties = []

    for property in soup.find_all("div", class_="search-results-product"):
        title = property.find("a", class_="product-title-link").text.strip()
        url = property.find("a", class_="product-title-link")["href"]
        price = property.find("span", class_="product-price-value").text.strip()
        area = property.find("div", class_="product-feature-area-value").text.strip()
        rooms = property.find("div", class_="product-feature-rooms-value").text.strip()
        floor = property.find("div", class_="product-feature-floor-value").text.strip()
        description = property.find("div", class_="product-description").text.strip()
        image_urls = [img["src"] for img in property.find_all("img", class_="lazy")]

        property_dict = {
            "title": title,
            "url": url,
            "price": price,
            "area": area,
            "rooms": rooms,
            "floor": floor,
            "description": description,
            "image_urls": image_urls
        }

        properties.append(property_dict)

    with open("properties.json", "w") as f:
        json.dump(properties, f)
    

if __name__ == "__main__":
    main()
