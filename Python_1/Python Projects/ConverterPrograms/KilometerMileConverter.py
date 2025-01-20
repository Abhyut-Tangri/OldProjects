# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
ConversionFactor = 0.621371

# calculate miles
miles = kilometers * ConversionFactor
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
