from bs4 import BeautifulSoup
import requests
import pandas as pd
page_link = "https://www.johnlewis.com/browse/electricals/laptops-macbooks/view-all-laptops-macbooks/price=600-800/_/N-a8fZ6lq8?showInStockOnly=false&sortBy=rating"
#fetch conent from url
page_response = requests.get(page_link, timeout=5)
# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")

# extract all html elements where price is stored
# info = page_content.find(class_= 'product-card__info')

records = []

for info in page_content.find_all(class_= 'product-card__info'):
    Name = info.h2.text
    print(Name)

    Price = info.p.span.text
    print(Price, end='\n  \n')

    records.append((Name, Price))


print(records)
df = pd.DataFrame(records, columns=['Name', 'Price'])
print(df)
df.to_csv("laptops.csv", index=False, encoding="utf-8")
