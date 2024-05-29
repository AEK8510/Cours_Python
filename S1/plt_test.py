import matplotlib.pyplot as plt
import numpy as np
import sys

My_choice = int(sys.argv[1])

if My_choice == 1:
    x = np.linspace(-5, 5, 20)
    plt.plot(x, np.sin(x))  # Using the sinus function from Numpy
    plt.ylabel('Sine Function')
    plt.xlabel('X-axis')
    plt.savefig("mygraph.png")
    plt.show()

if My_choice == 2:
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [1, 2, 3, 4, 5, 6, 7]
    # Creating a scatter plot
    plt.scatter(x, y, marker="o", color="blue")
    # Adding labels and title
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear function")
    # Displaying the plot
    plt.show()

if My_choice == 3:
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    fruits = ['apple', 'blueberry', 'cherry', 'orange']
    counts = [40, 100, 30, 55]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title='Fruit color')

    plt.show()
