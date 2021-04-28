import json
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import nltk
import pickle
from nltk.corpus import stopwords
import re
nltk.download('all')
from nltk.tokenize import word_tokenize 
import collections # Counter 

with open('total.json', 'rt', encoding='UTF8') as f:
    json_data = json.load(f)

jsonArray = json_data.get("value") # 총 5433개의 문서
jsonArray1 = list({v['title']:v for v in jsonArray}.values()) # title로 구분하여 중복 제거
#print(jsonArray)

print(len(jsonArray))
print(len(jsonArray1))

wlem = nltk.WordNetLemmatizer()
#lemmatized_words = []

# Stop Words 등록하기
stopwords = set(STOPWORDS)
stopwords.update(['system','service','paper','software','business','process','information'])
# print(stopwords) # 불용어 출력 

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

new_year2002 =[]
new_year2003 =[]
new_year2004 =[]
new_year2005 =[]
new_year2006 =[]
new_year2007 =[]
new_year2008 =[]
new_year2009 =[]
new_year2010 =[]
new_year2011 =[]
new_year2012 =[]
new_year2013 =[]
new_year2014 =[]
new_year2015 =[]
new_year2016 =[]
new_year2017 =[]
new_year2018 =[]
new_year2019 =[]
new_year2020 =[]
new_year2021 =[]

#print(len(jsonArray1[0].get("keyphrases"))) # keyphrases 개수 확인용

for i in range(4792):   # publication_year 개수 만큼 range 입력 (1000 입력하면 "5433 문서 중 1000개의 문서 뽑겠다!!)
    if jsonArray1[i]['publication_year'] == 2002 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력
            year2002 = jsonArray1[i].get("keyphrases")[j].split() # 쪼개서 year2002에 list 형태로 넣었음! 이제 list 요소를 하나씩 new_year2002 에 넣자..
            for w in range(len(year2002)):  # 핵심 어구를 단어로 만든 개수 만큼 range 입력 
                year2002[w] = year2002[w].replace("'","") # 어퍼스트로피(') 제거
                year2002[w]=year2002[w].lower()
                year2002[w] = wlem.lemmatize(year2002[w]) # 복수 명사를 단수로 변경
                if year2002[w] not in stopwords:
                    new_year2002.append(year2002[w])  
    if jsonArray1[i]['publication_year'] == 2003 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2003 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2003)):  
                year2003[w] = year2003[w].replace("'","")
                year2003[w]=year2003[w].lower()
                year2003[w] = wlem.lemmatize(year2003[w])
                if year2003[w] not in stopwords:
                    new_year2003.append(year2003[w])    
    if jsonArray1[i]['publication_year'] == 2004 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2004 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2004)):  
                year2004[w] = year2004[w].replace("'","")
                year2004[w]=year2004[w].lower()
                year2004[w] = wlem.lemmatize(year2004[w])
                if year2004[w] not in stopwords:
                    new_year2004.append(year2004[w])
    if jsonArray1[i]['publication_year'] == 2005 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2005 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2005)):  
                year2005[w] = year2005[w].replace("'","")
                year2005[w]=year2005[w].lower()
                year2005[w] = wlem.lemmatize(year2005[w])
                if year2005[w] not in stopwords:
                    new_year2005.append(year2005[w])    
    if jsonArray1[i]['publication_year'] == 2006 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2006 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2006)):  
                year2006[w] = year2006[w].replace("'","")
                year2006[w]=year2006[w].lower()
                year2006[w] = wlem.lemmatize(year2006[w])
                if year2006[w] not in stopwords:
                    new_year2006.append(year2006[w])
    if jsonArray1[i]['publication_year'] == 2007 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2007 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2007)):  
                year2007[w] = year2007[w].replace("'","")
                year2007[w]=year2007[w].lower()
                year2007[w] = wlem.lemmatize(year2007[w])
                if year2007[w] not in stopwords:
                    new_year2007.append(year2007[w])    
    if jsonArray1[i]['publication_year'] == 2008 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2008 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2008)):  
                year2008[w] = year2008[w].replace("'","")
                year2008[w]=year2008[w].lower()
                year2008[w] = wlem.lemmatize(year2008[w])
                if year2008[w] not in stopwords:
                    new_year2008.append(year2008[w])
    if jsonArray1[i]['publication_year'] == 2009 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2009 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2009)):  
                year2009[w] = year2009[w].replace("'","")
                year2009[w]=year2009[w].lower()
                year2009[w] = wlem.lemmatize(year2009[w])
                if year2009[w] not in stopwords:
                    new_year2009.append(year2009[w])    
    if jsonArray1[i]['publication_year'] == 2010 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2010 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2010)):  
                year2010[w] = year2010[w].replace("'","")
                year2010[w]=year2010[w].lower()
                year2010[w] = wlem.lemmatize(year2010[w])
                if year2010[w] not in stopwords:
                    new_year2010.append(year2010[w])
    if jsonArray1[i]['publication_year'] == 2011 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2011 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2011)):  
                year2011[w] = year2011[w].replace("'","")
                year2011[w]=year2011[w].lower()
                year2011[w] = wlem.lemmatize(year2011[w])
                if year2011[w] not in stopwords:
                    new_year2011.append(year2011[w])
    if jsonArray1[i]['publication_year'] == 2012 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2012 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2012)):  
                year2012[w] = year2012[w].replace("'","")
                year2012[w]=year2012[w].lower()
                year2012[w] = wlem.lemmatize(year2012[w])
                if year2012[w] not in stopwords:
                    new_year2012.append(year2012[w])    
    if jsonArray1[i]['publication_year'] == 2013 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2013 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2013)):  
                year2013[w] = year2013[w].replace("'","")
                year2013[w] = year2013[w].lower()
                year2013[w] = wlem.lemmatize(year2013[w])
                if year2013[w] not in stopwords:
                    new_year2013.append(year2013[w])
    if jsonArray1[i]['publication_year'] == 2014 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  # keyphrases 개수 만큼 range 입력
            year2014 = jsonArray1[i].get("keyphrases")[j].split() # 쪼개서 year2014에 list 형태로 넣었음! 이제 list 요소를 하나씩 new_year2014 에 넣자..
            for w in range(len(year2014)):  # 핵심 어구를 단어로 만든 개수 만큼 range 입력
                year2014[w] = year2014[w].replace("'","") # 어퍼스트로피(') 제거
                year2014[w]=year2014[w].lower() # 대문자 → 소문자
                year2014[w] = wlem.lemmatize(year2014[w]) # 복수형 → 단수형
                if year2014[w] not in stopwords:
                    new_year2014.append(year2014[w])
                # new_year2014.append(year2014[w])
                    
    if jsonArray1[i]['publication_year'] == 2015 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2015 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2015)):  
                year2015[w] = year2015[w].replace("'","")
                year2015[w]=year2015[w].lower()
                year2015[w] = wlem.lemmatize(year2015[w])
                if year2015[w] not in stopwords:
                    new_year2015.append(year2015[w])
    if jsonArray1[i]['publication_year'] == 2016 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2016 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2016)):  
                year2016[w] = year2016[w].replace("'","")
                year2016[w]=year2016[w].lower()
                year2016[w] = wlem.lemmatize(year2016[w])
                if year2016[w] not in stopwords:
                    new_year2016.append(year2016[w])    
    if jsonArray1[i]['publication_year'] == 2017 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2017 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2017)):  
                year2017[w] = year2017[w].replace("'","")
                year2017[w]=year2017[w].lower()
                year2017[w] = wlem.lemmatize(year2017[w])
                if year2017[w] not in stopwords:
                    new_year2017.append(year2017[w])
    if jsonArray1[i]['publication_year'] == 2018 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2018 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2018)):  
                year2018[w] = year2018[w].replace("'","")
                year2018[w]=year2018[w].lower()
                year2018[w] = wlem.lemmatize(year2018[w])
                if year2018[w] not in stopwords:
                    new_year2018.append(year2018[w])
    if jsonArray1[i]['publication_year'] == 2019 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2019 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2019)):  
                year2019[w] = year2019[w].replace("'","")
                year2019[w]=year2019[w].lower()
                year2019[w] = wlem.lemmatize(year2019[w])
                if year2019[w] not in stopwords:
                    new_year2019.append(year2019[w])    
    if jsonArray1[i]['publication_year'] == 2020 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2020 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2020)):  
                year2020[w] = year2020[w].replace("'","")
                year2020[w]=year2020[w].lower()
                year2020[w] = wlem.lemmatize(year2020[w])
                if year2020[w] not in stopwords:
                    new_year2020.append(year2020[w])
    if jsonArray1[i]['publication_year'] == 2021 :
        for j in range(len(jsonArray1[i].get("keyphrases"))):  
            year2021 = jsonArray1[i].get("keyphrases")[j].split()
            for w in range(len(year2021)):  
                year2021[w] = year2021[w].replace("'","")
                year2021[w]=year2021[w].lower()
                year2021[w] = wlem.lemmatize(year2021[w])
                if year2021[w] not in stopwords:
                    new_year2021.append(year2021[w])

# 연도별 top 20 가져오기 2014년도 테스트  
#counter_2014 = collections.Counter(new_year2014)
#print(counter_2014)
#print('======================')
#print(counter_2014.most_common(20))

#1884년
print("===================================2002년=======================================\n")
counter_2002 = collections.Counter(new_year2002)
print(counter_2002.most_common(20))
#print(new_year2002)
print("===================================2003년=======================================\n")
counter_2003 = collections.Counter(new_year2003)
print(counter_2003.most_common(20))
#print(new_year2003)
print("===================================2004년=======================================\n")
counter_2004 = collections.Counter(new_year2004)
print(counter_2004.most_common(20))
#print(new_year2004)
print("===================================2005년=======================================\n")
counter_2005 = collections.Counter(new_year2005)
print(counter_2005.most_common(20))
#print(new_year2005)
print("===================================2006년=======================================\n")
counter_2006 = collections.Counter(new_year2006)
print(counter_2006.most_common(20))
#print(new_year2006)
print("===================================2007년=======================================\n")
counter_2007 = collections.Counter(new_year2007)
print(counter_2007.most_common(20))
#print(new_year2007)
print("===================================2008년=======================================\n")
counter_2008 = collections.Counter(new_year2008)
print(counter_2008.most_common(20))
#print(new_year2008)
print("===================================2009년=======================================\n")
counter_2009 = collections.Counter(new_year2009)
print(counter_2009.most_common(20))
#print(new_year2009)
print("===================================2010년=======================================\n")
counter_2010 = collections.Counter(new_year2010)
print(counter_2010.most_common(20))
#print(new_year2010)
print("===================================2011년=======================================\n")
counter_2011 = collections.Counter(new_year2011)
print(counter_2011.most_common(20))
#print(new_year2011)
print("===================================2012년=======================================\n")
counter_2012 = collections.Counter(new_year2012)
print(counter_2012.most_common(20))
#print(new_year2012)
print("===================================2013년=======================================\n")
counter_2013 = collections.Counter(new_year2013)
print(counter_2013.most_common(20))
#print(new_year2013)
print("===================================2014년=======================================\n")
counter_2014 = collections.Counter(new_year2014)
print(counter_2014.most_common(20))
#print(new_year2014)
print("===================================2015년=======================================\n")
counter_2015 = collections.Counter(new_year2015)
print(counter_2015.most_common(20))
#print(new_year2015)
print("===================================2016년=======================================\n")
counter_2016 = collections.Counter(new_year2016)
print(counter_2016.most_common(20))
#print(new_year2016)
print("===================================2017년=======================================\n")
counter_2017 = collections.Counter(new_year2017)
print(counter_2017.most_common(20))
#print(new_year2017)
print("===================================2018년=======================================\n")
counter_2018 = collections.Counter(new_year2018)
print(counter_2018.most_common(20))
#print(new_year2018)
print("===================================2019년=======================================\n")
counter_2019 = collections.Counter(new_year2019)
print(counter_2019.most_common(20))
#print(new_year2019)
print("===================================2020년=======================================\n")
counter_2020 = collections.Counter(new_year2020)
print(counter_2020.most_common(20))
#print(new_year2020)
print("===================================2021년=======================================\n")
counter_2021 = collections.Counter(new_year2021)
print(counter_2021.most_common(20))
#print(new_year2021)

#key = jsonArray[0].get("keyphrases")

#print(key[0])

#cloud_descript = ' '.join(new_year2021) # new_year2014 를 str 형태로

# Word Cloud 생성하기
wordcloud = WordCloud(max_font_size = 300 ,
                      max_words = 20 ,
                      width = 1500,
                      height = 1000,
                      background_color='white')
cloud = wordcloud.generate_from_frequencies(dict(counter_2014.most_common(20)))

plt.figure(figsize = (20 , 15))
plt.imshow(wordcloud , interpolation = 'bilinear')
plt.axis('off')
plt.imshow(cloud)
plt.show()