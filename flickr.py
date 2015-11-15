import flickr_api

#Secrets
flickr_key = "dca00d0c7782247d89a98c1ee617a0ee"
flickr_secret = "5b568623184f70ca"

#puts key & secret into dict for easy use
secrets = {'api_key' : flickr_key, 'api_secret' : flickr_secret }

#gets num photos with specific tag
#uses flickr_api's built in functions 
def get_Photos(tag,num):
    flickr_api.set_keys(**secrets)
    photos = flickr_api.Photo.search(tags=tag, sort='date-posted-desc', per_page=num,extras='url_o')
    j = []
    for photo in photos:
        j.append(
            {
                'title': photo.title,
                'url': "https://www.flickr.com/photos/" + str(photo.owner.id) + "/" + str(photo.id),
                'd_url': "https://farm" + str(photo.farm) + ".staticflickr.com/" + str(photo.server) + "/" + str(photo.id) + "_" + str(photo.secret) + ".jpg"
            }
        )
    return j
