import requests
from bs4 import BeautifulSoup
import argparse
import sqlite3

def connect(dbname):
    conn=sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT,ADDRESS TEXT,PRICE INT,AMENITIES TEXT,RATING TEXT)")
    PRINT ("Table created successfully!")
    conn.close()

def insert_into_table(dbname,values):
    conn=sqlite3.connect(dbname)
    print("Inserted into table:"+ str(values))
    insert_sql="INSERT INTO OYO_HOTELS(NAME,ADDRESS,PRICE,AMENITIES,RATING) VALUES (?,?,?,?,?)"
    conn.execute(insert_sql,values)
    conn.commit()
    conn.close()

def get_hotel_info(dbname):
    conn=sqlite3.connect(dbname)
    cur=conn.cursor()
    cur.execute("SELECT * FROM OYO_HOTELS")

    table_data=cur.fetchall()
    for record in table_data:
        print(record)

parser=argparse.Arguementparser()
parser.add_arguement("__page_num_max",help="Enter the no. of pages to parse",type=int)
parser.add_arguement("__dbname",help="Enter the name of database",type=str)
args=parser.parse_args()

url="https://www.oyorooms.com/hotels-in-bhubaneswar/?page="
page_num_MAX=args.page_num_max
scraped_info_list=[]
connect(args.dbname)

for page_num in range(1,page_num_MAX):
    url_oyo=url+str(page_num)
    print("GET request for: "+url_oyo)
    req=requests.get(url_oyo)
    content=req.content

    soup=BeautifulSoup(content,"html.parser")

    all_hotels=soup.find_all("div",{"class":"hotelCardListing"})

    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"]=hotel.find("h3",{"class":"listingHotelDesciption__hotelName"}).text
        hotel_dict["address"]=hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["price"]=hotel.find("span",{"class":"listingPrice__finalPrice"}).text
        try:
            hotel_dict["rating"]=hotel.find("span",{"class":"hotelRating__ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"]=None

        parent_amenities_element=hotel.find("div",{"class":"amenityWrapper"})

        amenities_list=[]
        for amenity in parent_amenities_element.find_all("div",{"class":"amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())

        hotel_dict["amenities"]=','.join(amenities_list[:-1])

        scrapped_info_list.append(hotel_dict)
        insert_into_table(args.dbname,tuple(hotel_dict()))



get_hotel_info(args.dbname)

        
