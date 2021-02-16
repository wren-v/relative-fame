import pageviewapi
import wikipedia
import requests
import json
import csv
import time


def parseCity(line):
    output = "" 
    for char in line:
        if(char == ','):
            return output[11:]
        output += char

def parsePopulation(line):
    output = ""
    for char in line:
        if (char.isdigit()):
            output += char
    return output
        
def parseName(line):
    output = ""
    for char in line:
        if(char == ']' or char == '|'):
            if (char == ')'):
                output += char
            return output[3:]
        output += char

def createList():
    file = open('CitiesInIowa.xml', 'r')
    count = 0
    notableArr = [[]]
    cityArr = []
    cityName = ""
    addPeople = False

    for line in file:
        count = count + 1
        if ("<title>" in line and ("Category:" not in line)):
            if (len(cityArr) > 1):
                notableArr.append(cityArr)
            cityArr = []
            addPeople = False
            cityName = parseCity(line)
            cityArr = [cityName]
        if ("population_total" in line):
            cityArr.append(parsePopulation(line))
        if ("==" in line and "Notable" in line):
            addPeople = True
        if ("==" in line and not "Notable" in line):
            addPeople = False
        if((addPeople) and ("*[[" in line) and ("Category:" not in line) and ("File:" not in line) and ("NULLIFIED" not in line) and ("END OF NOTICE" not in line)):
            cityArr.append(parseName(line))
            
    file.close()
    return notableArr

def getPageViews(lis):
    headers = {'User-Agent': '(wvogelschmidt@colgate.edu)'}

    try:
        article = wikipedia.page(lis).url
        article = article[30:]
        url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/" + article + "/monthly/20210101/20210201"
    except wikipedia.exceptions.PageError:
        print("Page Error LIS: " + lis)
        return 0
    except wikipedia.exceptions.DisambiguationError:
        print("Disambiguation Error LIS: " + lis)
        return 0
    try:
        resp = requests.get(url, headers=headers)
        rd = resp.json()
        print("success url: " + url)
        return rd['items'][0]['views']
    except wikipedia.exceptions.DisambiguationError:
        print("Disambiguation Error URL: " + url)
        return 0


def outputList(notableArr):
    file = open('output.csv', 'w')

    for array in notableArr:
        if(len(array) > 2):
            count = 0
            pageViews = 0
            maxViews = 0
            for lis in array:
                if(count < 2):
                    file.write(lis)
                    file.write(',')
                    count += 1
                else:
                    pgVw = getPageViews(lis)
                    if (pgVw > maxViews):
                        maxViews = pgVw
                    pageViews += pgVw
            file.write(str(len(array)-2) + ',')
            file.write(str(pageViews) + ',')
            file.write(str(maxViews))
            file.write('\n')
    file.close()

#Create and Output List
notableArr = createList()
outputList(notableArr)