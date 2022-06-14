import xmltodict
import requests
from datetime import datetime

stjornumerki = [(120, 'Steingeit'), (218, 'Vatnsberi'), (320, 'Fiskur'), (420, 'Hrútur'), (521, 'Naut'),
           (621, 'Tvíburi'), (722, 'Krabbi'), (823, 'Ljón'), (923, 'Meyja'), (1023, 'Vog'),
           (1122, 'Sporðdreki'), (1222, 'Bogmaður'), (1231, 'Steingeit')]

def na_stjornumerki(date):
    date_number = int("".join((str(date.date().month), '%02d' % date.date().day)))
    for z in stjornumerki:
        if date_number <= z[0]:
            return z[1]

def kyn(nafn):
	if(nafn.find(u'dóttir') != -1):
		return 'kvk'
	elif(nafn.find(u'son') != -1):
		return 'kk'
	else:
		return '0'

def kenninafn(nafn):
	if(nafn.find(u'dóttir') != -1):
		return nafn.split(' ')[-1][:-6]
	elif(nafn.find(u'son') != -1):
		return nafn.split(' ')[-1][:-3]
	else:
		return '0'

def most_common(lst):
    return max(set(lst), key=lst.count)

url = 'http://www.althingi.is/altext/xml/thingmenn/'
response = requests.get(url)
data = xmltodict.parse(response.text)

afmaelisdagar = []
stjornumerk = []
mps = []
kenninofn = []
for mp in data[u'þingmannalisti'][u'þingmaður']:
	afmaelisdagar.append([datetime.strptime(mp[u'fæðingardagur'], '%Y-%m-%d'), mp[u'nafn']])
	mps.append((mp[u'nafn'], mp[u'fæðingardagur']))
	kenninofn.append(kenninafn(mp[u'nafn']))
	

#afmaelisdagar.sort()
for afmaelisdagur in afmaelisdagar:
	print(str(afmaelisdagur[0]) +', '+ afmaelisdagur[1] +', ' + kyn(afmaelisdagur[1]) +', '+ na_stjornumerki(afmaelisdagur[0]))

print(len(set(mps)))

#while '0' in kenninofn: kenninofn.remove('0')
#print(kenninofn)
mc = most_common(kenninofn)
print(mc, kenninofn.count(mc))
