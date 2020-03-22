from graphviz import Digraph

# make a tree with a root and a left child and a right child
basicTree = Digraph(format="svg")
basicTree.node("P")
basicTree.node("LC")
basicTree.node("RC")
basicTree.edge("P","LC")
basicTree.edge("P","RC")
basicTree.render("basicTree")

# make a tree with a root and a left child and a right child. right child has 
lcParent = Digraph(format="svg")
lcParent.node("P")
lcParent.node("LC")
lcParent.node("RC")
lcParent.node("LC.LC")
lcParent.node("LC.RC")
lcParent.edge("P","LC")
lcParent.edge("P","RC")
lcParent.edge("LC","LC.LC")
lcParent.edge("LC","LC.RC")
lcParent.render("lcParent")

# make a tree with a labeled root
rootDemo = Digraph(format="svg")
rootDemo.node("0 (Root)")
rootDemo.node("0.0")
rootDemo.node("0.1")
rootDemo.node("0.0.0")
rootDemo.node("0.0.1")
rootDemo.edge("0 (Root)","0.0")
rootDemo.edge("0 (Root)","0.1")
rootDemo.edge("0.0","0.0.0")
rootDemo.edge("0.0","0.0.1")
rootDemo.render("rootDemo")

# make a tree with labeled roots and leaves
rootLeaf = Digraph(format="svg")
rootLeaf.node("0 (Root)")
rootLeaf.node("0.0")
rootLeaf.node("0.1 (Leaf)")
rootLeaf.node("0.0.0 (Leaf)")
rootLeaf.node("0.0.1 (Leaf)")
rootLeaf.edge("0 (Root)","0.0")
rootLeaf.edge("0 (Root)","0.1 (Leaf)")
rootLeaf.edge("0.0","0.0.0 (Leaf)")
rootLeaf.edge("0.0","0.0.1 (Leaf)")
rootLeaf.render("rootLeaf")
