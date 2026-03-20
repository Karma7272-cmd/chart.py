import matplotlib.pyplot as plt

def generate_chart():
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 25, 30]
    plt.plot(x, y, marker='o')
    plt.title('Sample Data Chart')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.savefig('chart.png')
    print('Chart successfully saved as chart.png')

if __name__ == '__main__':
    generate_chart()
