from django.shortcuts import render
from fonoapi import FonoAPI
from .models import OriginalSmartphone, ScrapedSmartphone, ScrapedLaptop, OriginalLaptop, AccessLog, RequestLog
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import string
import logging
import json 
import random
import datetime
import os, os.path

import whoosh.index as index
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from operator import itemgetter
import locale
locale.setlocale(locale.LC_MONETARY, 'en_IN')

text_user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"

vendor = ["dealayo.com", "sastodeal.com", "pasalnepal.com", "reddoko.com", "thulo.com", "smartdoko.com", "muncha.com", "okdam.com", "daraz.com.np", "neostore.com.np", "evostore.com.np", "olizstore.com"]

vendor_images = ["dealayo.png", "sastodeal.png", "pasalnepal.png", "reddoko.png", "thulo.png", "smartdoko.png", "muncha.gif", "okdam.jpg", "daraz.png", "neostore.png", "evostore.png", "olizstore.png"]

@csrf_exempt
def initiateSession(request):
    sessionId = "".join([random.choice(string.ascii_letters + string.digits) for i in range(50)])
    data = AccessLog(sessionId =sessionId, client_ip = request.META["REMOTE_ADDR"], user_agent = request.headers["user_agent"])
    data.save()
    return JsonResponse({"sessionId": sessionId})


@csrf_exempt
def phone_search(request):
    if request.method == "POST":
        print (request.body)
        data = json.loads(request.body)
        sessionId = data.get("sessionId")
        print (sessionId)
        decision_arr = securer(sessionId, request.headers["user_agent"])
        if decision_arr[0] == False:
            return JsonResponse(decision_arr[1])
        else: 
            phone_name = data.get("phone_name")
            if phone_name == None:
                return JsonResponse({"error": "no phone_name"})
            ix = index.open_dir("index")
            qp = QueryParser("phone_name", schema = ix.schema)
            q = qp.parse(phone_name)  
            retrieved_phones_ = []            
            with ix.searcher() as s:    
                retrieved_phones = s.search(q) 
                if len(retrieved_phones) != 0:
                    for retrieved_phone in retrieved_phones:
                        retrieved_phones_.append(retrieved_phone["phone_name"])
    
            retrieved_phones__ = []
            q = qp.parse(' '.join(phone_name.split(" ")[1:]))
            with ix.searcher() as s:
                retrieved_phones = s.search(q)
                if len(retrieved_phones) != 0:
                    for retrieved_phone in retrieved_phones:
                        retrieved_phones__.append(retrieved_phone["phone_name"])

            
            retrieved_phones = []
            total_phones = retrieved_phones__ + retrieved_phones_

            print (retrieved_phones_)
            print (retrieved_phones__)    

            for phone_ in total_phones:
                if phone_ not in retrieved_phones:
                    retrieved_phones.append(phone_)            
            print (len(retrieved_phones))

            # special case for iphone X
            if phone_name == "Apple iPhone X":
                for phone_ in retrieved_phones:
                    if "8" in phone_.split(" "):
                        retrieved_phones.pop(retrieved_phones.index(phone_))
                    elif "7" or "iPhone\xa07" or "iPhone\xa07"  in phone_.split(" "):
                        retrieved_phones.pop(retrieved_phones.index(phone_))
                    elif "6" in phone_.split(" "):
                        retrieved_phones.pop(retrieved_phones.index(phone_))
    
                retrieved_phones = retrieved_phones[:3]


            phones_json = [{"image": phone_name.lower().replace(" ", "_") + ".jpg"}, [], {}]
            for i, phone in enumerate(retrieved_phones):
                phones = ScrapedSmartphone.objects.filter(data__name = phone)
                for search_phone in phones:
                    not_there = True
                    for phone_json in phones_json[1]:
                        if phone_json["url"] == search_phone.data["url"]:

                            not_there = False
                    if not_there == True:   
                        phones_json[1].append(search_phone.data)
                        try: 
                            vendor_index = vendor.index(search_phone.data["vendor"])
                            phones_json[1][-1]["brandLogoUrl"] = "http://localhost:8001/brand_images/" + vendor_images[vendor_index]                                    
                        except ValueError:
                            phones_json[1][-1]["brandLogoUrl"] = "http://localhost:8001/brand_images/daraz.png"
                        if len(phones_json[1][-1]["name"]) > 32:
                            phones_json[1][-1]["name"] = phones_json[1][-1]["name"][:33] + "..."
                        phones_json[1][-1]["price"] = int(float(phones_json[1][-1]["price"]))
            original = OriginalSmartphone.objects.filter(data__DeviceName = phone_name)
            print (original)
            if (len(original) > 0):
                original = original[0]
            else:
                return JsonResponse({"error": "invalid phone name"})
            specs = original.data

            specs_to_send = {}
            try:
                specs_to_send["camera"] = specs["triple"]
            except KeyError:
                try:
                    specs_to_send["camera"] = specs["dual_"]
                except KeyError:
                    try:
                        specs_to_send["camera"] = specs["single"]
                    except KeyError:
                        specs_to_send["camera"] = "Photo/Video"

            specs_to_send["ram"] = specs["internal"]
            try:
                specs_to_send["processor"] = specs["cpu"]
            except KeyError:
                try:
                    specs_to_send["processor"] = specs["chipset"]
                except:
                    specs_to_send["processor"] = "No Info"
                
            specs_to_send["battery"] = specs["battery_c"]   
            phones_json[2] = specs_to_send


            phones_json[1] = sorted(phones_json[1], key=itemgetter('price')) 
            for specific_phone in phones_json[1]:
                specific_phone["price"] = locale.currency(specific_phone["price"] , grouping=True)[1:-3]

            return JsonResponse(phones_json, safe=False) 
    else:
        return JsonResponse({"error": "method not allowed"})

@csrf_exempt
def search_suggestion(request):
    if request.method == "POST":
        print (request.body)
        data = json.loads(request.body)
        sessionId = data.get("sessionId")
        decision_arr = securer(sessionId, request.headers["user_agent"])
        print (decision_arr)
        if decision_arr[0] == False:
            return JsonResponse(decision_arr[1])
        else:
            keyword = data.get("keyword")
            if keyword == None:
                return JsonResponse({"error": "no keyword"})
            results = OriginalSmartphone.objects.filter(available = True, data__DeviceName__icontains = keyword)[:4]
            print (results)
            if len(keyword) == 0:
                return JsonResponse({"error": "no phone found"})
            phones_to_suggest = {}
            for i, result in enumerate(results):
                phones_to_suggest[i] = result.data["DeviceName"]
            return JsonResponse(phones_to_suggest)
    else:
        return JsonResponse({"error": "method not allowed"})

def securer(sessionId, user_agent):
    if sessionId == None:
        return [False, {"error":"no sessionId"}]
    else:
        try:
            session = AccessLog.objects.get(sessionId = sessionId)
        except:
            return [False, {"error": "incorrect sessionId"}]
        user_requests = RequestLog.objects.filter(datetime__gt = datetime.datetime.now() - datetime.timedelta(days = 1), session = session)
        print (user_requests)
        if len(user_requests) < 1000:
            print ("reached here")
            print (session.user_agent)
            print (user_agent)
            if session.user_agent == user_agent:
                this_request = RequestLog(session = session)
                this_request.save()
                return [True]
        return [False, {"error": "not permitted"}]

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

def negater(request):
    all_scraped = ScrapedSmartphone.objects.all()
    for scraped in all_scraped:
        scraped.available = False
        scraped.belongs_to = None
        scraped.save()

    all_scraped = OriginalSmartphone.objects.all()
    for scraped in all_scraped:
        scraped.available = False
        scraped.save()

    return HttpResponse("deal done")


def available_checker(request):
    scraped = 0
    original = 0
    all_original_phones = OriginalSmartphone.objects.all()
    ix = index.open_dir("index")
    qp = QueryParser("phone_name", schema = ix.schema)
    for original_phone in all_original_phones:
        q = qp.parse(original_phone.data["DeviceName"])
        another_trial = False
        with ix.searcher() as s:
            results = s.search(q)
            if len(results) != 0:
                original_phone.available = True
                original_phone.save()
                original += 1

                if original_phone.data["DeviceName"] == "vivo Y65":
                    for i in range(30):
                        print ("")
                    print ("In First")
                    print (len(results))
                    for result in results:
                        print (result["phone_name"])
                    for i in range(30):
                        print ("")

                for result in results:
                    scraped_phones = ScrapedSmartphone.objects.filter(data__name = result["phone_name"])
                    for scraped_phone in scraped_phones:    
                        scraped_phone.available = True
                        scraped_phone.belongs_to = original_phone
                        scraped_phone.save()
                        scraped += 1 
            else:
                another_trial = True
        if another_trial == True:
            keyword = original_phone.data["DeviceName"].split(" ")[1:]
            q = qp.parse(" ".join(keyword))
            with ix.searcher() as s:
                results = s.search(q)
                if len(results) != 0:
                    original_phone.available = True
                    original_phone.save()
                    original += 1

                    if original_phone.data["DeviceName"] == "vivo Y65":
                        for i in range(30):
                            print ("")
                        print ("In Second")
                        for result in results:
                            print (result["phone_name"])
                        for i in range(30):
                            print ("")


                    for result in results:
                        scraped_phones = ScrapedSmartphone.objects.filter(data__name = result["phone_name"])
                        for scraped_phone in scraped_phones:    
                            scraped_phone.available = True
                            scraped_phone.belongs_to = original_phone
                            scraped_phone.save()
                            scraped += 1

        i = list(all_original_phones).index(original_phone)
        percentage = i*100/len(all_original_phones)
        print (percentage) 
        print ("Original ", original)
        print ("Scraped ", scraped)


def whoosh_indexer(request):
    if not os.path.exists("index"):
        os.mkdir("index")
    schema = Schema(phone_name=TEXT(stored = True))
    ix = create_in("index", schema)
    writer = ix.writer()
    phones = ScrapedSmartphone.objects.all()
    for phone in phones:
        print (phone.data["name"])
        writer.add_document(phone_name = phone.data["name"])
    writer.commit()
    return HttpResponse("Indexed bro!")


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
