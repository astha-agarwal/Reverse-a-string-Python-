
string =  input('Enter a string: ')
length = len(string)
if len == 0:
  print 'Empty string'
  return
else:
  reverse_string = ''
  while length > 0:
    reverse_string += string[length]
    length = length - 1
  return reverse_string

