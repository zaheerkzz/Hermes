# Hermes

I would like to change to this link
https://www.hermes.com/hk/en/category/women/shoes
( need to trigger the 'Load more items' to get the full list )
after getting the full list, would like the print out the list with json format (eg. name, price, image link, item link )


# Instructions:

before running script locally:
1- please check your chrome version and download relevent chromedriver from https://chromedriver.storage.googleapis.com/index.html?path=103.0.5060.134/

and place it into /driver drirectory in place of current driver


2- install python3
3- install pip

4- run command in terminal:  “pip install -r requirements.txt”  to install all dependencies
5- run script by running command: “python3 hermes.py”  or “python hermes.py”

6 – this will open broiwser and download data in JSON format


Code docs: 
please check code comments for changes:

you can change category URL on line 43 in code 
categoryURL = f"https://www.hermes.com/hk/en/category/women/shoes/"

and run code for downloading new category information
