import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

# Example data
data = {
    'Module': ['Brainstorming', 'Create Course Materials', 'Edit & Review Videos', 'Final Review', 'Launch Course'],
    'Start Date': pd.to_datetime(['2024-03-01', '2024-03-21', '2024-05-14', '2024-05-31', '2024-06-06']),
    'End Date': pd.to_datetime(['2024-03-20', '2024-05-15', '2024-05-30', '2024-06-06', '2024-06-11'])
}
df = pd.DataFrame(data)

# Create plot
fig, ax = plt.subplots(figsize=(14, 7))
# Define custom colors
custom_colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']  # Custom vivid colors

# Reverse the DataFrame to plot from top to bottom
df_reversed = df.iloc[::-1].reset_index(drop=True)

for i, (index, row) in enumerate(df_reversed.iterrows()):
    start = mdates.date2num(row['Start Date'])
    end = mdates.date2num(row['End Date'])
    bar = ax.barh(i, end - start, left=start, height=0.4, color=custom_colors[i])

    # Add module name text above the bars
    middle = start + (end - start) / 2
    ax.text(middle, i + 0.2, row['Module'],  # Position text just above each bar
            ha='center', va='bottom', color='black', fontsize=10, fontweight='bold')

# Set the y-ticks to correspond to the reversed order
ax.set_yticks(range(len(df_reversed)))
ax.set_yticklabels(df_reversed['Module'])

# Hide the y-axis
ax.get_yaxis().set_visible(False)

# Format the date axis
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Make grid lines lighter and dotted
ax.grid(True, linestyle='--', linewidth=0.5, color='grey', which='both', axis='x')

# Remove top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Increase padding for the x-axis label and adjust title position
ax.xaxis.labelpad = 15
plt.title('Python Course Timeline', fontsize=16, pad=20)

plt.xlabel('Date')
plt.tight_layout()
plt.show()
