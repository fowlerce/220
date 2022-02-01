def traffic():
    total_cars = 0
    road_counter = 1
    roads = eval(input("How many roads were surveyed?"))
    for i in range(roads):
        daily_cars = 0
        day_counter = 1
        print("Road", road_counter)
        days = eval(input("How many days was the road surveyed?"))
        for j in range(days):
            print("Road", road_counter, "Day", day_counter)
            cars = eval(input("How many cars traveled this day?"))
            total_cars = total_cars + cars
            daily_cars = daily_cars + cars
            day_counter = day_counter + 1
        print("Road", road_counter, "average vehicles per day:", round(daily_cars / days, 1))
        road_counter = road_counter + 1
    print("Total number of vehicles on all roads:", total_cars)
    print("Average number of vehicles per road:", round(total_cars / roads, 2))
