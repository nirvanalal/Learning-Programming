def runLengthEncoding(string):
    # Write your code here.
	curr_run_length = 1
	chars = [] #empty list because list are immutable unlike strings (things can be added)
	
	for i in range(1, len(string)):
		curr_char = string[i]
		prev_char = string[i-1]
	
		if curr_char != prev_char or curr_run_length == 9:
			chars.append(str(curr_run_length))
			chars.append(prev_char)
			curr_run_length = 0 #reset to 0
			
		curr_run_length += 1
		
	chars.append(str(curr_run_length))
	chars.append(string[len(string) - 1])
	
	return "".join(chars)