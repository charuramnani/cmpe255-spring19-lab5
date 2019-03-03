

from collections import Counter
from linear_algebra import distance
from statistics import mean
import math, random
import matplotlib.pyplot as plt



def plot_state_borders(plt, color='0.8'):
    pass



def plot_cities(cities):

    # key is language, value is pair (longitudes, latitudes)
    plots = { "Java" : ([], []), "Python" : ([], []), "R" : ([], []) }

    # we want each language to have a different marker and color
    markers = { "Java" : "o", "Python" : "s", "R" : "^" }
    colors  = { "Java" : "r", "Python" : "b", "R" : "g" }
    from data import cities
    for (longitude, latitude), language in cities:
        
        plots[language][0].append(longitude)
        plots[language][1].append(latitude)

    # create a scatter series for each language
    for language, (x, y) in plots.items():
        plt.scatter(x, y, color=colors[language], marker=markers[language],
                          label=language, zorder=10)
    from state_border import plot_state_borders
    plot_state_borders(plt)    # assume we have a function that does this

    plt.legend(loc=0)          # let matplotlib choose the location
    plt.axis([-130,-60,20,55]) # set the axes
    plt.title("Favorite Programming Languages")
    plt.show()


def classify_and_plot_grid(cities, k=1):
    """
    TODO
    Classify and plot for Python, Java, and R languages.
    """
    plots = { "Java" : ([], []), "Python" : ([], []), "R" : ([], []) }
    markers = { "Java" : "o", "Python" : "s", "R" : "^" }
    colors  = { "Java" : "r", "Python" : "b", "R" : "g" }
    
    
    for longitude in range(-130, -60):
        for latitude in range(20, 55):
            from data import cities                    #importing data.py
            from Nearest_Neighbour import knn_classify      #importing knn_classify
            predicted_language = knn_classify(k, cities, [longitude, latitude])
            plots[predicted_language][0].append(longitude)
            plots[predicted_language][1].append(latitude)

    # create a scatter series for each language
    for language, (x, y) in plots.items():
        plt.scatter(x, y, color=colors[language], marker=markers[language],
                          label=language, zorder=0)
    from state_border import plot_state_borders
    plot_state_borders(plt, color='black')    # assume we have a function that does this

    plt.legend(loc=0)          # let matplotlib choose the location
    plt.axis([-130,-60,20,55]) # set the axes
    plt.title(str(k) + "-Nearest Neighbor Programming Languages")
    plt.show()



if __name__ == "__main__":
    from data import cities
    cities = []
    plot_cities(cities)
    classify_and_plot_grid(cities)
    classify_and_plot_grid(cities, 3)
    classify_and_plot_grid(cities, 5)



