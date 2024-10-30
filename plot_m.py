from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np

plt.show()
data = pd.read_csv('data1.csv')


size =data["size"].values
time1 = data["data1"].values
time2 = data["data2"].values
time3 = data["data3"].values
time4 = data["data4"].values
time5 = data["data5"].values
time6 = data["data6"].values
time7 = data["data7"].values
time8 = data["data8"].values
time9 = data["data9"].values

# Create 3D figure
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot each line at different y positions
y_positions = np.arange(1, 10)  # 0 to 8 for nine lines
for i, time_data in enumerate([time9, time8, time7, time6, time5, time4, time3, time2, time1]):
    y_pos = np.full_like(size, y_positions[i])
    ax.plot(y_pos, np.log10(size), time_data, '-o', label=f'data{i+1}')

# Customize the plot
ax.set_xlabel('')
ax.set_ylabel('log(d) (100 nm)')
ax.set_zlabel('relativní zastoupení')
ax.view_init(elev=20, azim=45)  # Adjust viewing angle
plt.legend()

plt.show()

