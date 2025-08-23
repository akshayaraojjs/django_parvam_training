# check Airline Queue
import heapq

class AirlineCheckIn:
    def __init__(self):
        self.pq = []  # (negative priority, passenger_name)

    def add_passenger(self, priority, name):
        heapq.heappush(self.pq, (-priority, name))  # Negate priority
        print(f"{name} added with priority {priority}")

    def check_in(self):
        if self.pq:
            priority, name = heapq.heappop(self.pq)
            print(f"Checking in {name} (priority {-priority})")
        else:
            print("No passengers left.")

# Usage
counter = AirlineCheckIn()
counter.add_passenger(3, "Economy John")
counter.add_passenger(5, "Business Sarah")
counter.add_passenger(7, "First Class Mike")

counter.check_in()  # Mike
counter.check_in()  # Sarah
counter.check_in()  # John

# Stock Market Order
import heapq

class StockMarket:
    def __init__(self):
        self.orders = []  # (negative price, order_id)

    def place_order(self, price, order_id):
        heapq.heappush(self.orders, (-price, order_id))
        print(f"Order {order_id} placed at price {price}")

    def execute_order(self):
        if self.orders:
            price, order_id = heapq.heappop(self.orders)
            print(f"Executing order {order_id} at price {-price}")
        else:
            print("No orders left.")

# Usage
market = StockMarket()
market.place_order(100, "Order1")
market.place_order(150, "Order2")
market.place_order(120, "Order3")

market.execute_order()  # Order2
market.execute_order()  # Order3
market.execute_order()  # Order1

# Customer Support System
import heapq

class SupportCenter:
    def __init__(self):
        self.tickets = []  # (-priority, ticket_id)

    def create_ticket(self, priority, ticket_id):
        heapq.heappush(self.tickets, (-priority, ticket_id))
        print(f"Ticket #{ticket_id} created with priority {priority}")

    def resolve_ticket(self):
        if self.tickets:
            priority, ticket_id = heapq.heappop(self.tickets)
            print(f"Resolving ticket #{ticket_id} with priority {-priority}")
        else:
            print("No tickets to resolve")

# Usage
center = SupportCenter()
center.create_ticket(1, "T101")  # Normal
center.create_ticket(5, "T105")  # Urgent
center.create_ticket(3, "T103")  # High

center.resolve_ticket()  # T105
center.resolve_ticket()  # T103
center.resolve_ticket()  # T101