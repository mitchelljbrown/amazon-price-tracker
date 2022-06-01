# amazon-price-tracker

## Overview
Growing up I have always loved Music. After discovering my late grandfathers record collection (~2010), I was hooked on listening to and collecting vinyl records. As the years have passed, vinyl records have become more and more popular allowing record companies to release high quality 180g vinyl records. This increase in quality along with the increase in the price of vinyl as a material has made record collecting a very expensive hobby. 

After years of shopping at various record stores and amazon.ca, I noticed the price of vinyl records can fluctuate alot. I wrote this module to allow users to track the price of their favourite vinyl records. This module is also equiped to deal with any amazon item you wish to track. Within function arguments, you can specify certain notification criterea. Currently, these are the options:

- when the price drops more than a specified amount
- when the record becomes available if currently unavailable
- if the price drops below a set amount

By default, if any of the above criterea are met, an email will be generated and sent to the user which contains:

1. Inforation regarding the price drop/record availabilty
2. Link to the product
3. Attachment: plot of date vs. price history of item
4. Attachment: plot of date vs. price history of all watched items

![](https://github.com/mitchelljbrown/amazon-price-tracker/blob/main/images/email_screenshot.PNG)

![](https://github.com/mitchelljbrown/amazon-price-tracker/blob/main/images/graph_screenshot.PNG)

## Installation

First make sure the module file "price_tracker.py" is downloaded and in your project working directory. Then open a terminal in your working directory.

```console
pip install price_tracker
```

## Running The Project

after installing `amazon-price-tracker` you need to privide a list or dictionary of items you want to track. A dictionary is used to increase readability when supplying many items. The dictionary should consist of "item name" keys and "link" values like the following. A list of urls can be used instead if prefered. 

1. Specify email (required) and emial password (optional) as string in the `email_setup()` function

```python
import price_tracker as pt

pt.email_setup(email, password)
```
2. Provide list of items to be scraped and tracked. These can be in dictionary or list format

```python
# Dictionary
items = {"Weezer-Blue-Ablum":'https://www.amazon.ca/...',
        "Weezer-Pinkerton":'https://www.amazon.ca/...',
        "Fleet-Foxes-Crack-Up":'https://www.amazon.ca/...'}

# List
items = ('https://www.amazon.ca/...',
        'https://www.amazon.ca/...',
        'https://www.amazon.ca/...')
```

3. Run the main funciton
```
pt.price_tracker(items)
```
The main function contains a while loop set to "True" and executes every x seconds. This is specified by the user as an argument and is 86400 (1 day) by default.

## Features
```python
import price_tracker as pt

# create a csv to store scraped data
pt.create_csv()

# scrape data and append to csv
pt.update_price()

# send an email the user
pt.send_mail(type='drop')   # specify whether you want to be notified by a price drop or item availability

# update .csv and send email
pt.update_and_email()

# master function to scrape data and send an email if the price of an item drops or becomes available
pt.price_tracker(freq='day')    # set the frequency the prices are checked. Enter 'day', 'week', or specify in seconds
```

## Dev Dependancies

For scraping amazon.ca and storing and viaulizing data
- BeautifulSoup
- requests
- time
- datetime
- pandas
- seaborn
- matplotlib.pyplot
- csv
- os

For Sending Emails
- smtplib
- email.message
- imghdr
