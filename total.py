
#####################################################################
############ 추출된 핵심 어구를 그대로 연도 별로 넣은 버전 ##############
#####################################################################

import json

with open('total.json', 'rt', encoding='UTF8') as f:
    json_data = json.load(f)

jsonArray = json_data.get("value") # 총 5433개의 문서
#print(jsonArray)

print(len(jsonArray))
#print(jsonArray[0])
#print(type(jsonArray[0]['publication_year']))
year2002 =[]
year2003 =[]
year2004 =[]
year2005 =[]
year2006 =[]
year2007 =[]
year2008 =[]
year2009 =[]
year2010 =[]
year2011 =[]
year2012 =[]
year2013 =[]
year2014 =[]
year2015 =[]
year2016 =[]
year2017 =[]
year2018 =[]
year2019 =[]
year2020 =[]
year2021 =[]

#print(len(jsonArray[0].get("keyphrases"))) # keyphrases 개수 확인용

for i in range(100):  # 검색하려는 개수 만큼 range 입력 (100 입력하면 "5433 문서 중 100개의 문서 뽑겠다!!)
    if jsonArray[i]['publication_year'] == 2002 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2002.append(jsonArray[i].get("keyphrases")[j])
    # 이 경우 예를 들면, jsonArray[0] 한 군데에서 SOA라는 단어가 여러 번 나오는 경우 고려 X !! 
    # jsonArray[0]의 keyphrases에서 각각의 '핵심 구'를 '한 단어'로 쪼갠다 → 저장 → 중복 제거한다.????   
    
    if jsonArray[i]['publication_year'] == 2003 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2003.append(jsonArray[i].get("keyphrases")[j])
    
    if jsonArray[i]['publication_year'] == 2004 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2004.append(jsonArray[i].get("keyphrases")[j])
    
    if jsonArray[i]['publication_year'] == 2005 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2005.append(jsonArray[i].get("keyphrases")[j])
    
    if jsonArray[i]['publication_year'] == 2006 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2006.append(jsonArray[i].get("keyphrases")[j])
    
    if jsonArray[i]['publication_year'] == 2007 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2007.append(jsonArray[i].get("keyphrases")[j])
    
    if jsonArray[i]['publication_year'] == 2008 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2008.append(jsonArray[i].get("keyphrases")[j])

    if jsonArray[i]['publication_year'] == 2009 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2009.append(jsonArray[i].get("keyphrases")[j])

    if jsonArray[i]['publication_year'] == 2010 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2010.append(jsonArray[i].get("keyphrases")[j])

    if jsonArray[i]['publication_year'] == 2011 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2011.append(jsonArray[i].get("keyphrases")[j])

    if jsonArray[i]['publication_year'] == 2012 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2012.append(jsonArray[i].get("keyphrases")[j])

    if jsonArray[i]['publication_year'] == 2013 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2013.append(jsonArray[i].get("keyphrases")[j])

    if jsonArray[i]['publication_year'] == 2014 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2014.append(jsonArray[i].get("keyphrases")[j])

    if jsonArray[i]['publication_year'] == 2015 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2015.append(jsonArray[i].get("keyphrases")[j])

    if jsonArray[i]['publication_year'] == 2016 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2016.append(jsonArray[i].get("keyphrases")[j])

    if jsonArray[i]['publication_year'] == 2017 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2017.append(jsonArray[i].get("keyphrases")[j])

    if jsonArray[i]['publication_year'] == 2018 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2018.append(jsonArray[i].get("keyphrases")[j])

    if jsonArray[i]['publication_year'] == 2019 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2019.append(jsonArray[i].get("keyphrases")[j])

    if jsonArray[i]['publication_year'] == 2020 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2020.append(jsonArray[i].get("keyphrases")[j])
 
    if jsonArray[i]['publication_year'] == 2021 :
        for j in range(len(jsonArray[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력 
            year2021.append(jsonArray[i].get("keyphrases")[j])

    else :
        print("다른년도입니다.")


print("===================================2002년=======================================\n")
print(year2002)
print("===================================2003년=======================================\n")
print(year2003)
print("===================================2004년=======================================\n")
print(year2004)
print("===================================2005년=======================================\n")
print(year2005)
print("===================================2006년=======================================\n")
print(year2006)
print("===================================2007년=======================================\n")
print(year2007)
print("===================================2008년=======================================\n")
print(year2008)
print("===================================2006년=======================================\n")
print(year2006)
print("===================================2007년=======================================\n")
print(year2007)
print("===================================2008년=======================================\n")
print(year2008)
print("===================================2009년=======================================\n")
print(year2009)
print("===================================2010년=======================================\n")
print(year2010)
print("===================================2011년=======================================\n")
print(year2011)
print("===================================2012년=======================================\n")
print(year2012)
print("===================================2013년=======================================\n")
print(year2013)
print("===================================2014년=======================================\n")
print(year2014)
print("===================================2015년=======================================\n")
print(year2015)
print("===================================2016년=======================================\n")
print(year2016)
print("===================================2017년=======================================\n")
print(year2017)
print("===================================2018년=======================================\n")
print(year2018)
print("===================================2019년=======================================\n")
print(year2019)
print("===================================2020년=======================================\n")
print(year2020)

#key = jsonArray[0].get("keyphrases")

#print(key[0])