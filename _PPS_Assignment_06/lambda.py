import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.example.com/emails"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

emails = []
while True:
    email_elements = soup.find_all("div", class_="email")
    for email_element in email_elements:
        subject = email_element.find("span", class_="subject").text
        body = email_element.find("p", class_="body").text
        label = email_element.find("span", class_="label").text

        email = {"subject": subject, "body": body, "label": label}
        emails.append(email)

    next_page_element = soup.find("a", class_="next-page")
    if next_page_element:
        next_page_url = next_page_element["href"]
        response = requests.get(next_page_url)
        soup = BeautifulSoup(response.content, "html.parser")
    else:
        break
        
df = pd.DataFrame(emails)
df.to_csv('emails.csv', index=False)
