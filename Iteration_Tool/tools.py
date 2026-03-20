# Iterable Object (lists, tuples, etc.) :- it is a object on which iteration can be performed.
# Iterator(loop , comprehension) :- it is a tool which can be used to perform iteration on an iteration object.
# __next__() :- t is a method of an iterator that returns the next item from the iterator.
#               When no items are left, it raises StopIteration. 

#myList = [1, 2, 3, 4]
#I = iter(myList) # creating an iterator object from the list
#print(I)
#print(next(I)) # Output: 1
#print(I)
#print(next(I)) # Output: 2      
#print(next(I)) # Output: 3
#print(I)
#print(next(I)) # Output: 4
#print(next(I)) # Output: StopIteration error because there are no more items left in the iterator.

#I hamesha memory reference same he hota h that is base(starting position ) , lekin uska jo iterator hota h (next) wo ek ek karke move karta h aage 

f = open(r"e:\Python-Revision-Problems\Iteration_Tool\tools.py")
iter(f) is f # Output: True, because the file object itself is an iterator, so iter(f) returns the same file object f. Different from list or tuple where iter() creates a new iterator object.

#“In a list, we need to create an iterator object to iterate over it, but in a file, we can directly iterate over the file using its name because the file object itself is an iterator.”
