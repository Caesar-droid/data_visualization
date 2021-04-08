from die import Die

#Create a d6
die=Die()

#make some rolls, and store results in a list.
results=[]
for roll_num in range(1000):
    result=die.roll()
    results.append(result)
#Analyze the results.
frequencies =[]
for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)

print(frequencies)