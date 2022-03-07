
from bs4 import BeautifulSoup
import requests,json
import json
from pprint import pprint
pical_url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="
page_1=requests.get(pical_url)
soup=BeautifulSoup(page_1.text,"html.parser")
a=soup.find_all("div",class_="_1EI9")
# print(a)    
def pical_1():
    pical_url1="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="
    page_2=requests.get(pical_url1)
    soup_1=BeautifulSoup(page_1.text,"html.parser")
    # pprint(soup_1)
    main_data=soup_1.find("div",class_="_3RA-")
    # print(main_data)
    pical_name=main_data.find_all("div",class_="UGUy")
    # pprint(pical_name)
    pical_praic=main_data.find_all("div",class_="_2bo3")
    # pprint(pical_praic)
    pical_link=main_data.find_all("div",class_="_3nWP")
    # pprint(pical_link)
    link=main_data.find_all("div",class_="_3WhJ")
    # print(link)
    i=0
    posisition=0
    list1=[]
    while i<len(pical_link):
        posisition+=1
        pical_name1=link[i].get_text()
        # pprint(pical_name)
        pical_price1=pical_praic[i].span.get_text()
        # pprint(pical_price1)
        pical_link1=link[i].a["href"]
        # pprint(pical_link1)
        pical_link2="https://paytmmall.com/"+pical_link1
        # pprint(pical_link2)
        i=i+1
        dic={"posisition":posisition,"pical name":pical_name1,"pical praic":pical_price1,"pical link":pical_link1}
        list1.append(dic)
    with open("my_pical_file.json","w")as file1:
        json.dump(list1,file1,indent=3)
    
pical_1()   
