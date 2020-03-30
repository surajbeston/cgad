from django.shortcuts import render
from fonoapi import FonoAPI
from .models import OriginalSmartphone, ScrapedLaptop, OriginalLaptop
from django.http import HttpResponse
import requests
import string
import logging


def phoneAssembler(request):
    fon = FonoAPI('686d5f5b0a9a5c25bb58612171cb23900a8cbd480b001c20')

    brands = ["nokia", "apple", "prolink", "oppo", "xiaomi", "samsung", "vivo", "huawei", "gionee", "oneplus", "lava", "micromax", "lg", "microsoft", "realme", "honor", "google", "panasonic", "tecno", "alcatel"]

    for brand in brands:
        devices = fon.getlatest(brand, limit=100)
        devices = devices.list_of_dicts()
        for device in devices:
            print (device)
            obj = OriginalSmartphone(data = device)
            obj.save()
    return HttpResponse("Done, Done")

def laptopAssembler(request):
    scraped_laptops = ScrapedLaptop.objects.all()
    names = []
    for scraped_laptop in scraped_laptops:
        name_ = scraped_laptop.data["name"]
        name = ""
        for letter in name_:
            if letter in string.punctuation:
                break
            name +=letter
        names.append(name)

    generic_words = ["gaming","i3", "i5",  "i7", "i9", "10th", "9th", "8th", "7th", "intel", "laptop", "notebook", "core"]
    cleaned_names = []
    for name in names:
        name = name.split(" ")[:4]
        for word in name:
            if word.lower() in generic_words:
                popped = name.pop(name.index(word))

        cleaned_names.append(' '.join(name))

    request_count = 1
    for cleaned_name in cleaned_names:
        print (cleaned_name)
        laptop_objs = ScrapedLaptop.objects.filter(data__name__icontains = cleaned_name)
        non_validator = True
        for laptop_obj in laptop_objs:
            if laptop_obj.searched == True:
                non_validator = False
        print("Searched: " + str(not non_validator))
        if non_validator == False:
            print("reached here")
            if request_count <= 150:
                request_count += 1
                r = requests.post('https://noteb.com/api/webservice.php', data={'apikey': "112233aabbcc", 'method': "get_model_info", 'param[model_name]': cleaned_name})
                data = r.json()
                if len(str(data)) > 800:
                    real_name = data['result']['0']['model_info'][0]['name']
                    print("Data available.")
                    print(real_name)
                    obj = OriginalLaptop(data = data)
                    obj.save()
                    in_scrape = ScrapedLaptop.objects.filter(data__name__icontains = real_name)
                    print(len(in_scrape))
                    if (len(in_scrape) > 0):
                        for laptop in in_scrape:
                            laptop.searched = True
                            laptop.save()
                else:
                    print("No data available.")
                print("message : " + data["message"])
                print ("")
                print ("*********************************")
                print ("")
    return HttpResponse("Scraped For Now....")
