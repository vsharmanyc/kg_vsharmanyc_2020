import sys

def isMapping(s1, s2):
	mapping = {}
	for i in range(len(s1)):
		if mapping.setdefault(s1[i],s2[i]) != s2[i]:
			print("{ " + s1[i] +  " , "  + mapping[s1[i]] + ' }  ... ' + s2[i])
			return False
	return True


if len(sys.argv) >= 3:
	print(isMapping(sys.argv[1], sys.argv[2]))
else:
	print("Invalid usage. Must provide two arguments")
