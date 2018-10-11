def is_palindrome(input_string):
 beginning = 0
 end = len(input_string)-1
 while beginning < end:
    if input_string[beginning] != input_string[end]:
      return False
    beginning +=1
    end -=1
  return True