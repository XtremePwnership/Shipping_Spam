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
