import numpy as np

import matplotlib.pyplot as plt

temp_data={'CITY A':np.array([30,32,31,29,28,27,26]),
           'CITY B':np.array([35,34,36,33,32,31,31]),
           'CITY C':np.array([25,26,27,28,29,30,31]),
           'CITY D':np.array([22,23,24,25,26,27,28])}


avg_temp={city:np.mean(temps)for city,temps in temp_data.items()}
print("AVERAGE TEMPERATURE:")
for city, avg_tempp in avg_temp.items():print(f"{city}:{avg_tempp}C")

for city,temps in temp_data.items():
    maxtemp=np.max(temps)
    mintemp=np.min(temps)
    print(f"{city}:MAX_TEMP={maxtemp}*c,MIN_TEMP={mintemp}*c")

def avg_temps(data):
    temp_array=np.array(list(data.values()))
    avgtemppd=np.mean(temp_array,axis=0)

    return avg_temps

    average_temp=avg_temps(temp_data)
    print("\n average temp per day of week:")
    for i,temp in enumerate(average_temp,1):print(f"DAY{i}:{temp}*c")

plt.figure(figsize=(10,6))
for city,temps in temp_data.items():plt.plot(temps,label=city)

plt.xlabel('day of the week')
plt.ylabel('temperature(*c)')
plt.legend()
plt.grid(True)
plt.show()
