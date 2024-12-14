












word = input(" type a word: ")
palindrome = True


for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:   
            palindrome = False
if palindrome:
        print("ye its a palindrome.")
else:
        print("no its not a palindrome.")       