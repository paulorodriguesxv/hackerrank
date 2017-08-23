#tripMaxWeight: 'int' representing the max weight per trip
#packagesWeight: array of 'int' representing the weight of each package
def minimumNumberOfTrips(tripMaxWeight, packagesWeight):
    val = 0

    trips_count = 0
    
    for i in range(0, len(packagesWeight)):
        trip_weight = 0
        trip_index = i

        if packagesWeight[trip_index] < 1: continue

        for j in range(i, len(packagesWeight)):
            w = packagesWeight[i] + packagesWeight[j]
            
            if packagesWeight[j] < 1: continue
            
            if w >= tripMaxWeight: continue

            if w > trip_weight: 
                trip_weight = w
                trip_index = j
        
        if trip_weight == 0:
            trip_weight = packagesWeight[i]
        
        packagesWeight[trip_index] = -packagesWeight[trip_index] 
        trips_count += 1
    #add your code here
    val = trips_count
    return val


print(minimumNumberOfTrips(100, [10, 20, 70]))
print(minimumNumberOfTrips(95, [10, 20, 70, 90, 45, 50 ]))
print(minimumNumberOfTrips(100, [10, 20, 70, 90, 45, 50 ]))