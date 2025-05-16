import requests

url = "https://fakestoreapi.com/products"

try:
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        defective_products = []

        for product in products:
            defects = []

            if not product.get('title'):
                defects.append("Missing or empty 'title'")

            price = product.get('price')
            if price is None:
                defects.append("Missing 'price'")
            elif price < 0:
                defects.append("Negative 'price'")

            rating = product.get('rating')
            if rating:
                rate = rating.get('rate')
                if rate is None:
                    defects.append("Missing 'rating.rate'")
                elif rate > 5:
                    defects.append("'rating.rate' exceeds 5")
            else:
                defects.append("Missing 'rating'")

            if defects:
                defective_products.append({
                    'id': product.get('id'),
                    'title': product.get('title'),
                    'defects': defects
                })

        if defective_products:
            print("Defective Products Found:")
            for dp in defective_products:
                print(f"ID: {dp['id']}, Title: {dp['title']}, Defects: {', '.join(dp['defects'])}")
        else:
            print("No defects found in the product data.")
    else:
        print(f"API request failed with status code: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred while making the API request: {e}")
