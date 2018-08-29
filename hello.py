# print("Hello world")
# print("Meina love Ilkin")

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/about/<name>/<surname>")
def about(name, surname):
    return "Hello, %s %s welcome to our website ,here you can find me " % (name, surname)


@app.route("/blog/<int:article_id>")
def blog(article_id):
    return "Wow yesterday was a great day Article id is %d" % article_id


@app.route("/calcu/<int:a>/<int:b>")
def calculator(a, b):
    return " the sum of %d and %d = %d" % (a, b, a+b)

@app.route("/moviesdisplay")
def movie2():
    movie_list=[]
    read=open("movies.txt","r")
    for movie in read:
        b=movie.split(",")
        id=int(b[0])
        title=b[1]
        image=b[5]
        summary=b[3]
        m={"id":id,"title":title,"image":image,"summary":summary}
        movie_list.append(m)
    return render_template("movie3.html",movie_list=movie_list)

@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    title = ""
    rating = 0.0
    summary = ""
    view = 0
    view_result=""
    found = False
    # if movie_id == 1:
    #     title = "Toy story"
    # elif movie_id == 2:
    #     title = "Animal story"
    # elif movie_id == 3:
    #     title = "Human story"
    # else:
    #     title = "sorry moview not found"

    # open a file to read every line
    r = open("movies.txt", "r")

    # go though every line - inspect every line
    for line in r:
        # split line into a list by a comma
        a = line.split(",")
        # convert first element into an integer
        id = int(a[0])
        # compare against movie_id
        if id == movie_id:
            # we found our movie
            title = a[1]
            rating = float(a[2])
            summary = a[3]
            view = int(a[4])
            if view < 100:
                view_result = "not bad movie"
            elif 100 < view < 200:
                view_result = " good movie"
            elif view> 200:
                view_result = "hot movie"
            else:
                view_result = "super hot movie"
            image = a[5]
            video = a[6]
            found = True
            break

    if found:
        return render_template("movie.html", title=title, rating=rating, summary=summary, view=view,result=view_result,image=image,video=video,id=id,id1=id,found=found)
    else:
        return "Sorry the movie that you have requested does not exist"

if __name__ == "__main__":
    app.run()