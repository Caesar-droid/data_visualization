import matplotlib.pyplot as plt
x_values=range(1,1001)
y_values=[x**2 for x in x_values]
plt.style.use('seaborn')
fig,bx = plt.subplots()
bx.scatter(x_values ,y_values, c=y_values,cmap=plt.cm.Blues, s=10)

#set chart title and label axes.
bx.set_title("Square Numbers",fontsize=24)
bx.set_xlabel("Value",fontsize=14)
bx.set_ylabel("Square of Value",fontsize=14)

#set size of tick labels.
bx.tick_params(axis='both',which='major',labelsize=14)

#set the range for each axis
bx.axis([0,1100,0,1100000])

plt.savefig("squares_plot.png",bbox_inches='tight')