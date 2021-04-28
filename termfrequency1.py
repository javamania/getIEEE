import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords 

nltk.download('stopwords')

f = open("C:\\Users\\javam\\Downloads\\tmwithpython-master\\tmwithpython-master\\트럼프취임연설문.txt", 'r')

lines = f.readlines()[0]
f.close()

lines[0:100]

tokenizer = RegexpTokenizer('[\w]+')

stop_words = stopwords.words('english')

words =  lines.lower()
tokens = tokenizer.tokenize(words)
stopped_tokens = [i for i in list((tokens)) if not i in stop_words]
stopped_tokens2 = [i for i in stopped_tokens if len(i)>1]


print(pd.Series(stopped_tokens2).value_counts().head(10))

