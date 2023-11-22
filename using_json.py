# python has a library for handling json data types
import json

# here is a JSON structure (remember JSON is a text format)
j = '''{
  "userId": 1,
  "id": 2,
  "title": "qui est esse",
  "body": "est rerum tempore vitae sequi sint nihil reprehenderit dolor beatae ea dolores neque fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis qui aperiam non debitis possimus qui neque nisi nulla"
}'''
# we can convert any JSON structure into a Python structure
d = json.loads(j) # pass in the JSON structure
print( type(d) ) # dict or list
print(d['title'])
print(d['body'])