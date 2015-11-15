import urllib2,json
from flask import Flask, render_template, redirect, url_for, request, Response
import flickr_api

flickr_key = "dca00d0c7782247d89a98c1ee617a0ee"
flickr_secret = "5b568623184f70ca"

secrets = {'api_key' : flickr_key, 'api_secret' : flickr_secret }

app = Flask(__name__)

def get_Photos(tag,num):
    flickr_api.set_keys(**secrets)
    photos = flickr_api.Photo.search(tags=tag, sort='date-posted-desc', per_page=num,extras='url_o')
    j = []
    for photo in photos:
        j.append(
            {
                'title': photo.title,
                'url': photo.getPhotoUrl(),
                'd_url': "https://farm" + str(photo.farm) + ".staticflickr.com/" + str(photo.server) + "/" + str(photo.id) + "_" + str(photo.secret) + ".jpg"
            }
        )
    return j

@app.route("/t",methods=['GET','POST'])
def t_home():
    if request.method == 'GET':
        return render_template("tags.html",search=False)
    else:
        tag = request.form['tag']
        j = get_Photos(tag,10)
        #return render_template("tags.html",j=j,search=True)
        return redirect("/t/%s" %tag)

@app.route("/t/<tag>")
def t(tag):
    search=True
        #responses = Response(json.dumps({'photos': j}), status=200, mimetype='application/json')
    
#works to get the info, now need to get direct url to pic and put that into a render_template return 
    #photos[]
    j = get_Photos(tag,10)
    return render_template("tags.html",j=j,search=True)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

