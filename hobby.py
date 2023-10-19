
import pandas as pd
import numpy as np

def Charles():
	schedule = [0, 1]
	hours = [7, 12]
	sleephour = [29, 17]
	str_sleeptime = ["5:00 a.m.", "7 a.m."]
	str_waketime = ["2 p.m.", "7 p.m."]
	str_hoursawakebefore = ["Twenty-nine", "Seventeen"]
	
	sleep = pd.DataFrame({"Schedule in Trial": schedule, "Hours Sleep": hours, "Bedtime in hours since waking": sleephour, "Bedtime in day houe": str_sleeptime, "Wake time in day hour": str_waketime, "Hours awake before sleeping": str_hoursawakebefore})
	print(sleep)
	sleep.to_csv('CharlesTruscottSleep.csv')
	
if __name__ == """__main__""": Charles()
	