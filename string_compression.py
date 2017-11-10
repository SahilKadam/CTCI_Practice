
def string_compression(input):
	prev = input[0]
	count = 0
	result = ""
	for i in range(len(input)):
		if input[i] == prev:
			count += 1
		else:
			result += (prev+str(count))
			prev = input[i]
			count = 1
			
	result += (prev+str(count))
			
	return (result)
		

def main():
	input = "abcd"
	result = string_compression(input)
	print ("Result is: %s" % result)

if __name__ == "__main__":
	main()

	