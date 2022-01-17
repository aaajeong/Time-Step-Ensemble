from matplotlib import pyplot as plt
import numpy as np

x_values = np.arange(10)


esb_list = []
plt.plot(x_values, esb_list)


# plt.legend(['Survival', 'Majority', 'Single'])

plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Single Model 1 TQE')
plt.show()


# y_values_1 = [10, 12, 12, 10, 14, 22, 24]
# y_values_2 = [11, 14, 15, 15, 22, 21, 12]

# plt.plot(x_values, y_values_1)
# plt.plot(x_values, y_values_2)

# plt.show()