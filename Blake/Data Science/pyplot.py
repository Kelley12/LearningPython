# Example program of using the pyplot library
# To install the matplotlib
#   python -m pip install -U pip setuptools
#   python -m pip install matplotlib
import matplotlib.pyplot as plt

year = [1950,1951,1952,1953,1954,1955,1956]
pop = [2.538,2.57,2.62,2.84,2.98,3.23,3.54]

# Create a plot of the data
plt.plot(year, pop)

# Add title and axis labels
plt.xlabel("Year")
plt.ylabel("Population [million]")
plt.title("Population over year")

plt.show()
plt.clf()

# Create a scatter plot of the data
plt.scatter(year, pop)
plt.show()
plt.clf()

# Create a scatter plot of the data
plt.hist(year, )
plt.show()
plt.clf()
