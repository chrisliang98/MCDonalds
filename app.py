import urllib2,json
from flask import Flask, render_template, redirect, url_for, request, Response
import flickr

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
@app.route("/home/", methods=['GET','POST'])
@app.route("/t",methods=['GET','POST'])
@app.route("/t/",methods=['GET','POST'])
def t_home():
    if request.method == 'GET':
        return render_template("tags.html",search=False)
    else:
        tag = request.form['tag']
        num = request.form['num']
        sort = request.form['sort']
        j = flickr.get_Photos(tag,num,sort)
        #return render_template("tags.html",j=j,search=True)
        return redirect("/t/%s/%s/%s" %(tag,num,sort))

@app.route("/t/<tag>/<num>/<sort>")
@app.route("/t/<tag>/<num>/<sort>/")
def t(tag,num,sort):
    search=True
    j = flickr.get_Photos(tag,num,sort)
    return render_template("tags.html",j=j,search=True)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

