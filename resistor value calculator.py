#values of each color code 
band_1_2 = [0,1,2,3,4,5,6,7,8,9]
multiplier = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,0.1,0.01]
tolerance = [0,1,2,0.05,0.02,0.5,0.25,0.1,0.01,0,5,10]

print("1.Black 2.Brown 3.Red 4.Orange 5.Yellow 6.Green 7.Blue 8.Violet 9.Gery 10.White 11.Gold 12.Silver")
band1 = int (input("Enter the 1st Band color : "))
band2 = int (input("Enter the 2nd Band color : "))
band3 = int (input("Enter the 3rd Band color : "))
band4 = int (input("Enter the 4th Band color : "))

val1 = band_1_2[band1-1]
val2 = band_1_2[band2-1]
val3 =  multiplier[band3-1]
value = ((val1*10)+val2) * val3
toleranceValue = tolerance[band4-1]

if ( value < 1000000 and value >= 1000 ):
    curt_value = value/1000
    print (f"{curt_value}K Ohm +/- {toleranceValue}%")
elif ( value >= 1000000 and value < 1000000000 ):
    curt_value = value/1000000
    print (f"{curt_value}M Ohm +/- {toleranceValue}%")
elif ( value >= 1000000000 ):
    curt_value = value/1000000000
    print (f"{curt_value}G Ohm +/- {toleranceValue}%")
elif  (value < 1000 ):
    print (f"{value} Oh +/- {toleranceValue}%")
else:
    print (f"{value}Ohm +/- {toleranceValue}%")

