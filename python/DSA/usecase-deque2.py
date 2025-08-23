# Check Browser History (Search, Back, Next)
from collections import deque

class BrowserHistory:
    def __init__(self):
        # 2 objects of deque class
        self.history = deque()
        self.forward_stack = deque()
        
    def visit(self, site):
        self.history.append(site)
        self.forward_stack.clear()
        print(f"You've searched: {site}")
        
    def back(self):
        if len(self.history) > 1:
            site = self.history.pop()
            self.forward_stack.appendleft(site)
            print(f"Back to : {self.history[-1]}")
        else:
            print("No previous site found")
            
    def forward(self):
        if self.forward_stack:
            site = self.forward_stack.popleft()
            self.history.append(site)
            print(f"Forward to : {site}")
        else:
            print("No site to go forward")
            
chrome = BrowserHistory()
chrome.visit("Google")
chrome.visit("Facebook")
chrome.visit("Instagram")
chrome.visit("Whatsapp")

chrome.back()
chrome.back()

chrome.forward()
chrome.forward()

# Tracing:
# history(h) = [], forward_stack(f) = []
# 1) visit("Google")
# h.append("Google") => h = ["Google"]
# f.clear() => f = [] 
# 2) visit("Facebook")
# h.append("Facebook") => h = ["Google", "Facebook"]
# f.clear() => f = [] 
# 3) visit("Instagram")
# h.append("Instagram") => h = ["Google", "Facebook", "Instagram"]
# f.clear() => f = [] 
# 4) visit("Whatsapp")
# h.append("Whatsapp") => h = ["Google", "Facebook", "Instagram", "Whatsapp"]
# f.clear() => f = [] 

# h = ["Google", "Facebook", "Instagram", "Whatsapp"], len(h) = 4, f = [], len(f) = 0 
# back()
# if len(h) > 1 => 4 > 1 - T
    # site = h.pop() => site = "Whatsapp"
    # h = ["Google", "Facebook", "Instagram"]
    # f.appendleft(site) => f = ["Whatsapp"]
    # print(h[-1]) => "Back to Instagram"
# back()
# if len(h) > 1 => 3 > 1 - T
    # site = h.pop() => site = "Instagram"
    # h = ["Google", "Facebook"]
    # f.appendleft(site) => f = ["Instagram","Whatsapp"]
    # print(h[-1]) => "Back to Facebook"
    
# h = ["Google", "Facebook"], f = ["Instagram", "Whatsapp"], len(h) = 2, len(f) = 2
# forward()
# if f[] - T
    # site = f.popleft() => site = "Instagram"
    # f = ["Whatsapp"]
    # h.append(site) => h = ["Google", "Facebook", "Instagram"]
    # print(site) => "Forward to Instagram"
# forward()
# if f[] - T
    # site = f.popleft() => site = "Whatsapp"
    # f = []
    # h.append(site) => h = h = ["Google", "Facebook", "Instagram", "Whatsapp"]
    # print(h[-1]) => "Back to Whatsapp"