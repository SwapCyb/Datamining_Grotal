from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient
import time
import os
os.startfile(r"C:\Program Files\MongoDB\Server\3.6\bin\mongod.exe")            # Starting the mongodb
time.sleep(5)
os.startfile(r"C:\Program Files\MongoDB\Server\3.6\bin\mongo.exe")
Client = MongoClient()                                                         # Stating Client
coaching_info = Client.mydatabase
grotal_coaching5 = coaching_info.grotal_coaching5
ch = "C:\chromedriver"
driver = webdriver.Chrome(ch)                                                  # Calling the driver
driver.implicitly_wait(30)
driver.maximize_window()
Coaching_name = []
Address = []
Address2 = []
Contact = []
ConTact = []
Contact_full = []
Phone_no = []
Mobile_no = []
Email = []
Contact_Person = []
b = 0
line1 = []
line2 = []
landmark = []
add = []


URL = []


def site(i):                                                                                        # Function to iterate between different
    driver.get("https://www.grotal.com/Indore/Coaching-C90A0P" + str(i) + "A0/")                    # pages of the site
    a = driver.find_elements_by_css_selector(".area.cursor")
    print(a)
    length = len(a)
    print(length)
    return length


def scrapper(lth, n):                                                                               # Function to scrap data
    for k in range(lth):
        g = driver.find_element_by_id("divTitle" + str(k + n)).get_attribute("innerText")
        Coaching_name.append(g)
        driver.find_element_by_id("divTitle" + str(k + n)).find_element_by_class_name("cursor").click()
        h = driver.find_element_by_class_name("label-txt").get_attribute("innerText")
        Address.append(h)
        p = driver.current_url
        URL.append(p)

        try:                                                                                         #code for scraping phone numbers
            j = driver.find_element_by_class_name("ph-no").get_attribute("innerText")
            if (len(j) == 11) and ("0731" in j):
                Phone_no.append(j)
                Contact_full.append(j)
                Contact.append(j[4:])
            elif len(j) == 11:
                Mobile_no.append(j)
                Contact_full.append(j)
                Contact.append(j[1:])
            else:
                Contact_full.append(j)
                Contact.append(j)

        except NoSuchElementException:
            Contact.append("")
            Contact_full.append("")
        d = driver.find_element_by_xpath('//*[@id="printDiv"]/div[5]/div').get_attribute("innerText")
        if d == 'NA':
            Contact_Person.append("")
        else:
            Contact_Person.append(d)
        e = driver.find_element_by_xpath('//*[@id="printDiv"]/div[10]/div').get_attribute("innerText")
        if e == 'NA':
            Email.append("")
        else:
            Email.append(e)

        print("\n")
        driver.back()


def address_edit(lin1, lin2, land_mark, array, array2):                         # Function to edit the address
        land_mark = []
        lin1 = []
        lin2 = []
        for j in array:
            add_ress = {}
            add1 = j.split(',')
            lin1.append(add1[0])
            lin2.append(add1[1:])
            for s in add1:
                if ('Near' in s) or ('Opposite' in s) or ('Behind' in s) or ('Above' in s):
                    land_mark.append(s)

            add_ress = {'city': 'indore',
                        'state': 'M.P',
                        'country': 'India',
                        'pincode': '',
                        'landmark': land_mark,
                        'address line1': lin1,
                        'address line2': lin2,
                        'latitude': '',
                        'longitude': ''}
            array2.append(add_ress)
            land_mark = []
            lin1 = []
            lin2 = []
        return array2


def phone_edit(phone_no, mobile_no, array1):                                # Editing of Phone number
    dict1 = {}
    extent_phone = "0731"
    extent_mobile = "+91"
    for i in Contact_full:
        if i in phone_no:
            dict1 = {'ext': extent_phone,
                    'phone': i[4:],
                    'source': 'Grotal'}
        elif i in mobile_no:
            dict1 = {'ext': extent_mobile,
                    'phone': i[1:],
                    'source': 'Grotal'}
        else:
            dict1 = {'ext': '',
                     'phone': '',
                     'source': 'Grotal'}
        array1.append(dict1)

    return array1


def database():                                                                        # Creating the Database
    address = address_edit(line1, line2, landmark, Address, Address2)
    phone = phone_edit(Phone_no, Mobile_no, ConTact)
    post_data = {}
    for i in range(len(Coaching_name)):
        post_data = {'name': Coaching_name[i],
                    'source': URL[i],
                    'phones': phone[i],
                    'emails': Email[i],
                    'contact person': Contact_Person[i],
                    'websites': '',
                     'address': address[i],
                     'ratings': '',
                     'reviews': '',
                     'courses': '',
                     'tags': '',
                     'directions': ''}
        grotal_coaching5.insert_one(post_data)


def main(m):                                                                                  # main Function
    for q in range(1, 5):
        time.sleep(5)
        site(q)
        scrapper(site(q), m)
        m = site(q) + m
    database()
    driver.quit()


main(b)



