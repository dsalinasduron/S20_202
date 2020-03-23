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

# recursive tree
count = 0
names = "ABC"
def addChildren(tree, left, height, name):
	global count
	myName = name + (".0" if left else ".1")
	# :(
	if height == 0 :
		myName = "0"
	with tree.subgraph(name=("cluster_" + myName)) as currentTree :
		currentTree.attr(label="Tree " + myName)
		rootName = myName
		if (height < 2) :
			rootName = names[count] 
			currentTree.node(rootName)
			count = count + 1
			leftRt = addChildren(currentTree,True,height+1,myName)
			rightRt = addChildren(currentTree,False,height+1,myName)
			currentTree.edge(rootName,leftRt)
			currentTree.edge(rootName,rightRt)
		else :
			currentTree.node(name=myName,style="dotted",label="empty")
		return rootName
big = Digraph(format="svg")
addChildren(big,True,0,"")
big.render("recursiveTree")

# nonrecursive ABC tree
# make a tree with a root and a left child and a right child
nonRecursive = Digraph(format="svg")
nonRecursive.node("A")
nonRecursive.node("B")
nonRecursive.node("C")
nonRecursive.edge("A","B")
nonRecursive.edge("A","C")
nonRecursive.render("nonRecursive")

# make a tree with a root and a left child
nonRecursive = Digraph(format="svg")
nonRecursive.node("A")
nonRecursive.node("B")
nonRecursive.edge("A","B")
nonRecursive.render("nonRecursive1")

# make a tree with a root and a left child
rec2 = Digraph(format="svg")
with rec2.subgraph(name="cluster_0") as ct :
	ct.attr(label="Tree 0")
	ct.node("A")
	with ct.subgraph(name="cluster_0.0") as b :
		b.attr(label="Tree 0.0")
		b.node("B")
		with ct.subgraph(name="cluster_0.0.0") as e2 :
			e2.attr(label="Tree 0.0.0")
			e2.node(name="e2", label="empty",style="dotted")
			b.edge("B","e2")
		with ct.subgraph(name="cluster_0.0.1") as e3 :
			e3.attr(label="Tree 0.0.1")
			e3.node(name="e3", label="empty",style="dotted")
			b.edge("B","e3")

	with ct.subgraph(name="cluster_0.1") as e1 :
		e1.attr(label="Tree 0.1")
		e1.node(name="e1", label="empty",style="dotted")

	ct.edge("A","B")
	ct.edge("A","e1")
rec2.render("rec2")

# make a tree with a node to be deleted
delete0 = Digraph(format="svg")
delete0.node("60")
delete0.node("48",label="48 (Delete)")
delete0.node("73")
delete0.edge("60","48")
delete0.edge("60","73")
delete0.node("22")
delete0.node("55", label="55 (Successor)")
delete0.edge("48","22")
delete0.edge("48","55")
delete0.node("17")
delete0.node("30",label="30 (Successor)")
delete0.edge("22","17")
delete0.edge("22","30")
delete0.render("delete0")
# make a tree with a node to be deleted, substitute successor
delete1 = Digraph(format="svg")
delete1.node("60")
delete1.node("48",label="30")
delete1.node("73")
delete1.edge("60","48")
delete1.edge("60","73")
delete1.node("22")
delete1.node("55")
delete1.edge("48","22")
delete1.edge("48","55")
delete1.node("17")
delete1.node("30",label="30 (Extra) ")
delete1.edge("22","17")
delete1.edge("22","30")
delete1.render("delete1")
# make a tree with a node to be deleted, substitute successor
delete2 = Digraph(format="svg")
delete2.node("60")
delete2.node("48",label="30")
delete2.node("73")
delete2.edge("60","48")
delete2.edge("60","73")
delete2.node("22")
delete2.node("55")
delete2.edge("48","22")
delete2.edge("48","55")
delete2.node("17")
delete2.edge("22","17")
delete2.render("delete2")
