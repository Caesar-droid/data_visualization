import matplotlib.pyplot as plt
x_values =range(1,5001)
y_values =[x**3 for x in x_values]
plt.style.use('seaborn')
fig,ax =plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)

#set chart title and axes
ax.set_title("Cubes Numbers",fontsize=24)
ax.set_xlabel("Values",fontsize=14)
ax.set_ylabel("Cubes of Values",fontsize=14)
#set ticks in labels
ax.tick_params(axis='both',which='major',labelsize=24)
#set range for each axis
ax.axis([0,5000,0,125000000000])



plt.show()