#Lists:

#Mutable: You can modify, add, and remove elements after creation.
#Ordered: Elements are stored in the order they are added and can be accessed by index.
#Defined using square brackets [ ].
#Commonly used for sequences of similar items or when you need a mutable collection.


#Tuples:

#Immutable: Once created, elements cannot be modified, added, or removed.
#Ordered: Similar to lists, elements are stored in the order they are added and can be accessed by index.
#Defined using parentheses ( ).
#Often used for sequences of heterogeneous data or to ensure data integrity.


#Sets:

#Mutable: You can add and remove elements after creation, but you cannot modify individual elements directly.
#Unordered: Elements are not stored in any particular order, and duplicates are not allowed.
#Defined using curly braces { }.
#Used when you need to store unique elements or perform set operations like union, intersection, etc.


#Dictionaries:

#Mutable: You can add, remove, and modify key-value pairs after creation.
#Unordered: Elements are stored in an arbitrary order, and the key is used to access the associated value.
#Defined using curly braces { }, with key-value pairs separated by colons :.
#Commonly used for storing and retrieving data based on keys, providing fast lookup times.


marks={"chem":98,"maths":89}
print(marks["chem"])
marks["physics"]=77
print(marks)
