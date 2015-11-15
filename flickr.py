import urllib2, json
fKey = '20dd8b0f53a96c73c31c2f9ec7a22c9f'
gKey ="AIzaSyDbrIKnZ-fJcUxd636duQL8khuiekjC5pQ"

def getLatLng(address):
    uri = "https://maps.googleapis.com/maps/api/geocode/json?key=%(key)s&address=%(address)s"
    url = uri%({ "key":gKey, "address":address.replace(' ', '%20') })
    request = urllib2.urlopen(url)
    result = json.loads(request.read())
    return result['results'][0]['geometry']['location']


def searchPhotos(number, tag, latlng, radius):
# Takes the number of photos, the Flickr api key, the tag and a location, then returns a list of dictionaries with the format 'title':title, 'photo_id':photo_id,
    method = 'flickr.photos.search'
    uri = 'https://api.flickr.com/services/rest/?format=json&nojsoncallback=1&has_geo=1&method=%s&per_page=%s&api_key=%s&tags=%s&lat=%s&lon=%s&radius=%s&min_taken_date=%s'
    url = uri%(method, number, fKey, tag, latlng['lat'], latlng['lng'], radius, 1388534400)
    print url
    request = urllib2.urlopen(url)
    result = request.read()
    translated = json.loads(result)
    out = []
    for key in translated['photos']['photo']:
        a = {}
        a['user'] = key['owner']
        a['photo_id'] = key['id']
        a['title'] = key['title']
        a['farm'] = key['farm']
        a['server'] = key['server']
        a['secret'] = key['secret']
        out.append(a)
    return out

def getPhotoUrl(farm, server, id, secret):
    uri = "https://farm%(farm)s.staticflickr.com/%(server)s/%(id)s_%(secret)s.jpg"
    url = uri%({ "farm":farm, "server":server, "id":id, "secret": secret })
    return url

def findLocation(a):
# Takes the list from function above and returns list of dictionaries with format 'title':title, 'longitude':longitude, 'latitude':latitude
    method = 'flickr.photos.geo.getLocation'
    uri = 'https://api.flickr.com/services/rest/?format=json&nojsoncallback=1&method=%s&api_key=%s&photo_id=%s'
    out = []
    for photo in a:
        photo_id = photo['photo_id']
        url = uri%(method, fKey, photo_id)
        request = urllib2.urlopen(url)
        result = request.read()
        translated = json.loads(result)
        d = {}
        d['lng'] = translated['photo']['location']['longitude']
        d['lat'] = translated['photo']['location']['latitude']
        d['title'] = photo['title']
        d['id'] = photo['photo_id']
        d['url'] = getPhotoUrl(photo['farm'], photo['server'], photo['photo_id'], photo['secret'])
        out.append(d)
    return out
