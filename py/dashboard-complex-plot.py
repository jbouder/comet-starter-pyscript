import matplotlib.pyplot as plt
import numpy as np
from pyscript import display

# Generate some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x / 3)

# Create the figure and axes
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create secondary y-axis
ax2 = ax1.twinx()

# Line plot on primary y-axis
ax1.plot(x, y1, label="Sin(x)", color="b", linestyle="-", linewidth=2)
ax1.plot(x, y2, label="Cos(x)", color="r", linestyle="--", linewidth=2)

# Scatter plot on primary y-axis
ax1.scatter(x, y3, label="Tan(x)", color="g", marker="o", alpha=0.6)

# Bar plot on secondary y-axis
ax2.bar(x, y4, label="Exp(x/3)", color="purple", alpha=0.3, width=0.2)

# Add a legend to both axes
ax1.legend(loc="upper left", fontsize=12)
ax2.legend(loc="upper right", fontsize=12)

# Add grid
ax1.grid(True, which="both", linestyle="--", linewidth=0.5)

# Add annotations
for i in range(0, 100, 20):
    ax1.annotate(
        f"{y1[i]:.2f}",
        xy=(x[i], y1[i]),
        xytext=(x[i], y1[i] + 0.3),
        arrowprops=dict(facecolor="black", shrink=0.05),
    )
    ax1.annotate(
        f"{y2[i]:.2f}",
        xy=(x[i], y2[i]),
        xytext=(x[i], y2[i] - 0.3),
        arrowprops=dict(facecolor="black", shrink=0.05),
    )
    ax1.annotate(
        f"{y3[i]:.2f}",
        xy=(x[i], y3[i]),
        xytext=(x[i] + 0.2, y3[i]),
        arrowprops=dict(facecolor="green", shrink=0.05),
    )
    ax2.annotate(
        f"{y4[i]:.2f}",
        xy=(x[i], y4[i]),
        xytext=(x[i] - 0.5, y4[i] + 1),
        arrowprops=dict(facecolor="purple", shrink=0.05),
    )

# Add titles and labels
ax1.set_title("Advanced Complex Plot with Multiple Subplots and Y-axes", fontsize=16)
ax1.set_xlabel("X-axis", fontsize=14)
ax1.set_ylabel("Primary Y-axis", fontsize=14)
ax2.set_ylabel("Secondary Y-axis", fontsize=14)

# Set the limits of the axes
ax1.set_xlim([0, 10])
ax1.set_ylim([-2, 2])
ax2.set_ylim([0, 1000])

# Show the plot
plt.tight_layout()
plt.show()
display(fig, target="dashboard-complex-plot")
