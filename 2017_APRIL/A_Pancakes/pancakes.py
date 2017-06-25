#flips = 0

def flip(c):
	if c == '+':
		return '-'
	else:
		return '+'

#for my sakes zero index the positions
def flip_num(string, n, pos):
	str_length = len(string)

	if (pos+n) > str_length:
		return []

	# sub_str = string[pos:pos+n]
	# for i in xrange(n):
	# 	sub_str[i] = flip[i]
	# return string[:pos]
	for i in range(pos, pos+n):
		string[i] = flip(string[i])
	#flips += 1
	return string

#greedy strat
def check(string):
	for index, c in enumerate(string):
		if c == '-':
			return index
	return -1

def final_mission(string, n):
	# k = check(string)
	# #print k
	# #print string
	# #print k
	# if not string:
	# 	return -1000
	# elif k == -1:
	# 	#print flips_num
	# 	return flips_num
	# else:
	# 	return final_mission(flip_num(string, n, k), n, flips_num + 1)
	flips = 0
	for index, c in enumerate(string):
		if c == '-':
			string = flip_num(string, n, index)
			if not string:
				return -10000
			flips +=1

	if check(string) == -1:
		return flips
	else:
		return -1000



t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  string, m = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  string = list(string)
  #print string
  #string[0] = flip(string[0])
  m_num = int(m)

  #seems to be doign what I want
  #print flip_num(['+','+','+','-','-','-' ], 3, 5)
  #print check(['+','+','+', '-'])
  x = final_mission(string, m_num)
  #print x

  #change the final print to just one bracket and the number of flips

  #fcheck if number of flips is negatives. if negativers invalid
  #print string, m_num
  target = open('output.txt', 'w')

  if x < 0:
  	x = "IMPOSSIBLE"
  print "Case #{}: {}".format(i, x)
  target.write("Case #{}: {}".format(i, x))
  #target.write('\n')
  target.close()


  # check out .format's specification for more formatting options