# Checking the Priority number with descending order
import heapq

class LeaderBoard:
    def __init__(self):
        self.scoreboard = [] # empty list
        
    def add_score(self, score, player):
        heapq.heappush(self.scoreboard, (-score, player))
        print(f"Player {player} scored {score} runs")
        
    def top_performers(self):
        if self.scoreboard:
            score, player = heapq.heappop(self.scoreboard)
            print(f"Top Performers are: {player} scored {abs(score)}")
        else:
            print("No players has scored yet")
    
cricket = LeaderBoard()

cricket.add_score(30, "Sudeep")
cricket.add_score(50, "Manoj")
cricket.add_score(20, "Rohit")
cricket.add_score(35, "Vishwas")

cricket.top_performers()
cricket.top_performers()
cricket.top_performers()
cricket.top_performers()