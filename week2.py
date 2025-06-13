class Node:
    """Represents a node in the singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Manages the singly linked list."""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Adds a node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Prints the entire list."""
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Deletes the nth node (1-based index)."""
        try:
            if not self.head:
                raise IndexError("Cannot delete from an empty list.")
            if n <= 0:
                raise IndexError("Index must be a positive integer.")

            if n == 1:
                deleted_value = self.head.data
                self.head = self.head.next
                print(f"Deleted node with value: {deleted_value}")
                return

            current = self.head
            count = 1
            while current and count < n - 1:
                current = current.next
                count += 1

            if not current or not current.next:
                raise IndexError("Index out of range.")

            deleted_value = current.next.data
            current.next = current.next.next
            print(f"Deleted node with value: {deleted_value}")

        except IndexError as e:
            print("Error:", e)

# ------------------ TESTING ------------------

# Create a linked list and add nodes
ll = LinkedList()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)

print("Original List:")
ll.print_list()

# Delete the 2nd node
ll.delete_nth_node(2)

print("After deleting 2nd node:")
ll.print_list()

# Try deleting an out-of-range node
ll.delete_nth_node(10)

# Try deleting from an empty list
empty_list = LinkedList()
empty_list.delete_nth_node(1)
