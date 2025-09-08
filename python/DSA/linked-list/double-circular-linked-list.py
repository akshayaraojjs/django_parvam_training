class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    # Traversal
    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

    # Insert at start
    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node.prev = new_node
            self.head = new_node
            return
        tail = self.head.prev
        new_node.next = self.head
        new_node.prev = tail
        tail.next = new_node
        self.head.prev = new_node
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        if not self.head:
            self.insert_at_start(data)
            return
        new_node = Node(data)
        tail = self.head.prev
        new_node.next = self.head
        new_node.prev = tail
        tail.next = new_node
        self.head.prev = new_node

    # Insert after a given value
    def insert_after_value(self, target, data):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                new_node.prev = current
                current.next.prev = new_node
                current.next = new_node
                return
            current = current.next
            if current == self.head:
                break
        print(f"Value {target} not found")

    # Delete at start
    def delete_at_start(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:  # only one node
            self.head = None
            return
        tail = self.head.prev
        self.head = self.head.next
        self.head.prev = tail
        tail.next = self.head

    # Delete at end
    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:  # only one node
            self.head = None
            return
        tail = self.head.prev
        tail.prev.next = self.head
        self.head.prev = tail.prev

    # Delete by value
    def delete_by_value(self, target):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            if current.data == target:
                if current.next == current:  # only one node
                    self.head = None
                    return
                if current == self.head:  # deleting head
                    self.delete_at_start()
                    return
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next
            if current == self.head:
                break
        print(f"Value {target} not found")


# Menu-driven program
if __name__ == "__main__":
    dcll = DoublyCircularLinkedList()

    while True:
        print("\n--- Doubly Circular Linked List Menu ---")
        print("1. Display List")
        print("2. Insert at Start")
        print("3. Insert at End")
        print("4. Insert after Value")
        print("5. Delete at Start")
        print("6. Delete at End")
        print("7. Delete by Value")
        print("8. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            dcll.display()
        elif choice == 2:
            val = int(input("Enter value: "))
            dcll.insert_at_start(val)
        elif choice == 3:
            val = int(input("Enter value: "))
            dcll.insert_at_end(val)
        elif choice == 4:
            target = int(input("Enter value to insert after: "))
            val = int(input("Enter new value: "))
            dcll.insert_after_value(target, val)
        elif choice == 5:
            dcll.delete_at_start()
        elif choice == 6:
            dcll.delete_at_end()
        elif choice == 7:
            target = int(input("Enter value to delete: "))
            dcll.delete_by_value(target)
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")