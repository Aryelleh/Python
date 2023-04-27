LegoSet = 'R2-D2'
InflationRate = 1.5

message = 'I really wanted to buy us a %s set for %d EUR but the price went up by %2.1f percent' %( LegoSet , 300 , InflationRate )
print(message)

message2 = 'I looked at the prices for the {0:s} lego set, and it will costs us {1:d} EUR plus an additional amount of {2:2.1f} percent VAT' .format('R2-D2' , 300 , 2.5)
print(message2)