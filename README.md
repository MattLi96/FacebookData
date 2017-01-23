# FacebookData
Processes the data from the Facebook download. Right now focuses on extracting the chat data.

# UidMap.py
Sometimes people have private facebook pages that does not allow this program to determine the username corresponding to an id. However, you can still get these usernames by checking <https://www.facebook.com/$id> while logged into your account (replace id in the url with the id number). You should then create your own `UidMap.py` file in the `src` folder to define these manually as a dictionary. The syntax of the file is:

```python
UID_MAP = {'id1': 'name1', 'id2': 'name2',...}
NAME_MAP = {'name1' : ['nickname1', 'nickname2',...], 'name2' : ['nickname1']}
```

- **UID_MAP:** This is the map from a id to the name. Also note that sometimes there are IDs that even logged in you will not be able to find. These are likely deleted accounts or accounts that have blocked or unfriended you.
- **NAME_MAP:** This is the map from a name to the possible nicknames of that person. This may happen if someone has done a name change. In that case all instances of the nickname will be replaced with the name (when being used as a sender). Multiple people having the same nickname is undefined behavior

