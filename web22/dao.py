def get_categories():
    return [{
        "id": 1,
        "name": "Mobile"
    }, {
        "id": 2,
        "name": "Table"
    }]

def get_products(kw):
   products = [{
        "id": 1,
        "name": "iphone13",
        "price": 20000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png"
    }, {
        "id": 2,
        "name": "Galaxys23",
        "price": 20000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png"
    }, {
        "id": 3,
        "name": "Galaxys23",
        "price": 20000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png"
    }, {
        "id": 4,
        "name": "iphone13",
        "price": 20000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png"
    }, {
        "id": 5,
        "name": "Galaxys23",
        "price": 20000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png"
    }
   ]
   if kw:
       products = [p for p in products if p['name'].find(kw) >= 0]
   return products