from DynamicArray import DynamicArray

my_array = DynamicArray(3)
my_array2 = DynamicArray(3)
# we allocated memory location for 3 elements.
my_array.insert(10)
my_array.insert(20)
my_array.insert(30)

my_array.insert(50)
my_array.insert_at(4, 70)
my_array.print()
