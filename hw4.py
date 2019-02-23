#                          
# NO CODE HERE
#
################################################################################# QUESTION 1
#                          
# NO CODE HERE
#
import math                     # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
def step_count(ins_str):        # DO NOT CHANGE THIS LINE 
  result = 0                    # DO NOT CHANGE THIS LINE 
    #
    # Your code here
  for idx in range(0,len(ins_str)):
    if ins_str[idx] in {'u','U','d','D','l','L','r','R'}:
      result += 1
    else:
      return -1
    #
  return result                 # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
def distance(ins_str):          # DO NOT CHANGE THIS LINE 
  result = 0                    # DO NOT CHANGE THIS LINE 
    #
    # Your code here
  ins_str = ins_str.lower()
  left_step, right_step, up_step, down_step = 0, 0, 0, 0 
  for idx in range(0,len(ins_str)):
    if ins_str[idx] == 'l':
      left_step += 1
    elif ins_str[idx] == 'r':
      right_step += 1
    elif ins_str[idx] == 'u':
      up_step += 1
    elif ins_str[idx] == 'd':
      down_step += 1
    else:
      return -1
  hor_step = abs(left_step - right_step)            # horizontal total steps
  ver_step = abs(up_step - down_step)               # vertical total steps
  result = round(math.sqrt(pow(hor_step,2) + pow(ver_step,2)),4)
    #  
  return result                 # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
if __name__ == "__main__":      # DO NOT CHANGE THIS LINE 
  print(step_count('LRlURRDu')) # DO NOT CHANGE THIS LINE
  print(distance('LRlURRDu'))   # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#                                                  
################################################################################# QUESTION 2
#                          
# NO CODE HERE
#
def compress(input_str):                            # DO NOT CHANGE THIS LINE
  result = ''                                       # DO NOT CHANGE THIS LINE
    #
    # Your code here
  if input_str is None:
    result = ''
  elif len(input_str) == 1:
    result += input_str
    result += str(1)
  elif len(input_str) >= 1:
    result += input_str[0]
    count = 1
  for i in range(1,len(input_str)):
    if input_str[i] == input_str[i-1]:
      count += 1
      if i == len(input_str)-1:
        result += str(count)
    elif input_str[i] != input_str[i-1]:
      result += str(count)
      result += input_str[i]
      count = 1
    #
  return result                                     # DO NOT CHANGE THIS LINE
#                          
# NO CODE HERE
#
if __name__ == "__main__":                          # DO NOT CHANGE THIS LINE 
  print(compress(''))                               # DO NOT CHANGE THIS LINE
  print(compress('a'))                              # DO NOT CHANGE THIS LINE
  print(compress('AAAAATTTTGGGGCCCCAAA'))           # DO NOT CHANGE THIS LINE
  print(compress('##########'))                     # DO NOT CHANGE THIS LINE
  print(compress('zzz ZZ  zZzZ'))                   # DO NOT CHANGE THIS LINE
#                          
# NO CODE HERE
#
################################################################################# QUESTION 3
#
# NO CODE HERE
#
def any_smaller(lst, level):    # DO NOT CHANGE THIS LINE 
  result = False                # DO NOT CHANGE THIS LINE
    #
    # Your code here
  temp = []
  for n in lst1:
    each_min = min(sorted(n))
    temp.append(each_min)
  min_num = min(temp)
  if level > min_num:
    result = True
  else:
    result = False
    #
  return result                 # DO NOT CHANGE THIS LINE
#                          
# NO CODE HERE
#
def all_smaller(lst, level):    # DO NOT CHANGE THIS LINE 
  result = True                 # DO NOT CHANGE THIS LINE
    #
    # Your code here
  temp = []
  for n in lst1:
    each_max = max(sorted(n))
    temp.append(each_max)
  max_num = max(temp)
  if level > max_num:
    result = True
  else:
    result = False
    #
  return result                 # DO NOT CHANGE THIS LINE
#                          
# NO CODE HERE
#
def max_exp(lst, level):        # DO NOT CHANGE THIS LINE
  result = 0                    # DO NOT CHANGE THIS LINE
    #
    # Your code here
  new_lst = []
  new_sum = []
  k = 0
  for i in range(0, len(lst)-1):             # dimension 1
    for j in range(0, len(lst[0])-1):      # dimension 2
      new_lst = [ lst[i][j], lst[i+1][j], lst[i][j+1], lst[i+1][j+1] ]
      for num in new_lst:
        if num < level:
          k += num
        else:
          break
      new_sum.append(k)
      k = 0  
  result = max(new_sum)
    #
  return(result)                # DO NOT CHANGE THIS LINE
#                          
# NO CODE HERE
#
if __name__ == "__main__":      # DO NOT CHANGE THIS LINE 
  lst1 = [[5,4,3],              # DO NOT CHANGE THIS LINE 
         [6,7,8],               # DO NOT CHANGE THIS LINE 
         [4,7,8]]               # DO NOT CHANGE THIS LINE 
  lst2 = [[7,7,7,7,7],          # DO NOT CHANGE THIS LINE 
          [1,6,5,5,5],          # DO NOT CHANGE THIS LINE 
          [9,8,5,5,1]]          # DO NOT CHANGE THIS LINE 
  print(any_smaller(lst1, 3))   # DO NOT CHANGE THIS LINE 
  print(any_smaller(lst1, 4))   # DO NOT CHANGE THIS LINE 
  print(all_smaller(lst1, 8))   # DO NOT CHANGE THIS LINE 
  print(all_smaller(lst1, 10))  # DO NOT CHANGE THIS LINE 
  print(max_exp(lst1, 9))       # DO NOT CHANGE THIS LINE 
  print(max_exp(lst2, 7))       # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#