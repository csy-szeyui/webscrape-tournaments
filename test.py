from lxml import html
from bs4 import BeautifulSoup

file_path = 'result.html'

with open(file_path, 'r', encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

list_items = soup.find_all('span', class_="name")
print("Tournaments:")
print ("Tournament | Location | Singles Winner")
for item in range(len(list_items)):
    tourney_name = list_items[item].text.strip()
    
    venue_element = list_items[item].find_next('div', class_="bottom").find('span', class_="venue")
    events_element = list_items[item].find_parent('ul', class_="events")

    if (venue_element):
        venue = venue_element.text.strip(" | ")
        winner_element = (events_element).find('dl', class_="winner")
        if (winner_element != None and (winner_element).find('a') != None):
            winner_element = (winner_element).find('a')
            winner = winner_element.text.strip()
            print(f"{tourney_name} | {venue} | {winner}")

print (1)