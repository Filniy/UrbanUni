calls = 0

def count_calls():
  global calls
  calls +=1

def string_info(string):
  count_calls()
  transfer = str(string)
  list_to_search = (len(transfer),               transfer.upper(),transfer.lower())
  return list_to_search


def is_contains(string, list_to_search):
  count_calls()
  string = str(string).lower()
  list_to_search = list(list_to_search)
  for i in range(len(list_to_search)):
      if str(list_to_search[i]).lower() == string:
          result = True
          break
      else:
          result = False
          continue
  return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
#Done


  