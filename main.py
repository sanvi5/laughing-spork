from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_movies=movies_data[['orignal_title','poster_link','release_date','runtime','weighted_rating']]
liked_movies=[]
not_liked_movies=[]
did_not_watch=[]

# variables to store data
def assign_val():
  m_data={
    "original_title":all_movies.iloc[0,0],
    'poster_link':all_movies.iloc[0,1],
    "release_date":all_movies.iloc[0,2] or "N/A",
    "duration":all_movies.iloc[0,3],
    "rating":all_movies.iloc[0,4]/2
  }
  return m_data

# method to fetch data from database


# /movies api
@app.route("/movies")
def get_movie():
  movie_data=assign_val()
  return jsonify({
    "data":movie_data,
    "status":"success"
  })

# /like api
@app.route("/like",methods=["POST"])
def liked_movies():
  global all_movies
  movies_data=assign_val()
  liked_movie.append(movies_data)
  all_movies.drop([0],inplace=True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify({
    "status":"success"
  })


# /dislike api
@app.route("/dislike",methods=["POST"])
def unliked_movies():
  global all_movies
  movies_data=assign_val()
  not_liked_movies.append(movies_data)
  all_movies.drop([0],inplace=True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify({
    "status":"success"
  })


# /did_not_watch api
@app.route("/did_not_watch",methods=["POST"])
def did_not_watch_view():
  global all_movies
  movies_data=assign_val()
  did_not_watch.append(movies_data)
  all_movies.drop([0],inplace=True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify({
    "status":"success"
  })

if __name__ == "__main__":
  app.run()