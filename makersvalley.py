import random
import folium
from folium.plugins import HeatMap

# bounding box for Makers Valley
lat_min, lat_max =  -26.194798, -26.185376
lng_min, lng_max = 28.067899, 28.084559

def generate_random_data(num_points):
    data = []
    for _ in range(num_points):
        lat = random.uniform(lat_min, lat_max)
        lng = random.uniform(lng_min, lng_max)
        capacity = random.randint(0, 100)
        data.append((lat, lng, capacity))
    return data

random_data = generate_random_data(100)

# center
maker_map = folium.Map(location=[-26.190033, 28.077792], zoom_start=16)

# heatmap layer
HeatMap(random_data, name='Makers Valley', min_opacity=0.1, radius=50, blur=50, gradient={0: 'black', 0.5: 'yellow', 1: 'red'}).add_to(maker_map)

# markers with cap labels
for lat, lng, capacity in random_data:
    folium.Marker(
        location=[lat, lng],
        icon=folium.DivIcon(html=f"""<div style="font-family: Arial; color: black; font-size: 12px;">{capacity}</div>""")
    ).add_to(maker_map)

maker_map.save("makersvalley.html")
