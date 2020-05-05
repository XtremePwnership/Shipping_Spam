# Shipping_Spam
This code helps you make add new email IDs to the from field of an existing Gmail filter using a Telegram Bot. 

Simply download everything from the SourceCode folder, make minor changes in each file as instructed, & you're good to go!

In case you're following along with the YouTube video tutorial (url), below are the codes which you can copy/paste.

<h3 id="1">Scope URL @ 4:45: `https://www.googleapis.com/auth/gmail.settings.basic`</h3>

<h2 id="2">Code @ 8:32:</h2>

```python
#Get the existing filter's ID by searching for the Shipping Spam Label's ID & then picking the Filter ID indirectly. Filter ID will keep changing whenever i delete & add a new one, but Filter ID will remain constant until deletion.
    filters = service.users().settings().filters().list(userId='me').execute()
    for f in filters['filter']:
        if f['action'].get('addLabelIds',"") == ['INSERT_YOUR_LABELID_HERE']:
            currFilId =  f['id']
            currEmIds = f['criteria']['from']
```
