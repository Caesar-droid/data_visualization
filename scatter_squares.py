import matplotlib.pyplot as plt
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]
plt.style.use('seaborn')
fig,bx = plt.subplots()
bx.scatter(x_values ,y_values, s=100)

#set chart title and label axes.
bx.set_title("Square Numbers",fontsize=24)
bx.set_xlabel("Value",fontsize=14)
bx.set_ylabel("Square of Value",fontsize=14)

#set size of tick labels.
bx.tick_params(axis='both',which='major',labelsize=14)

plt.show()