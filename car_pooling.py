def car_pooling(trips, capacity):
        passangers = [0]*1001
        for count, fr, to in trips:
            if count > capacity: return False  # optimization 1
            passangers[fr] += count
            passangers[to] -= count
        for i in range(1, len(passangers)):
            passangers[i] += passangers[i-1]
            if passangers[i] > capacity:
                return False
        return True
print(car_pooling([[2,1,5],[3,3,7]], 4))
print(car_pooling([[2,1,5],[3,3,7]], 5))
