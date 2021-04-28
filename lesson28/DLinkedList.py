class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.adjacent = {}

    def __str__(self) -> str:
        return f"Node data {self.data}" + str([x.data for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_lenth(self):
       return self.lenth()

    def add_node(self):
        return self.data

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

# HEAD | Node("b") -> Node(24) -> Node("st") -> None

class DLinkedList:

    def __init__(self, node) -> None:
        self.head = None
        if node is not None:
            current_node = Node(node.pop(0))
            self.head = current_node
            for elem in node:
                current_node.next = Node(elem)
                current_node = current_node.next
        self.neighbor = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.neighbor.values())

    def add_node(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Node(node)
        self.neighbor[node] = new_vertex
        return new_vertex

    def find(self, searched_data):
        node = self.head
        while node is not None:
            if node.data == searched_data:
                return node
            node = node.next
        return None

    def remove(self, data):

        previous_node = None
        node = self.head
        while node is not None:
            if node.data == data:
                if previous_node is None:
                    self.head = node.next
                    del node
                    return True
                previous_node.next = node.next
                del node
                return True
            previous_node = node
            node = node.next
        return False

    def __str__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


if __name__ == "__main__":
    linked_list = LinkedList(['b', "24", "st", "1213"])

    print(linked_list)

    print(linked_list.remove("b"))
    print(linked_list.remove("1213"))
    print(linked_list)
