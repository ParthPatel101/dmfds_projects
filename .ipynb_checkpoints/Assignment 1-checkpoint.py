# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO CANVAS

from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    # WRITE YOUR CODE BELOW
    lines = open(f)
    ratingsDict = {}
    for line in lines:
        x = line.split("|")
        if x[0] in ratingsDict.keys():
            ratingsDict[x[0]].append(float(x[1]))
        else:
            ratingsDict[x[0]] = [float(x[1])]
    return ratingsDict
    
    

# 1.2
def read_movie_genre(f):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    # WRITE YOUR CODE BELOW
    lines = open(f)
    movieGenreDict = {}
    for line in lines:
        x = line.strip().split("|")
        movieGenreDict[x[2]] = x[0]
    return movieGenreDict

# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    # WRITE YOUR CODE BELOW
    genreDict = {}
    for v in d.keys():
        if d[v] in genreDict:
            genreDict[d[v]].append(v)
        else:
            genreDict[d[v]] = [v]
    return genreDict
    
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    averageDict = {}
    for i in d.keys():
        averageDict[i] = sum(d[i])/len(d[i])
    return averageDict
    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    return dict(sorted(d.items(), key = lambda val: val[1], reverse = True)[:n])
    
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    return dict([(k,v) for k,v in d.items() if v >= thres_rating])
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    lst = genre_to_movies[genre]
    list = []
    for i in lst:
        list.append((i, movie_to_average_rating[i]))
    return dict(sorted(list, key = lambda val: val[1], reverse = True)[:n])
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    lst = genre_to_movies[genre]
    list = []
    for i in lst:
        list.append(movie_to_average_rating[i])
    return (sum(list)/len(list))
    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    genrePopularityDict = {}
    for i in genre_to_movies.keys(): 
        genrePopularityDict[i] = get_genre_rating(i, genre_to_movies, movie_to_average_rating)
    genrePopularityDict = dict(sorted(genrePopularityDict.items(), key = lambda val: val[1], reverse = True)[:n])
    return genrePopularityDict

# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to movies and ratings
    # WRITE YOUR CODE BELOW
    lines = open(f)
    lst = []
    user_ratings = {}
    for line in lines:
        lst = line.rstrip().split("|")
        if lst[2] in user_ratings.keys():
            user_ratings[lst[2]].append((lst[0],lst[1]))
        else:
            user_ratings[lst[2]] = [(lst[0],lst[1])]
    return user_ratings
    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW
    lst = {}
    for i in user_to_movies[user_id]:
        if movie_to_genre[i[0]] in lst.keys():
            lst[movie_to_genre[i[0]]].append(float(i[1]))
        else:
            lst[movie_to_genre[i[0]]] = [float(i[1])]
    for i,k in lst.items():
        lst[i] = (sum(k)/len(k))
    return max(lst, key = lst.get)
    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    reccomendations = {}
    userGenre = get_user_genre(user_id, user_to_movies, movie_to_genre) #favorite genre
    for i,k in movie_to_genre.items():
        if k == userGenre:
            reccomendations[i] = movie_to_average_rating[i]
    
    for (x,y) in user_to_movies[user_id]:
        if x in reccomendations.keys():
            del reccomendations[x]
    reccomendations = dict(sorted(reccomendations.items(), key = lambda val: val[1], reverse = True)[:3])
    return reccomendations

# -------- main function for your testing -----
def main():
    # write all your test code here
    # this function will be ignored by us when grading
    
    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions

    
# program will start at the following main() function call
# when you execute hw1.py
main()

    