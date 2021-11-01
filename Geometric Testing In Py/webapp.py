from main import sphere,cuboid,cone,cylinder
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def mainMenu():
    if request.method == "POST":                    # if input is being poted to this method
        shape = request.form.get("shapebutton")     # There are multiple buttons in index with the id shapebutton that return different values
        print("Selection was: ",shape)
        # The different values of shapebutton are listed here
        if shape=="sphere":
            return redirect(url_for('sphereForm'))
        elif shape=="cylinder":
            return redirect(url_for('cylinderForm'))
        elif shape=="cone":
            return redirect(url_for("coneForm"))
        elif shape=="cubiod":
            return redirect(url_for("cuboidForm"))
    return render_template("index.html")            # if the signal is HTTP GET

@app.route("/sphere",methods= ["GET","POST"])
def sphereForm():
    if request.method == "POST":
        if request.form.get("home")=="true":
            return render_template("index.html")
        radius = request.form.get("rad")            # get the shape parameters from the page 
        vol = sphere.calcVolume(int(radius))        # calculate the volume
        sA = sphere.calcSurfArea(int(radius))       # calculate the surface area 
        return "User entered: Radius "+ str(radius) + ". <p>The Volume is: " + str(vol) + ", the Surface area is: " + str(sA)  # return a string that will somehow print the output in the place of the submit button
    return render_template("sphere.html")           # load the base sphere.html page

@app.route("/cylinder",methods= ["GET","POST"])
def cylinderForm():
    if request.method == "POST":
        if request.form.get("home")=="true":
            return render_template("index.html")
        radius = request.form.get("rad")
        height = request.form.get("height")
        vol = cylinder.calcVolume(int(radius),int(height))
        sA = cylinder.calcSurfArea(int(radius),int(height))
        latSA = cylinder.calcLatSurfArea(int(radius),int(height))
        endSA = cylinder.calcEndSurfArea(int(radius))
        return "User entered: Radius "+ str(radius) + ",User entered: Height "+ str(height) + ". <p>The Volume is: " + str(vol) + ", the Surface area is: " + str(sA) + ", the Lateral Surface area is: "+ str(latSA)+", the End Surface area is: "+ str(endSA)
    return render_template("cylinder.html")

@app.route("/cone",methods= ["GET","POST"])
def coneForm():
    if request.method == "POST":
        if request.form.get("home")=="true":
            return render_template("index.html")
        radius = request.form.get("rad")
        height = request.form.get("height")
        vol = cone.calcVolume(int(radius),int(height))
        sA = cone.calcSurfArea(int(radius),int(height))
        latSA = cone.calcLatteralSurfArea(int(radius),int(height))
        return "User entered: Radius "+ str(radius) + ", Height "+ str(height)  + ". <p>The Volume is: " + str(vol) + ", the Surface area is: " + str(sA)+ "the Lateral Surface area is: "+ str(latSA)
    return render_template("cone.html")
    
@app.route("/cuboid",methods= ["GET","POST"])
def cuboidForm():
    if request.method == "POST":
        if request.form.get("home")=="true":
            return render_template("index.html")
        s1 = request.form.get("len")
        s2 = request.form.get("wid")
        s3 = request.form.get("hei")
        vol = cuboid.calcVolume(int(s1),int(s2),int(s3))
        sA = cuboid.calcSurfArea(int(s1),int(s2),int(s3))
        return "User entered: s1 "+ str(s1) +", s2 "+ str(s2) + ", s3 " + str(s3) + ". <p>The Volume is: " + str(vol) + ", the Surface area is: " + str(sA)
    return render_template("cuboid.html")

if __name__=="__main__":
    app.run(host='0.0.0.0')
        
