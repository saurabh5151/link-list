class Node:
    """A class to represent a node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """A class to manage the singly linked list."""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Added head node: {data}")
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print(f"Added node: {data}")

    def print_list(self):
        """Print all elements of the list."""
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index) from the list."""
        if not self.head:
            raise Exception("Cannot delete from an empty list.")
        if n < 1:
            raise IndexError("Index should be 1 or higher.")

        if n == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            print(f"Deleted head node with data: {deleted_data}")
            return

        current = self.head
        prev = None
        count = 1

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError("Index out of range.")

        prev.next = current.next
        print(f"Deleted node at index {n} with data: {current.data}")

# Testing the implementation
if __name__ == "__main__":
    ll = LinkedList()

    # Adding nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    # Print the list
    ll.print_list()

    # Delete the 3rd node
    try:
        ll.delete_nth_node(3)
    except Exception as e:
        print("Error:", e)

    # Print after deletion
    ll.print_list()

    # Trying to delete node with invalid index
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print("Error:", e)

    # Deleting head node
    try:
        ll.delete_nth_node(1)
    except Exception as e:
        print("Error:", e)

    ll.print_list()

    # Deleting from empty list
    try:
        # Deleting remaining nodes
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)  # Should raise an error
    except Exception as e:
        print("Error:", e)
