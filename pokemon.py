from requests import get
from bs4 import BeautifulSoup
from time import sleep

the_page = ""

# mechanism for getting page  
base_url = "https://bulbapedia.bulbagarden.net"
curr_page = "/wiki/Ivysaur_(Pok%C3%A9mon)"

for i in range(5):
    the_page = get(base_url + curr_page).text

    #get link to next page
    soup = BeautifulSoup(the_page, "html.parser")

    #look for cool pokemon facts
    pkmn_name = (soup.title.text.split(' (')[0])

    type1 = soup.find_all("a", string="Type")[0].parent.parent.find_all('b')[1].text

    type2 = soup.find_all("a", string="Type")[0].parent.parent.find_all('b')[2].text


    print(f"Pokemon: {pkmn_name} Type: {type1} Type 2: {type2}")

    #find next page then iterate
    curr_page = soup.table.find_all("a")[5]['href']
    sleep(5)
