import urllib2,json
from flask import Flask, render_template, redirect, url_for, request, Response
import flickr

app = Flask(__name__)

@app.route("/t",methods=['GET','POST'])
def t_home():
    if request.method == 'GET':
        return render_template("tags.html",search=False)
    else:
        tag = request.form['tag']
        j = flickr.get_Photos(tag,10)
        #return render_template("tags.html",j=j,search=True)
        return redirect("/t/%s" %tag)

@app.route("/t/<tag>")
def t(tag):
    search=True
        #responses = Response(json.dumps({'photos': j}), status=200, mimetype='application/json')
    
#works to get the info, now need to get direct url to pic and put that into a render_template return 
    #photos[]
    j = flickr.get_Photos(tag,10)
    return render_template("tags.html",j=j,search=True)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

