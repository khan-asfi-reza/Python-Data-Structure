from Nodes.nodes import DynamicNode


class DoublyLinkedList:
    # Every linked list has a head and a tail,
    # head and tail will be DynamicNode instance

    # In this linked list class, head and tail will be a private|immutable property
    __head = None
    __tail = None

    # The head can be assigned only using this private method
    def __set_head(self, node: DynamicNode):
        self.__head = node

    # The tail can be assigned only using this private method
    def __set_tail(self, node: DynamicNode):
        self.__tail = node

    # Accessor Method of class , returns head node
    def get_head(self):
        return self.__head

    # Accessor Method of class , returns tail node
    def get_tail(self):
        return self.__tail

    # Returns data of the head node
    @property
    def head(self):
        return self.__head

    # Returns data of the tail node
    @property
    def tail(self):
        return self.__tail

    # Creates linked list from multiple value
    def __create(self, args):
        # Declaring the previous node
        previous = None
        # Looping through the data
        for i in args:
            # Creating node instance with the looped instance data
            current = DynamicNode(i, previous=previous)
            # If previous node is not None then previous node's next will be the current node instance
            if previous is not None:
                previous.next = current
            # Otherwise we will set the head to the current node
            else:
                self.__set_head(current)
            # Setting the previous node as the current node in the end of the loop
            previous = current
            # If looped data instance is the last elem of the args, it will be the tail
            if i == args[-1]:
                self.__set_tail(current)

    # Gets the previous node of a given node
    @staticmethod
    def __get_previous_node(node):
        # Declaring the current node and setting head to it
        return node.previous

    # Maps through all the nodes, map method will take a function as parameter and param->function must have a val param
    def __map(self, function):
        # Declaring the current node and setting head to it
        current = self.__head
        # Looping through all the nodes and executing the param->function
        while current:
            function(current)
            current = current.next

    def __print(self):
        # Declaring returning value for printing/display
        print_state = f""

        # Function for the map method
        def make_str(val):
            #  Nonlocal to declare that the variable is not local and getting print_state from outer scope
            nonlocal print_state
            if val.next is None:
                print_state += f"{val.data} "
            else:
                print_state += f"{val.data} <-> "

        self.__map(make_str)
        return print_state

    # Construction method to create linked list object
    def __init__(self, *args):
        self.__create(args)

    # Returns structured string when the class instance object is called
    def __str__(self):
        return f"{self.__print()}"

    # Prepend nodes in the beginning of the linked list
    def prepend(self, *args):
        # Head of the linked list
        head = self.__head
        # List the pre-appending values
        nodeList = list(args)
        current = None
        if len(nodeList) > 0:
            # Looping through the node list
            for each in nodeList:
                # Creating instance node for that value
                node = DynamicNode(each, previous=current)
                # If the value is the first element of the node, make it head
                if each == nodeList[0]:
                    self.__set_head(node)
                    node.next = head
                    head.previous = node
                elif len(nodeList) > 1 and each == nodeList[-1]:
                    # If the instance loop element is the last element of the provided arg list
                    # Set the next node of the current loop element node to previous head of the linked list
                    node.next = head
                    head.previous = node
                    # Set the tail of the head as previous head of the node
                    if self.__tail is None:
                        self.__set_tail(head)
                # Setting current node
                if current is not None:
                    current.next = node
                    node.previous = current
                current = node

    # Add value at the end of the linked list
    def append(self, *args):
        # Previous head of the
        self.__create(*args)

    # Gets item from that instance
    def get(self, index: int) -> DynamicNode:
        # Iteration value
        itr = 0
        # Current working node
        current = self.__head
        # Traversing through the linked list
        while True:
            # If current iteration value is the index, return the current working node
            if itr == index:
                return current
            elif current is None:
                # Index out of range
                raise IndexError(f"DynamicNode at {index} does not exist, Index out of range")
            itr += 1
            current = current.next

    # Get index using value
    def index(self, value):
        # Iteration value
        itr = 0
        # Current working node
        current = self.__head
        while True:
            # If current working node value is the provided value
            if current.data == value:
                # Return the iteration value which is the index of the DynamicNode with that value in the linked list
                return itr
            # Else Return none if there is no node with the given value
            elif current is None:
                return None
            itr += 1
            current = current.next

    # Remove node using index
    def remove(self, index):
        # Prev node of current working node
        prev = None
        # Current Working DynamicNode
        current = self.__head
        # Iteration Index
        itr = 0
        # Traversing through the list
        while current:
            # If iteration index and given index is same
            if itr == index:
                # If head is the current working node, set head to it's next node
                if current == self.__head:
                    self.__head = self.__head.next
                    self.__head.previous = None
                else:
                    prev.next = current.next
                    current.next.previous = prev
            itr += 1
            prev = current
            current = current.next

    # Get length of the linked list
    def length(self):
        itr = 0

        def iterate(val):
            nonlocal itr
            itr += 1

        self.__map(iterate)
        return itr

    # Insert into linked list
    def insert(self, index=None, value=None):
        # If index is greater than the length, raise error
        if index > self.length() - 1:
            raise IndexError("Index out of range")
        # Create node using given value
        node = DynamicNode(data=value)
        # Set working node
        current = self.__head
        # Set iteration Time
        itr = 0
        # Traversing through the list
        while current:
            if itr == index == 0:
                self.__head = node
                node.next = current
                current.previous = node
                break
            elif itr == index:
                prev = self.__get_previous_node(current)
                prev.next = node
                node.next = current
                node.previous = prev
                break
            current = current.next
            itr += 1

    # Reverse the linked list
    def reverse(self):
        temp = None
        current = self.__head
        # Swap next and prev for all nodes of
        # doubly linked list
        while current is not None:
            temp = current.previous
            current.previous = current.next
            current.next = temp
            current = current.previous

        # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            self.__head = temp.previous

    # Converts linked list into python list
    def to_list(self):
        list_of_linked_list = []
        # Mapping through each element in the linked list

        self.__map(lambda each: list_of_linked_list.append(each.data))
        # Returns the list of linked list
        return list_of_linked_list

    # Maps or travers through the linked list
    def map(self, function):
        def wrapper():
            self.__map(function)

        return wrapper

    # Len(Linked List Object) returns length 0f linked list object
    def __len__(self):
        return self.length()

    def __getitem__(self, item):
        return self.get(item).data


