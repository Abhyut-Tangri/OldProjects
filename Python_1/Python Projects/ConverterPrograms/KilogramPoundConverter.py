# Seeing how much kilograms person needs to covert
kilograms = float(input("Enter value in kilograms: "))

# Conversion Factor
ConversionFactor =  2.205

# Caclulating Pounds
Pounds = kilograms * ConversionFactor

print('%0.2f kilograms is equal to %0.2f pounds' %(kilograms,Pounds))
print('Thank you for using The KilogramPoundConverter!')
