#                          
# NO CODE HERE
#
# QUESTION 1
#  
# NO CODE HERE
#
def password_check(password):           # DO NOT CHANGE THIS LINE 
  result = True                         # DO NOT CHANGE THIS LINE 
  #
  # Your code here

  # check if it's at least 8 characters
  if len(password) < 8:
    result = False
    
  # check if it contains question mark
  if '?' in list(password):
    result = False
    
  # check if it has at least 1 numerical, 1 alphabetical & 1 special character
  abc_cnt = 0
  num_cnt = 0
  spec_cnt = 0
  for i in list(password):
    if 48 <= ord(i) <= 57:
      num_cnt += 1
    elif 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
      abc_cnt += 1
    else:
      spec_cnt += 1
  if num_cnt == 0 or abc_cnt == 0 or spec_cnt == 0:
    result = False
    
  # check if it contains the same character more than two times consecutively
  for idx in range(0,len(password)-2):
    if password[idx] == password[idx+1] == password[idx+2]:
      result = False
    
  #number of distinct characters in the password must not be less than half of the password’s length
  set_password = set(password)
  if len(set_password) < (len(password) / 2):
    result = False

  #
  return result                         # DO NOT CHANGE THIS LINE 
# 
# Only use this space to write helper functions (if necessary)
#
if __name__ == "__main__":              # DO NOT CHANGE THIS LINE 
  print(password_check('a12#8'))        # DO NOT CHANGE THIS LINE 
  print(password_check('a1234567#?'))   # DO NOT CHANGE THIS LINE 
  print(password_check('abcdefgh#'))    # DO NOT CHANGE THIS LINE 
  print(password_check('a12345678'))    # DO NOT CHANGE THIS LINE 
  print(password_check('12345678#'))    # DO NOT CHANGE THIS LINE 
  print(password_check('abbbcd1@'))     # DO NOT CHANGE THIS LINE 
  print(password_check('a1@a1@1@'))     # DO NOT CHANGE THIS LINE 
  print(password_check('a123456#7'))    # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
###################################################### QUESTION 2
#  
# NO CODE HERE
#
def word_counter(file_name):            # DO NOT CHANGE THIS LINE 
  result = 0                            # DO NOT CHANGE THIS LINE 
    #
    # Your code here
  with open(file_name) as file:
    text = file.read()
  result = len(text.split())
    #
  return result                         # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
if __name__ == "__main__":              # DO NOT CHANGE THIS LINE 
  print(word_counter('input1.txt'))     # DO NOT CHANGE THIS LINE 
  print(word_counter('input2.txt'))     # DO NOT CHANGE THIS LINE 
  print(word_counter('input3.txt'))     # DO NOT CHANGE THIS LINE 
  print(word_counter('input4.txt'))     # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
def most_frequent(file_name):           # DO NOT CHANGE THIS LINE 
  result1 = ''                          # DO NOT CHANGE THIS LINE 
  result2 = 0                           # DO NOT CHANGE THIS LINE 
    #
    # Your code here
  with open(file_name) as file:
    text = file.read()
  myDict = {}                            # create a dictionary
  file_name_2 = text.lower()        # all words turn into lower case
  for word in (file_name_2.split()):
    if word not in myDict:
      myDict[word] = 1
    elif word in myDict:
      myDict[word] += 1
  result2 = max(myDict.values())         # how many times the most frequent word has appeared
  for word, num in myDict.items():       # here we grab the most frequent word by its value
    if num == result2:
      result1 = word
    #
  return result1, result2               # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
if __name__ == "__main__":              # DO NOT CHANGE THIS LINE 
  print(most_frequent('input1.txt'))    # DO NOT CHANGE THIS LINE 
  print(most_frequent('input2.txt'))    # DO NOT CHANGE THIS LINE 
  print(most_frequent('input3.txt'))    # DO NOT CHANGE THIS LINE 
  print(most_frequent('input4.txt'))    # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#