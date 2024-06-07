from graphviz import Digraph
class Node:
    def __init__(self, value=None):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1  # Red is 1, Black is 0
        self.id = id(self)  # Unique identifier for each node

class RBTree:
    def __init__(self):
        self.TNULL = Node()
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == self.TNULL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == self.TNULL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_node(self, z: Node):
        x = self.root
        y = self.TNULL
        while x != self.TNULL:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == self.TNULL:
            self.root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z

        z.left = self.TNULL
        z.right = self.TNULL
        z.color = 1

        self.insert_fixup(z)

    def insert_fixup(self, z: Node):
        while z.parent.color == 1:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 1:
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 1:
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.left_rotate(z.parent.parent)

        self.root.color = 0

    def transplant(self, u: Node, v: Node):
        if u.parent == self.TNULL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_node(self, value):
        z = self.search_tree(value)
        if z == self.TNULL:
            print(f"Node with value {value} not found.")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fixup(x)

    def delete_fixup(self, x: Node):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 1:
                    w.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 0 and w.right.color == 0:
                    w.color = 1
                    x = x.parent
                else:
                    if w.right.color == 0:
                        w.left.color = 0
                        w.color = 1
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 0
                    w.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 1:
                    w.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 0 and w.left.color == 0:
                    w.color = 1
                    x = x.parent
                else:
                    if w.left.color == 0:
                        w.right.color = 0
                        w.color = 1
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 0
                    w.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def minimum(self, node: Node):
        while node.left != self.TNULL :
            node = node.left
        return node

    def search_tree(self, value):
        return self.search_tree_helper(self.root, value)

    def search_tree_helper(self, node, value):
        if node == self.TNULL or value == node.value:
            return node
        if value < node.value:
            return self.search_tree_helper(node.left, value)
        return self.search_tree_helper(node.right, value)

    def add(self, a: int):
        self.insert_node(Node(a))

    def pre_order_traversal(self, node):
        if node != self.TNULL:
            print(node.value, end=' ')
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node != self.TNULL:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value, end=' ')

    def in_order_traversal(self, node):
        if node != self.TNULL:
            self.in_order_traversal(node.left)
            print(node.value, end=' ')
            self.in_order_traversal(node.right)

    def visualize(self, filename="RBTREE"):
        def add_edges(graph, node):
            if node != self.TNULL:
                if node.left != self.TNULL:
                    graph.edge(f"{node.value}_{node.id}", f"{node.left.value}_{node.left.id}")
                if node.right != self.TNULL:
                    graph.edge(f"{node.value}_{node.id}", f"{node.right.value}_{node.right.id}")
                add_edges(graph, node.left)
                add_edges(graph, node.right)

        graph = Digraph(format='svg')
        graph.node(name=f"{self.root.value}_{self.root.id}", label=str(self.root.value), color="black" if self.root.color == 0 else "red")

        def add_nodes(graph, node):
            if node != self.TNULL:
                graph.node(name=f"{node.value}_{node.id}", label=str(node.value), color="black" if node.color == 0 else "red")
                add_nodes(graph, node.left)
                add_nodes(graph, node.right)

        add_nodes(graph, self.root)
        add_edges(graph, self.root)

        graph.render(filename)
