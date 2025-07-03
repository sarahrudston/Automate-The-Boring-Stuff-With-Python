def is_phone_number(text):
    if len(text) != 12: # US phone numbers have exactly 12 characters.
        return False
    for i in range(0, 3): # The first three characters must be numbers.
        if not text[i].isdecimal():
            return False
    if text[3] != '-': # The fourth character must be a dash.
            return False
    for i in range(4, 7): # The next three characters must be numbers.
         if not text[i].isdecimal():
              return False
    if text[7] != '-': # The eighth character must be a dash.
         return False
    for i in range(8, 12): # The next four characters must be numbers.
         if not text[i].isdecimal():
              return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    segment = message[i:i+12]
    if is_phone_number(segment):
        print('Phone number found: ' + segment)
print('Done')