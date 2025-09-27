'''
Searching

1. Linear Search - Searching an element in a Linear data structure like a list.
   Time Complexity of the Linear Search is O(n) which means n comparisions to n elements.

2. Binary Search - Seaching an element in a Binary data structure but the condition is it should be sorted first.
   Time Complexity of the Binary Search is O(Log n) which means 10 comparisions to 1000 elements. 
   Better Performance.
   
   
   
Hashing - It is the technique of mapping keys and values into the hash table by using a hash function.
If implemented correctly then one can achieve O(1) time complexity in searching items in the collection of elements.

Why Hashing? It is designed to solve the problem of needing to efficiently find or store an item in a collection.

Key Terms:- 
1. Hash table - It is the data structure used to store elements.
2. Hash Function - It is a function to map key values to the memory address.
3. Hashing - It is the method for storing and retrieving records from a database.

Collision - It occurs when two records hash to the same slot in the table. Even under the best circumstances,collisions are unavoidable.
Collision occurs when there are more keys than indexes.

Hash Functions - The HF creates a mapping between the key and the value, this is done through the use of the 
math formulas.

various Hash Functions:-
1. Simple Mod function
2. Division method
3. Binning
4. Mid Square method

Collision Resolution:-
1. Open Hashing - When collision happens, instead of overriding another memory block is created and like a linear search data is stored.
2. Closed Hashing - Instead of creating new memory block, it searches for vacant space within the same memory keys.


Time Complexity

   '''