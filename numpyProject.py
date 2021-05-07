#Simple Graph showing the number and ages of kids that loves animes

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x_axis = [4,7,9]
y_axis = [13,17,6]

x2_axis = [5,10,12]
y2_axis = [7,10,7]


plt.bar(x_axis, y_axis, color='y', align='center')

plt.bar(x2_axis, y2_axis, color='b', align='center')


plt.title('Love animes')
plt.ylabel('Age')
plt.xlabel('Kids')

plt.show()