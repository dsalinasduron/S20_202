<link rel="stylesheet" href="http://people.westminstercollege.edu/faculty/ggagne/styles.css">
<p id="header">CMPT 201 Lab 3 <br>Sets</p>

### Due: By 5 PM Friday September 13, 2019 

### How Labs are Managed and Graded

1. Select a partner on your own. The rules are you must pair with a new partner each week.
2. Work as a pair to complete the lab. At the end of the lab period, make sure to share all files with each partner.
3. Each partner will submit the lab separately. 
4.  If you do not finish the lab during the lab period, you may either get together outside of class to complete it, or complete it on your own. If you choose to complete it on your own, be sure to indicate this in your submission. 

### Objectives

The objectives of this lab are:

1. Review using Java interfaces
2. Design an implementation of a Set interface
3. Design and run unit tests
4. Apply some principles of programming and software engineering

### Overview

This lab will involve designing a Java class that implements an interface for a set. This lab will introduce the concept of abstraction, an important topic throughout software development.

### The Lab 

Create a new Eclipse project named **lab3** (case-specific).

A **Set** is similar to a Bag except that a set does not allow duplicates.

The following interface defines an ADT for a `Set` object:

[Set.java](./Set.java)

Design a class named `ArraySet` that implements the `Set` interface using an array. The approach will be similar to how a bag was implemented with an array, and it is recommended that you use the `ArrayBag` and `TestArrayBag` as starting points for this lab.

In addition to not having any duplicates, the `Set` interface defines three additional methods as the `Bag` interface:

- `Set union(Set anotherSet)`

- `Set intersection(Set anotherSet)`

- `Set difference(Set anotherSet)`

Below we provide additional details for implementing these methods.

Provide two constructors:

- a default constructor that sets the size of the set to a default value.

- a constructor that allows the original size of the set to be specified.


Your implementation will be similar to the `ArrayBag` in that it will use a variably-sized array to store the elements in the set using the approach highlighted in the `ensureCapacity()` method.

### Unit Tests

Your implementation will be tested against the following unit tests 

[TestArraySet.java](./TestArraySet.java)

### The union()/intersection()/difference() Methods

Assume we have the following set definitions:

$S1 = \{a \; b \; c \; d \; e \; f\}$

$S2 = \{d \; e \; f \; g \; h \; i\}$

### Union

A **union** of two sets combines the elements of both sets, ensuring there are no duplicates.

$S3 = S1.union(S2)$ performs a union of $S1$ and $S2$ which yields $S3 = \{a \; b \; c \;d \;e \;f \;g \;h \;i\}$ (Notice of course $d \;e \;f$ only appear once in resulting set $S3$.)

### Intersection

An **intersection** of two sets yields the values that appear in both sets.

$S3 = S1.intersection(S2)$ performs an intersection of $S1$ and $S2$ which yields $S3 = \{d \;e \;f\}$.

### Difference

The **difference** between $S1$ and $S2$ (which we may also call $S1 - S2$) refers to the elements that are only in $S1$ and not in $S2$.

$S3 = S1.difference(S2)$ calculcates the difference of $S1 - S2$, which yields $S3 = \{a \;b \;c\}$.

**Hint** - You will likely find the easiest strategy is to  implement `difference()` and `intersection()` methods  prior to implementing `union()`.

**Important Things to Consider**

It is important to note that  the parameter type passed to the `union(Set anotherSet)`, `intersection(Set anotherSet)`, and `difference(Set anotherSet)` methods is a `Set`, and not a specific implementation of a `Set`. This means that you can access the elements array for `this` object, but can only  use the methods defined in the `Set` interface to access the data in `anotherSet`.

It is also important that the `union()`/`intersection()`/`difference()` methods do not alter the calling object, or the parameter. For example, if we perform `s3 = s1.union(s2)` , `s1` and `s2` should remain unchanged after the `union()` operation. (Likewise for `difference()` and `intersection()`.)



### Lab Submission

At the completion of the lab period, be sure to share the Java files with your partner. This ensures both partners have all necessary files. **Both** lab partners must upload the following files to the Canvas dropbox for Lab 3:

* `ArraySet.java`

A rubric will be provided for the Canvas dropbox for this lab.

