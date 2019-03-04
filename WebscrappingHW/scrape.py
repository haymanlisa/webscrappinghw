from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


executable_path = {"executable_path": "/Users/lisahayman/Desktop/homework/WebscrappingHW/chromedriver"}
browser = Browser("chrome", **executable_path, headless=True)
    

def mars_scrape():
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)


    #browser.is_element_present_by_css("ul.item_list li.slide", wait_time=0.5)

    html = browser.html
    soup = bs(html, "html.parser")

    #using find will give you first css class
    body = soup.find(class_="article_teaser_body")
    bodytxt = body.get_text()
    
    title = soup.find(class_="content_title")
    titletxt = title.get_text()
    
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(url)
    full_image = browser.find_by_id("full_image")
    time.sleep(2)

    full_image.click()

    html = browser.html
    soup = bs(html, "html.parser")

    image_link = soup.find(class_="fancybox-image")

    feature1 = image_link.attrs["src"]

    base_url = "https://www.jpl.nasa.gov" + feature1
    
    
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")

    twitter = soup.find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    twittertxt = twitter.get_text()

    table_html = pd.read_html("https://space-facts.com/mars/")[0]
    mars_table = table_html.to_html()

    url = ["https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced",
    "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced",
    "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced",
    "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"]

    hemisphere_image_urls = []

    for u in url:


        browser.visit(u)

        full_image = browser.find_by_css(".open-toggle")

        full_image.click()

        html = browser.html

        soup = bs(html, "html.parser")

        title = soup.find(class_="title")

        titletxt = title.get_text()

        image_link = soup.find(class_="wide-image")["src"]

        image_url = "https://astrogeology.usgs.gov" + image_link

        per_image = {"title": titletxt, "img_url": image_url}

        hemisphere_image_urls.append(per_image)

    mars = { 'title': titletxt, 'body': bodytxt, 'twitter': twittertxt, 'feature_image': base_url, 'mars_table': mars_table, 'hemisphere': hemisphere_image_urls  

    return mars
print(mars_zcrape())
