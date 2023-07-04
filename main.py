from requests_html import HTMLSession
s = HTMLSession()
country = 'india'
city ='delhi'
url =f'https://www.google.com/search?q=weather+{country}+{city}'
r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'})

temp = r.html.find('span#wob_tm', first= True).text

unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text

desc = r.html.find('div.wob_dcp span#wob_dc', first =True).text
print(city , temp+unit ,desc)