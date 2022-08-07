from notion.client import NotionClient

client = NotionClient(token_v2="324adbe39d1b03a9898527670c93546856531f91feb5b841898cf4d9616d2ec26b0c1bc59b5f3bf3be658ca42965c4c326875092110fda731eaaac7d1a021630f7a8677a659965a40188a15ce015")
cv = client.get_block("https://www.notion.so/ec68a29f55ba4da7b84ba3f55e568033?v=3792b65f9f544e61869e5abcbfa5e2c7")
cv.title = 'amoongus'