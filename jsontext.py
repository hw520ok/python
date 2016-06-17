# -*- coding: utf-8

import json
import customserializer

with open('entry.json','r',encoding='utf-8') as f:
	entry = json.load(f,object_hook=customserializer.from_json)

print(entry)
下载它。 (大部分的供稿阅读器会美一小时检查一次更新。 )
让我们先用最粗糙和最快的方法来实现它，接着再来看看怎样
改进。
>>> import urllib.request
>>> a_url =
'
