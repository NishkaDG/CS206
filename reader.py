import json
with open('bookmarks') as data_file:    
	data = json.load(data_file)
csvDatalist=[]
def explorer(jsonObject, parentName, parentID):
	for each in jsonObject:
		child=each
		if child['type']=='url':
			entryList=[parentName, parentID,'url',child['name'],child['id'],child['date_added'], child['date_added'],child['url']]
		else:
			entryList=[parentName, parentID,'folder',child['name'],child['id'],child['date_added'], child['date_modified'],'NA']
			explorer(child['children'], child['name'], child['id'])
		csvDatalist.append(entryList)
for each in data['roots']:
	try:
		explorer(data['roots'][each]['children'],data['roots'][each]['name'],data['roots'][each]['id'])
	except:
		print("No bookmarks under folder "+ data['roots'][each])
f=open('chrome.csv', 'w')
for each in csvDatalist:
	f.write(','.join(y for y in each))
	f.write('\n')
f.close()
