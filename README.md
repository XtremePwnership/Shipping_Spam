# Shipping_Spam: Update Gmail filters using Python
This code helps you add new email IDs to the from field of an existing Gmail filter using a Telegram Bot. 

Simply download everything from the SourceCode folder, make minor changes in each file as instructed, & you're good to go!

In case you're following along with the YouTube video tutorial, below are the codes which you can copy/paste.

<a href="https://www.youtube.com/watch?v=uFrAssWMaC8&feature=youtu.be"><h3>YouTube Tutorial Part 1/2</h3></a>

<a href="https://www.youtube.com/watch?v=MlATkqqm2RE&feature=youtu.be"><h3>YouTube Tutorial Part 2/2</h3></a> 

<h3 id="1">Scope URL @ 4:45: https://www.googleapis.com/auth/gmail.settings.basic</h3>

<h3 id="2">Code @ 8:32:</h3>

```python
#Get the existing filter's ID by searching for the Shipping Spam Label's ID & then picking the Filter ID indirectly. Filter ID will keep changing whenever i delete & add a new one, but Filter ID will remain constant until deletion.
    filters = service.users().settings().filters().list(userId='me').execute()
    for f in filters['filter']:
        if f['action'].get('addLabelIds',"") == ['INSERT_YOUR_LABELID_HERE']:
            currFilId =  f['id']
            currEmIds = f['criteria']['from']
```

<h3 id="3">Code @ 11:28:</h3>

```
def EmFmt(txt):
    ip = txt.strip()
    list1 = ip.split() #Everything will be put into a list with spaces as delimiter

    final = [] #initialized to hold ONLY the emails from the list
    for item in list1:
      if '@' in item or ('<' in item and '>' in item): #Checks if item in list1 contains @<>. If Yes, then that item (which is the email) is added to final list initialized above. Asking for both angular brackets so that if user inputs additional emails manually separated by space, they get accepted as well.
        final.append(item.strip("<>,;")) #Strips out the angular brackets,comma & semicolon (user might enter comma/semicolon when manually typing emails in terminal), if any, from start & end of item.
      else:
        continue #If item does not contain @<> then it is skipped. Names of the email IDs will be skipped by this.
    op = " OR ".join(final)
    return op, final
```

<h3 id="4">Code @ 12:46:</h3>

```
input, inpWtoutOr = EmFmt(txt)

    if input != "":
        newEmIds = currEmIds + " OR " + input
    else:
        newEmIds=currEmIds
        return 'No new emails supplied.'
        exit()
```

Hope you find the code useful!
