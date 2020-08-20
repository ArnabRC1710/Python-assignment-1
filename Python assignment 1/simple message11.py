# list of transport
travel_mode_list = ["Hovercraft","Metro","Train","Bus","Car","Bicycle"]
# List of activity
activity_list =["I wish I owned a","The most comfortable way to ride is to ride",
                "For long distance journey I prefer","While going to office I usually take",
                "I would always prefer manual","An excelent way of excercise is to ride a" ]
#total number of activity
total_len = len(activity_list)
#print activity for each transport
for i in range(total_len):
        print(activity_list[i],travel_mode_list[i])
