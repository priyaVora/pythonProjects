import bs4 as bs
import urllib.request

class Product(object):

    def __init__(self, product_name, image, price, description):
        self.product_name = product_name
        self.images = image
        self.prices = price
        self.descriptions = description



    def __str__(self):
        product_representation = "%s:: %s:: %s :: %s" % (self.product_name, self.images, self.prices, self.descriptions)
        return str(product_representation)


    __repr__ = __str__


coffee_path= "https://www.walmart.com/ip/Coffee-Mate-Coffee-Creamer-French-Vanilla-15-oz/28831205"
shoe_path = "https://www.walmart.com/ip/Time-and-Tru-Women-s-Perforated-Twin-Gore-Slip-On-Sneaker/217301164"
bedding_path = "https://www.walmart.com/ip/Mainstays-Garden-Floral-Bed-in-a-Bag-Bedding-Set/492260898"
pillow_path = "https://www.walmart.com/ip/The-Pioneer-Woman-Ree-s-Garden-16x16-Decorative-Pillow/56129864"
earring_path = "https://www.walmart.com/ip/Woman-Nylon-Tassel-Pendant-Fish-Hook-Earrings-Royal-Blue-4-5-Inch-Length-Pair/316134870"
dress_path = "https://www.walmart.com/ip/Fashion-Striped-2-Pieces-Set-Camisole-High-Waist-Skirt/286508881"
backpack_path = "https://www.walmart.com/ip/17-Inch-Triple-Pocket-Cotton-Canvas-Backpack/55116211"
towels_path = "https://www.walmart.com/ip/Better-Homes-And-Gardens-Extra-Absorbent-6-Piece-Towel-Set/45799905"
lip_balm_path = "https://www.walmart.com/ip/Burt-s-Bees-Flavor-Crystals-100-Natural-Lip-Balm-Sweet-Orange-with-Beeswax-Fruit-Extracts-1-Tube/55039137"
wall_paper_path = "https://www.walmart.com/ip/Barn-Board-Grey-Thin-Plank-Wallpaper/103898937"

paths = [dress_path,towels_path,coffee_path,shoe_path,bedding_path,pillow_path,earring_path,backpack_path,lip_balm_path,wall_paper_path]
#sauce = urllib.request.urlopen(coffee_path).read()
#soup = bs.BeautifulSoup(sauce, "html.parser")
print(" ")

#print("Title: " + str(soup.title.text).replace("- Walmart.com", "") + "\n")

#span_tags = soup.find_all('span')

def get_price():
    price_data = ""
    for each_item in [item["aria-label"] for item in soup.find_all() if "aria-label" in item.attrs]:
        if "$" in each_item:
            price_data += str(each_item)
            #print( " " + str(each_item), end="", flush=True)
            break
    return price_data
def img():
    imgUrl = ""
    for divdata in soup.findAll('div', {"class": "prod-hero-image"}):
        for getatag in divdata.findAll('img', src=True):
            imgUrl = getatag['src']
            #print(getatag['src'])
    return imgUrl

def product_desc():
    data = ""
    for divdata in soup.findAll('div', {"class": "about-desc"}):
            data += str(divdata.text)
            #print(str(divdata.text))
    return data


product_list = []
for each_path  in paths:
    sauce = urllib.request.urlopen(each_path).read()
    soup = bs.BeautifulSoup(sauce, "html.parser")
    title = str(soup.title.text).replace("- Walmart.com", "")
    print("\n\nTitle: " + title + "\n")

    print("Price: ", end="",flush=True)
    price = get_price()
    print(price)
    print("\nImage: ", end="", flush=True)
    image = img()
    print(image)
    print("\nProduct Description: ", end="", flush=True)
    desc = product_desc()
    print(product_desc())

    newProduct = Product(title,image,price, desc)
    if newProduct not in product_list:
        product_list.append(newProduct)



print("--------------------------------------------")

for each_item in product_list:
   #print(each_item)



