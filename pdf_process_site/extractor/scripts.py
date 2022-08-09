from notion.client import NotionClient
from notion.block import TodoBlock


client = NotionClient(token_v2="324adbe39d1b03a9898527670c93546856531f91feb5b841898cf4d9616d2ec26b0c1bc59b5f3bf3be658ca42965c4c326875092110fda731eaaac7d1a021630f7a8677a659965a40188a15ce015")
cv = client.get_block("https://www.notion.so/8ca6e428fa7e494e9bde40e23d21df74?v=0ea9d9f7fb2a4223b013a1f119d16bf4")
cv.title = 'amoongus'

link = "https://www.notion.so/Aug-1-3f07c5e22009443e9bb185c572c6d0f4"
link_client = client.get_block(link)
row = cv.collection.add_row()
print(cv.collection.get_schema_properties())

row.Daily_Tracking = link



'''
text = {"id": "text", 'name':'Test', 'type': 'text'}
cv.collection.add_property(**text)

num = {"id": "num", 'name':'num', 'type': 'number'}
cv.collection.add_property(**num)

state = {"id": "state", 'name':'state', 'type': 'status'}
cv.collection.add_property(**state)

check = {"id": "check", 'name':'check', 'type': 'checkbox'}
cv.collection.add_property(**check)

relation = {"id": "relation", 'name':'relation', 'type': 'relation'}
cv.collection.add_property(**relation)

timecreation = {"id": "time", 'name':'time', 'type': 'created_time'}
cv.collection.add_property(**timecreation)
'''