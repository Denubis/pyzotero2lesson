#!/usr/bin/env python3

from pyzotero import zotero
from pprint import pprint, pformat
import json
#For group libraries, the ID can be found by opening the group's page: https://www.zotero.org/groups/groupname, and hovering over the group settings link. The ID is the integer after /groups/

#https://www.zotero.org/groups/22427/twitterresearch/collections/A5KNVA8P

LIBRARY_ID="22427"
LIBRARY_TYPE="group"

with open("zotero.json") as jsonfile:
	API_KEY = json.load(jsonfile)['JSON_API']
	#print(apikey)
zot =  zotero.Zotero(LIBRARY_ID, LIBRARY_TYPE, API_KEY)
items = zot.top(limit=10)
for item in items:
	data = item['data']
	#print(data)
	# print(item.keys())
	# print('Title: {} | Key: {}'.format(data['title'], data['key']))
	# print("Abstract: {}".format(data['abstractNote']))
	# print(item['links'].keys())
	with open("../../_bibliography/{}-{}.md".format(data['key'], data['title']), "w") as bibfile:
		bibfile.write("""---
layout: default
title: {}
--- 
<pre>
{}
</pre>""".format(data['title'], pformat(item)))
		