import folium
import pandas as pd 

m = folium.Map(location=[20,0], title='OpenStreetMap',zoom_start=2)
data = pd.DataFrame({
    'lon':[83,80,72.82,83.2],
    'lat':[18.2,16,18.9,17.6],
    'labels' :['srikakulam','vijayawada','mumbai','vizag'],
},dtype=str)

for i in range(0,len(data)):
    folium.Marker(
        location=[data.iloc[i]['lat'],data.iloc[i]['lon']],
        popup = data.iloc[i]['labels']
    ).add_to(m)

m.save('abc.html')
