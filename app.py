import urllib2,json
from flask import Flask, render_template, Response
import flickr_api

flickr_key = "dca00d0c7782247d89a98c1ee617a0ee"
flickr_secret = "5b568623184f70ca"

secrets = {'api_key' : flickr_key, 'api_secret' : flickr_secret }

app = Flask(__name__)

@app.route("/t")
@app.route("/t/<tag>")
def t(tag):
    flickr_api.set_keys(**secrets)
    photos = flickr_api.Photo.search(tags=tag, sort='date-posted-desc', per_page=10)
    j = []
    for photo in photos:
        j.append(
            {
                'title': photo.title,
                'description': photo.title,
                'url': photo.getPhotoUrl()
            }
        )
    response = Response(json.dumps({'photos': j}), status=200, mimetype='application/json')
    
#works to get the info, now need to get direct url to pic and put that into a render_template return 
    #photos[]

    #for r in response:
     #   try:    
      #      newPhoto = r[]

    return response


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

