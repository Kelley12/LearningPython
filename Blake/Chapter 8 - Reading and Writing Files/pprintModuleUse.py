#! python3
# Saving variables with the shelve modules examples from Chapter 8

import pprintModule

print('Brand\tColor')
for bike in pprintModule.motorbikes:
    print(bike['name'] + '\t' + bike['color'])
