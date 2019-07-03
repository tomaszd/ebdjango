'''
Created on 24 lut 2016

@author: opera
'''
from BeautifulSoup import BeautifulSoup
import requests


def get_details_from_single_card(soup, full_url):
    try:
        expansion_set = str(soup).split("Expansions/")[1].split("\"")[0]
    except:
        expansion_set = "brak Expansion Set!"
        # PRICE
    try:
        price = soup.findAll("td", text="Price Trend")[0].next.text.split(" &")[0] + " EURO"
    except:
        price = "dziwaczna"

    card_details = {
        "href": full_url,
        "expansion_set": expansion_set,
        "price": price}
    return [card_details]


def get_singles_details_MCM(cardname=None):
    url = "https://www.cardmarket.com/en/Magic/Products/Search?searchString="
    if not cardname:
        print "no card specified"
        return []
    full_url = url + cardname
    full_url = full_url.replace(" ", "+")
    print "Full search URL : " + "\"" + full_url + "\""
    try:
        data = requests.get(full_url)
        soup = BeautifulSoup(data.text)
    except:
        print "Problems for {}".format(full_url)
        return []
    list_of_cards = []

    if "Price Trend" in str(soup):
        print "Only one Card expansion"
        return get_details_from_single_card(soup, full_url)

    rows_with_products = [row for row in soup.findAll("div", {"class": "row no-gutters"}) if row.has_key("id")]
    row_with_actual_cards = []
    for row_product in rows_with_products:
        try:
            if "#" in row_product.contents[3].text:
                row_with_actual_cards.append(row_product)
        except:
            print "blad panie !"

    # dodatek=str(row_with_actual_cards[4].contents[3]).split("Singles/")[1].split("/")[0]
    # cena=str(row_with_actual_cards[4].contents[5]).split("\">")[1].split("&")[0].strip()



    for single_card_row in row_with_actual_cards:

        # expansion Set
        try:
            expansion_set = str(single_card_row.contents[3]).split("Singles/")[1].split("/")[0]
        except:
            expansion_set = "brak Expansion Set!"
        # PRICE
        try:
            price = str(single_card_row.contents[5]).split("\">")[1].split("&")[0].strip()
        except:
            price = "dziwaczna"
        try:
            href = "https://www.cardmarket.com" + str(single_card_row.contents[3]).split("href=\"")[1].split("\"")[0]
        except:
            href = "Errors"

        card_details = {

            # "href": base_url + href.split("\"")[1],
            # "href": URL,
            # "comment": URL,
            # "singles": singles,
            # "avail": avail,
            "search_href=": full_url,
            "href": href,
            "expansion_set": expansion_set,
            "price": price}

        list_of_cards.append(card_details)
    return list_of_cards  # dead code below:


"""
for row in range(len(soup.findAll('tr')))[1:-1]:
    card_details = {}
    # print "checking ",full_url
    try:
        thumb, expan, rarity, href, URL, singles, avail, price = soup.findAll(
            'tr')[row].findAll('td')
    except:
        print "just one occurence for {}".format(full_url)
        card_details = {
            "href": full_url,
            "comment": "1 occurence",
            "singles": False,
            "avail": False,
            "expansion_set": "strange",
            "price": "strange"}
        return [card_details]
    if price.text == "N/A":
        print "Warning! N/A for price {} .{}".format(price, href)
        continue
    if "Playmat" in str(href):
        print "Warning! This is Playmat , Skipping...", href
        continue
    if "Promo" in str(href):
        print "Warning! This is PROMO price , Skipping...", href
        continue
    href = str(href).replace('<td>', '').replace('</td>', '')
    cardname_in_URL = str(URL).split("\">")[1].replace("</a></td>", "")

    # soup.findAll("div", {"class": "row no-gutters"})[1].contents[5].text


    URL = "https://www.cardmarket.com" + \
          str(URL).replace('<td>', '').replace('</td>', '').lstrip("'<a href=\"").rstrip("</a>").split("\">")[0]
    singles = str(singles).replace('<td>', '').replace('</td>', '')
    # e.g. Chill Haunting != Chill
    if cardname_in_URL.lower() != cardname.lower():
        continue
    if "Playmats" in singles:
        continue
    avail = str(avail).replace('<td>', '').replace('</td>', '')
    if "0" == avail:
        continue
    price = str(price).replace('<td>', '').replace(
        '</td>', '').split(">")[1].split("<")[0].replace("&#x20AC;", "").strip()
    try:
        expansion_set = expan.findAll("a")[0].attrs[0][1].split("/")[-1]
    except:
        print"There is no expansion ready"
        continue

    if expansion_set in ["Alpha", "Beta", "Unlimited", "Player-Rewards-Promos", u'Prerelease-Promos']:
        print "Expansion set is {} .skipping then ...for {}".format(expansion_set, cardname)
        continue
    if "Expedition" in expansion_set:
        continue
    if "WCD" in expansion_set:
        print "Expansion set is {} .skipping then ...HIS gold bordered {}".format(expansion_set,
                                                                                  cardname)
        continue
    if URL:
        print "URL: ", URL, " Price: ", price
    card_details = {

        # "href": base_url + href.split("\"")[1],
        "href": URL,
        "comment": URL,
        "singles": singles,
        "avail": avail,
        "expansion_set": expansion_set,
        "price": price}

    list_of_cards.append(card_details)
if list_of_cards == []:
    print "Nie ma!"
return list_of_cards
"""


def get_best_expansion(list_of_cards):
    """This is getting lowest price dict. the cheapest expansion set"""
    #   for single_detail in list_of_cards:
    #     print single_detail['expansion_set'] , " : ", single_detail['price']
    a = 0
    if len(list_of_cards) == 1:
        return list_of_cards[0]
    newlist_sorted_by_price = sorted(list_of_cards,
                                     key=lambda k: float(k['price'].replace(",", ".")))
    lowest_price_single = newlist_sorted_by_price[0]
    return lowest_price_single


def get_price_trend(lowest_price_single):
    """get price tend form sites like :
     https://www.magiccardmarket.eu/Products/Singles/Future+Sight/Tarmogoyf"""
    # 'href': '<a href="/Products/Singles/Magic+2012/Manabarbs">Manabarbs</a>' -> /Products/Singles/Magic+2012/Manabarbs

    # return lowest_price_single

    final_single_url = lowest_price_single["href"]
    price_trend = 0
    try:
        data_for_single = requests.get(final_single_url)
        soup = BeautifulSoup(data_for_single.text)
        price_trend = soup.findAll("td", text="Price Trend")[0].next.text.split(" &")[0] + " EURO"
    except:
        print "problems for {}".format(final_single_url)
    lowest_price_single['price_trend'] = price_trend
    return lowest_price_single


def get_price_and_set_MagicCardMarket(cardname):
    """ function return dict with all details about card in form:

    {'comment': '',
     'singles': 'Singles',
     price_trend': u'113,50 EURO'
     'price': '0,02 EURO',
     'avail': '1379',
     'href': 'https://www.magiccardmarket.eu/Products/Singles/Magic+2012/Manabarbs',
     'expansion_set': 'Magic+2012'}
    """
    lowest_price_single = get_best_expansion(get_singles_details_MCM(cardname))
    lowest_price_single = get_price_trend(lowest_price_single)
    return lowest_price_single


if __name__ == "__main__":
    print get_price_and_set_MagicCardMarket("Puresteel Paladin")
    print get_price_and_set_MagicCardMarket("Tarmogoyf")
    # print get_price_and_set_MagicCardMarket("doran, the siege tower")
    # print get_price_and_set_MagicCardMarket("flooded strand")
    # print get_price_and_set_MagicCardMarket("Chill")
    # print get_price_and_set_MagicCardMarket("Gilt-leaf palace")
    # print get_price_and_set_MagicCardMarket("Fire-lit thicket")
