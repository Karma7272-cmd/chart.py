import matplotlib.pyplot as plt
import math

def generate_chart():
    """
    Generates and saves a modern, colorful sample chart.
    """
    # Use a modern plot style
    plt.style.use('seaborn-v0_8-darkgrid')

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Generate more interesting sample data
    x = [i / 10.0 for i in range(0, 100)]
    y1 = [math.sin(val) for val in x]
    y2 = [math.cos(val) for val in x]

    # Plot data with vibrant colors and styles
    ax.plot(x, y1, label='Sine Wave', color='#FF5733', linewidth=2.5, marker='o', markersize=4)
    ax.plot(x, y2, label='Cosine Wave', color='#33CFFF', linewidth=2.5, linestyle='--', marker='x', markersize=4)

    # Add a title and labels with more descriptive names
    ax.set_title('Modern Sample Data Chart', fontsize=18, fontweight='bold')
    ax.set_xlabel('Time (s)', fontsize=12)
    ax.set_ylabel('Amplitude', fontsize=12)

    # Add a legend to distinguish the data series
    ax.legend(fontsize=10)

    # Customize grid and ticks for a cleaner look
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.tick_params(axis='both', which='major', labelsize=10)

    # Ensure everything fits without overlapping
    plt.tight_layout()
    plt.savefig('chart.png', dpi=300)
    
    print('Chart successfully saved as chart.png')

if __name__ == '__main__':
    generate_chart()