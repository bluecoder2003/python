import matplotlib.pyplot as plt
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
consumption = [300, 320, 280, 350, 400, 420, 380, 390, 370, 360, 330, 310]
plt.plot(month,consumption)
plt.xlabel("month")
plt.ylabel("consumption")
plt.show()