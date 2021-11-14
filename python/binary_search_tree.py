class Node:
    """
    A custom implementation of the Binary Search Tree data structure
    providing an in-order, pre-order, and post-order traversal methods
    as well as an insert method.
    """

    def __init__(self, data):
        """
        Create a new Node object with comparable data.
        Args:
             data: Any type object to be encapsulated as the data item within
             a specific node. 
        """
        # Encapsulates data to new Node object
        self.data = data
        
        # Sets the initial references to left and 
        # right child Nodes to None
        self.left = None
        self.right = None
        
    def insert(self, data) -> NoReturn:
        """
        Takes a new instance of the data stored in the Node object
        and inserts accordingly.
        Args:
            data: Any type object
        """

        # Do nothing if not data
        if self.data:

            # Where data value is less than current, branch left
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            # Where data is greater than current, branch right
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def in_order(self, root: "Node") -> List[Any]:
        """ 
        Traverse the tree in an 'in order' fashion 
        Args:
            root: The node from which the traversal starts.
        Returns:
            List object containing data from each Node in order.
        """
        # Create and output container
        output = []

        # Starting at the specified Node,
        # traverse in Left, Root, Right fashion
        if root:
            # Check Left
            output = self.in_order(root.left)

            # Check Root
            output.append(root.data)

            # Check Right, add output to current output
            output = output + self.in_order(root.right)

        # Returns the list of Nodes in-order
        return output

    def pre_order(self, root: "Node") -> List[Any]:
        """
        Traverse the tree in a pre-order fashion
        Args:
            root: The node from which the traversal starts.
        Returns:
            List object containing data from each Node in order.
        """
        # Create and output container
        output = []

        # Starting at the specified Node,
        # traverse in Root, Left, Right fashion
        if root:

            # Get Root Node Data
            output.append(root.data)

            # Get the Left Node Data and append to current
            output = output + self.pre_order(root.left)

            # Get the Right node data and append to current
            output = output + self.pre_order(root.right)

        # Returns the list of Nodes in pre-order
        return output

    def post_order(self, root: "Node") -> List[Any]:
        """
        Traverse the tree in a post-order fashion
        Args:
            root: The node from which the traversal starts.
        Returns:
            List object containing data from each Node in order.
        """
        # Create an output container
        output = []

        # Starting at the specified node,
        # Traverse in a left, right, root fashion
        if root:
            # Get left node data
            output = self.post_order(root.left)

            # Get right node data
            output = output + self.post_order(root.right)

            # Get root data
            output.append(root.data)

        # Returns a list of node data in pre-order
        return output
