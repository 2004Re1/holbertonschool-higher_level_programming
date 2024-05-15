# Print numbers from 0 to 98 in decimal and hexadecimal without storing in variables
for i in range(99):
    print("{} = {}".format(i, hex(i)), end='\n')

