import simplejson
import urllib
import urllib.parse
import urllib.request

ELEVATION_BASE_URL = 'https://maps.googleapis.com/maps/api/elevation/json'
key=""#Replace this with a key obtained from Google's API website (https://developers.google.com/maps/documentation/elevation/start)

def getElevation(loc, **elvtn_args):#Gets the elevation of a set of points
    elvtn_args.update({
    'locations':loc,
    'key':key
    })

    url = ELEVATION_BASE_URL + '?' + urllib.parse.urlencode(elvtn_args)
    response = simplejson.load(urllib.request.urlopen(url))

    elevationArray = []
    for resultset in response['results']:
        elevationArray.append(resultset['elevation'])
    return elevationArray

def getCircle(lat):#Gets the elevation of 360 point along a circle of latitude
    loc=str(lat)+",-179"
    for lon in range(-178,181):
        loc+="|"+str(lat)+","+str(lon)
    return getElevation(loc)

elevMap=[]
if key=="":
    print("You need to get a (free) key to use the Google Maps Elevation API")
else:
    for lat in range(-89,90):
        print(lat)
        elevMap.append(getCircle(lat))