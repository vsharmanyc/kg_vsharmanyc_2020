import sys

"""
isMapping(s1, s2)

s1: string 1
s2: string 2

returns True if s1 is a one-to-one character mapping to s2, else False
"""
def isMapping(s1, s2):
	# return false if s1 and s2 are not the same length
	if len(s1) != len(s2):
		return False

	# used to store mappings of characters from s1 to s2 as key,value pairs
	mappings = {}

	for i in range(len(s1)):
		# map s1[i] to s2[i] if not done so already
		# if s1[i] is already mapped check if its value is not different than s2[i]
		if mappings.setdefault(s1[i],s2[i]) != s2[i]:
			return False

	return True


# driver code : gets command line arguments and prints result of isMapping()

if len(sys.argv) < 3:
	print("Invalid usage. Must provide two arguments")
elif isMapping(sys.argv[1], sys.argv[2]):
	print("true")
else:
	print("false")
