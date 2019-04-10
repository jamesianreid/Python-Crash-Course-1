motorcycles = ['Yamaha', 'Ducati', 'Harley-davidson', 'Honda', 'Suzuki']
print(motorcycles)
# created my first list [',] are crucial to lists
motorcycles[1] = 'Kawasaki'
#changes value 1 'ducati' and replaces with 'kawasaki
motorcycles.append('Ducati')
# .append adds 'ducati' to the end of the list
motorcycles.insert(0, 'Bmw')
# .insert adds 'bmw' to the 0 position within the list
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(0)
#pop removes the last item from the list as if you were poping it off
# changing the value in the () changes what list item is popped off
print("the last motorcycle i owned was a " +last_owned.title()+".")
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

#motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


