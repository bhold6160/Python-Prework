pyg = 'ay'
original = 'hippo'
word = original.lower()
first = word[0]
new_word = word + first + pyg

if len(original) > 0 and original.isalpha():
  print original
else:
  print 'empty'

new_word = new_word[1:len(new_word)]

print(new_word)
