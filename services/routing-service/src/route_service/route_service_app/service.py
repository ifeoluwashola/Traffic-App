import operator
from functools import reduce
import openrouteservice
from folium import Map, PolyLine
import os

def get_route(start, end):
    # Create a client instance
    client = openrouteservice.Client(key=os.environ.get('TRAFFIC_APP_API'))

    # Get coordinates for the start and end points
    start_coords = client.pelias_search(start)['features'][0]['geometry']['coordinates']
    end_coords = client.pelias_search(end)['features'][0]['geometry']['coordinates']

    # Get the route
    route = client.directions(coordinates=[start_coords, end_coords], profile='foot-walking', format='geojson')

    # Create a map centered at the start of the route
    m = Map(location=list(reversed(start_coords)), tiles="cartodbpositron", zoom_start=13)

    # Draw the route on the map
    waypoints = list(dict.fromkeys(reduce(operator.concat, list(map(lambda step: step['way_points'], route['features'][0]['properties']['segments'][0]['steps'])))))
    PolyLine([list(reversed(coord)) for coord in route['features'][0]['geometry']['coordinates']], color="blue").add_to(m)
    PolyLine([list(reversed(route['features'][0]['geometry']['coordinates'][index])) for index in waypoints], color="red").add_to(m)

    # Return the HTML representation of the map
    return m._repr_html_()
