# from wordcloud import WordCloud, STOPWORDS
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# 한글 폰트 패스로 지정
import matplotlib.font_manager as fm
import re
import collections

text = "''services', 'multi-domain service-based systems', 'different domains', 'critical tasks', 'domain', 'systems', 'data flow', 'composed services', 'security', 'trustworthiness', 'major concerns', 'service-based systems', 'access control models', 'data reproduction', 'data provenance schemes', 'data quality assessment', 'access control', 'recent years', 'enhancement', 'existing mechanisms', 'integrated model', 'data provenance model', 'integrated role-based access control', 'cross-domain interactions', 'paper', 'data object', 'data trustworthiness', 'role-based data provenance scheme', 'roles of originators', 'contributors', 'information', 'data provenance information', 'information flow control', 'derived data quality attributes', 'cross domain access', 'use', 'access control', 'trustworthiness', 'better security', 'data provenance', 'multi-domain service-based applications', 'integrated model', 'storage', 'separate customer service', 'data collection', 'bookkeeping', 'inventory', 'sensors', 'majority', 'network of meters', 'billing', 'municipality territory', 'monitoring', 'control of utilities networks', 'maintenance', 'challenging process', 'development of sensor network', 'human work', 'RTU research team', 'multi-resource meters', 'multi-apartment buildings', 'state research program NexIT', 'installation', 'district heating substations', 'water distribution network', 'temperature', 'offices', 'humidity measurement', 'protocols translation function', 'adapter', 'communication', 'gateways', 'systems', 'municipality', 'cloud of public utilities systems', 'common architecture', 'SOA', 'gateway devices', 'sensors', 'IoT approaches', 'Thanks', 'customer experience centric', 'demand driven market environment', 'ICT', 'partner', 'leading enabler', 'service oriented', 'modern enterprise business', 'companies', 'virtual organized enterprises', 'group of business oriented', 'pure digital style', 'applications', 'microservice', 'modules', 'technical solution staff', 'context of enterprise architecture', 'concept of microservice', 'enterprise microservices', 'reference architecture model', 'clear understanding', 'definition', 'blocks', 'key architectural components', 'paper', 'enterprise level', 'transformation architecture solutions', 'reference architecture model', 'API', 'microservice relevant technologies', 'pragmatic guidance', 'business', 'professionals', 'confusion', 'corresponding recommendations', 'set of key architectural issues', 'microsevices', 'APIs', 'company', 'enterprise level', 'paper', 'trending standard', 'development of software', 'Service Oriented architecture', 'services', 'self-standing function', 'service', 'different services', 'different organizational databases', 'serious issue', 'numerous heterogeneities', 'Service interoperability', 'Consumer Affairs', 'automated system', 'Existing system', 'consumer issue', 'Department of Civil Supplies', 'heterogeneous organizations', 'interoperability model', 'SOA', 'Service Oriented Architecture', 'secure manner', 'paper', 'idea', 'different level of security mechanism', 'different services interoperability issue', 'organizational databases', 'proposal', 'agreement', 'various parties', 'interoperability', 'verification', 'particular service', 'heterogeneities database server', 'model', 'effective integration of various data sources', 'different functionalities', 'interoperable model', 'automated manner', 'Outcome'"
spwords = set(STOPWORDS)  # 제외할 단어
spwords = {'data','different', 'service', 'systems', 'based', 'information', 'services', 'systems', 'of', 'paper' }  # 제외하고 싶은 단어 추가
# 워드 클라우드를 설정합니다. 한글폰트 사용
# text string 사용
wc1 = WordCloud(max_font_size=200, stopwords=spwords, font_path='C:/Windows/Fonts/MOD20.TTF',
                background_color='white', width=800, height=800)
wc1.generate(text)

plt.figure(figsize=(10, 8))
plt.imshow(wc1)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
