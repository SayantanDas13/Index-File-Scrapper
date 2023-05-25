from bs4 import BeautifulSoup
import csv

# Read index.html file
with open('page20.html', 'r',encoding='utf-8') as file:
    html_content = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with the specified class
div_elements = soup.find_all('div', class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')

# Open data.csv in write mode
with open('data20.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Write header row
    writer.writerow(['Link', 'Title', 'Rating', 'Price', 'NoReviews'])

    # Iterate over each div element
    for div in div_elements:
        # Find img element for link
        img = div.find('img', class_='s-image')
        link = img['src'] if img else ''

        # Find span element for title
        span_title = div.find('span', class_='a-size-medium a-color-base a-text-normal')
        title = span_title.text if span_title else ''

        # Find span element for rating
        span_rating = div.find('span', class_='a-icon-alt')
        rating = span_rating.text if span_rating else ''

        # Find span element for price
        span_price = div.find('span', class_='a-price-whole')
        price = span_price.text if span_price else ''

        # Find span element for number of reviews
        span_reviews = div.find('span', class_='a-size-base')
        no_reviews = span_reviews.text if span_reviews else ''

        # Write the data to the CSV file
        writer.writerow([link, title, rating, price, no_reviews])
