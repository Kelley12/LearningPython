# Generating random people's height and weight
import numpy

# Generate 5000 random heights
# random.normal(distribution mean, distribution std dev., number of samples)
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
#
np_city = np.column_stack((height, weight))
