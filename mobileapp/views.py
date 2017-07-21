from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from PIL import Image
from lxml import html  
import requests
def welfun(request):
	return render(request,'first.html',) 
def compare(request, value=None):
	li=list()
	first=''
	second=''
	third=''
	if(value== "1"):
		li.insert(0,'http://ecx.images-amazon.com/images/I/61E8jlkhYnL._SX522_.jpg')
		Aurl='http://www.amazon.in/HTC-Desire-10-Pro-Polar/dp/B01N35HX8A/ref=sr_1_2?s=electronics&ie=UTF8&qid=1499687082&sr=1-2&keywords=htc+desire+10+pro'
		Furl='https://www.flipkart.com/htc-desire-10-pro-polar-white-64-gb/p/itmeqqzhzp6fvrhg?pid=MOBEQQZHMNPRT57Z&srno=s_1_1&otracker=search&lid=LSTMOBEQQZHMNPRT57ZXRWK15&qH=cb3482a78183a5d7'
		Curl='https://www.croma.com/htc-desire-10-pro-polar-white-64gb-/p/200617'
	if(value== "2"):
		li.insert(0,'http://ecx.images-amazon.com/images/I/31n1xbQSVqL.jpg')
	 	Aurl='http://www.amazon.in/Samsung-J7-Prime-32GB-VoLTE/dp/B06Y3HFZBQ/ref=sr_1_7?s=electronics&ie=UTF8&qid=1499688341&sr=1-7&keywords=samsung+galaxy+j7'
		Furl='https://www.flipkart.com/samsung-galaxy-j7-prime-gold-32-gb/p/itmeswzmrpy4gttt?pid=MOBESWZM2Z8GBCHF&srno=s_1_1&otracker=search&lid=LSTMOBESWZM2Z8GBCHF6FOO4V&qH=f2980880b1647294'
		Curl='https://www.croma.com/samsung-galaxy-j7-prime-gold-32gb-mobile-phone/p/202697'
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	if(value=="3"):
		li.insert(0,'https://fr.e-recycle.com/fr/boutique/2344-thickbox_default/8.jpg')
		Aurl='http://www.amazon.in/Huawei-V100R001-Honor-Sapphire-Blue/dp/B01FM7IB92/ref=sr_1_1?s=electronics&ie=UTF8&qid=1499688119&sr=1-1&keywords=honor+8'
		Furl='https://www.flipkart.com/honor-8/p/itmeuydakfewgvk3?pid=MOBEM38ENZEBZFY5&srno=s_1_1&otracker=search&lid=LSTMOBEM38ENZEBZFY5HYY85C&qH=c3a45f2263d4cce5'
		Curl='https://www.croma.com/honor-8-sapphire-blue-32gb-/p/199284'
	if(value=="4"):
		li.insert(0,'http://ecx.images-amazon.com/images/I/317gq-PLD9L.jpg')
		Aurl='http://www.amazon.in/Lenovo-K6-Note-Gold/dp/B01MZ0NA27/ref=sr_1_1?s=electronics&ie=UTF8&qid=1499689932&sr=1-1&keywords=Lenovo+K6+Note+%28Gold%29'
		Furl='https://www.flipkart.com/lenovo-k6-note-gold-32-gb/p/itmeuyd9jh8gqsgz?pid=MOBES68AHHX4YHQZ&srno=s_1_1&otracker=search&lid=LSTMOBES68AHHX4YHQZZB5DP0&qH=04437f75dc027bbf'
		Curl='https://www.croma.com/lenovo-k6-note-gold-32gb-mobile-phone/p/202294'
	#Amazon
	Apage = requests.get(Aurl,headers=headers)
	doc = html.fromstring(Apage.content)
	XPATH_NAME = '//h1[@id="title"]//text()'
	XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
	OTHER_XPATH_SALE_PRICE = '//span[contains(@class,"a-color-price") or contains(@id,"saleprice")]/text()'
 	RAW_NAME = doc.xpath(XPATH_NAME)
	RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
	OTHER_RAW_SALE_PRICE = doc.xpath(OTHER_XPATH_SALE_PRICE)
	OTHER_PRICE = ' '.join(''.join(OTHER_RAW_SALE_PRICE).split()).strip() if OTHER_RAW_SALE_PRICE else None 
	ANAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
	ASALE_PRICE = ''.join(RAW_SALE_PRICE).strip() if RAW_SALE_PRICE else None
	AOTHER_PRICE=OTHER_PRICE.partition(' ')[0]
	
	#Flipkart
	Fpage = requests.get(Furl,headers=headers)
	doc = html.fromstring(Fpage.content)
	XPATH_NAME = '//h1[@class="_3eAQiD"]//text()'
	XPATH_SALE_PRICE = '//div[contains(@class,"_1vC4OE _37U4_g")]/text()'
	RAW_NAME = doc.xpath(XPATH_NAME)
	RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
	FNAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
	FPRICE = ''.join(RAW_SALE_PRICE).strip() if RAW_SALE_PRICE else None
	FPRICE=FPRICE[1:]
	
	#Croma
	Cpage = requests.get(Curl,headers=headers)
	doc = html.fromstring(Cpage.content)
	XPATH_NAME = '//h1[@style="text-transform: uppercase;"]//text()'
	XPATH_SALE_PRICE = '//h2[@style="font-size: 20px;"]/text()'
	XPATH_MRP_PRICE = '//span[@style="text-decoration: line-through;"]/text()'
	RAW_NAME = doc.xpath(XPATH_NAME)
	RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
	RAW_MRP_PRICE = doc.xpath(XPATH_MRP_PRICE)
	CNAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
	CSALE_PRICE = ''.join(RAW_SALE_PRICE).strip() if RAW_SALE_PRICE else None
	CMRP_PRICE = ''.join(RAW_MRP_PRICE).strip() if RAW_MRP_PRICE else None
	
	flag=0
	if ASALE_PRICE<=AOTHER_PRICE:
		APRICE=ASALE_PRICE
	else:
		APRICE=AOTHER_PRICE
		flag=1
	if APRICE<=FPRICE and APRICE<=CSALE_PRICE:
		first='Amazone '+APRICE
		if FPRICE<=CSALE_PRICE:
			second='Flipkart '+FPRICE
			third='Corma '+CSALE_PRICE
		else:
			second='Corma '+CSALE_PRICE
			third='Flipkart '+FPRICE
	if FPRICE<=APRICE and FPRICE<=CSALE_PRICE:
		first='Flipkart '+FPRICE
		if APRICE<=CSALE_PRICE:
			second='Amazone '+APRICE
			third='Corma '+CSALE_PRICE
		else:
			second='Corma '+CSALE_PRICE
			third='Amazone  '+APRICE
	if CSALE_PRICE<=APRICE and CSALE_PRICE<=FPRICE:
		first='Corma '+CSALE_PRICE
		if APRICE<=FPRICE:
			second='Amazone '+APRICE
			third='Flipkart '+FPRICE
		else:
			second='Flipkart '+FPRICE
			third='Amazone  '+APRICE
	li.insert(1,ANAME)
	li.insert(2,first)
	li.insert(3,second)
	li.insert(4,third) 
	return  render_to_response('Result.html',{'posts' : li})	
	
