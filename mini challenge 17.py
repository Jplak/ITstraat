#ik snapte de niet ingevulde plekken van [::-1] line 5 niet helemaal

def isPalindrome(string):
	if(string == string[::-1]):
		return "The string is a palindrome."
	else:
		return "The string is not a palindrome"
		
string = input('enter string:  ')
print(isPalindrome(string))