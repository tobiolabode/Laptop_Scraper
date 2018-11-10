# Laptop_Scraper
A project that scrapes the prices of laptops using requests and beautifulsoup.


## Installation

```bash
git clone ...
```

## Usage
Change the page_link varible to choose the website you want to scrap
```python
page_link = www.yourwebsite.com
```
Change the class where the wanted elements are found.
Change the name and price variables to the elements of the page 
```python
for info in page_content.find_all(class_= 'example_class'):
    Name = info.h2.text
    print(Name)

    Price = info.p.span.text
    print(Price, end='\n  \n')

    records.append((Name, Price))
```


Run the code below and it will produce an csv file 
```
python demo.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
