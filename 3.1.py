calls = 0
def count_calls():
     global calls
     calls += 1
     return

def  string_info(string):
     count_calls()
     a = ()
     a = len(string), string.upper(), string.lower()
     return a

def is_contains(string, list_to_search):
     count_calls()
     a = True
     b = "".join(list_to_search).lower()
     if b.find(string.lower()) == -1:
      a = False
     return a


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)