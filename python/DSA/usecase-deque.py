from collections import deque

def is_palindrome(word):
    string = deque(word)
    print(string)
    while len(string) > 1:
        if string.popleft() != string.pop():
            return False
    return True

print(is_palindrome("NAYAN"))
print(is_palindrome("NAYANA"))

# Tracing:
# word = NAYAN, string = ["N", "A", "Y", "A", "N"], len(string) = 5
# while len(string) > 1 => while 5 > 1 => T
    # Step1: 
    # if string.popleft() != string.pop()
    # if "N" != "N" => F
    # Step2: 
    # if string.popleft() != string.pop()
    # if "A" != "A" => F
    # Step3: 
    # if string.popleft() != string.pop()
    # if "Y" != "Y" => F
    # Stop
    # True
    
# word = NAYANA, string = ["N", "A", "Y", "A", "N", "A"], len(string) = 6
# while len(string) > 1 => while 6 > 1 => T
    # Step1: 
    # if string.popleft() != string.pop()
    # if "N" != "A" => T
    # STOP
    # False