from flask import Flask, jsonify, request
import csv

all_movies = []
liked_movies = []
disliked_movies = []
not_watched_movies = []

with open('movies.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

app = Flask(__name__)

@app.route("/allMovies")

def allMovies():
    return jsonify({
        "data" : all_movies[0],
        "status" : "All Movies"
    }),405

@app.route("/likedMovies", methods = ["POST"])

def likedMovies():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
      "message" : "Liked movies"
    }),406

@app.route("/dislikedMovies", methods = ["POST"])

def dislikedMovies():
    global all_movies
    movie2 = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(movie2)
    return jsonify({
        "Message" : "Disliked movies"
    }),407

@app.route("/didNotWatch", methods = ["POST"])

def didNotWatch():
    global all_movies
    movie3 = all_movies[0]
    all_movies = all_movies[1:]
    didNotWatch.append(movie3)
    return jsonify({
        "message" : "Did Not Watch"
    }),408
if __name__ == "__main__":
    app.run()