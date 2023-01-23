import pandas as pd
import matplotlib.pyplot as plt

df0 = pd.read_excel('sample_data.xlsx', engine='openpyxl', index_col=0, sheet_name=0)
print(df0)
print(df0.index)
print(df0.columns)
ax = df0.plot(
    grid=True,
    style=[':','--','-'],
    marker='o',
    fontsize=13,
    color='blue'
)
# ax.set_title('A Large Title', size= 20)
ax.set_xlabel(df0.index.name, size=15)
ax.set_ylabel(df0.columns.values[0], size=15)
plt.savefig("motor-w.png")


df1 = pd.read_excel('sample_data.xlsx', engine='openpyxl', index_col=0, sheet_name=1)
print(df1)
print(df1.index)
print(df1.columns)
ax = df1.plot(
    grid=True,
    style=[':','--','-'],
    marker='o',
    fontsize=13,
    color='green'
)
# ax.set_title('A Large Title', size= 20)
ax.set_xlabel(df1.index.name, size=15)
ax.set_ylabel(df1.columns.values[0], size=15)
plt.xticks([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
plt.savefig("motor-vel.png")


df2 = pd.read_excel('sample_data.xlsx', engine='openpyxl', sheet_name=2)
print(df2)
print(df2.index)
print(df2.columns)
ax = df2.plot.scatter(
    x='x[m]',
    y='y[m]',
    grid=True,
    marker='o',
    s=10,
    fontsize=13,
    color='blue',
    label="spline path"
)
# ax.set_title('A Large Title', size= 20)
ax.set_xlabel(df2.columns.values[0], size=15)
ax.set_ylabel(df2.columns.values[1], size=15)
plt.legend(loc="upper left")
plt.xticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
plt.savefig("spline-path.png")


df3 = pd.read_excel('sample_data.xlsx', engine='openpyxl', sheet_name=2)
print(df3)
print(df3.index)
print(df3.columns)
ax = df3.plot.scatter(
    x='x[m]',
    y='y[m]',
    grid=True,
    marker='o',
    s=10,
    fontsize=13,
    color='blue',
    label="target path"
)
df3.plot.scatter(x='x2[m]', y='y2[m]', ax=ax, marker='>', s=10, grid=True, color='green', label="path 1")
df3.plot.scatter(x='x3[m]', y='y3[m]', ax=ax, marker='x', s=10, grid=True, color='red', label="path 2")
# ax.set_title('A Large Title', size= 20)
ax.set_xlabel(df3.columns.values[0], size=15)
ax.set_ylabel(df3.columns.values[1], size=15)
plt.legend(loc="upper left")
plt.xticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
plt.savefig("path.png")


plt.show()
