from flask import Flask, render_template, request, url_for, redirect

from movie.repository.memoryrepository import MemoryRepository



def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    repository = MemoryRepository('movie/datafiles/Data1000Movies.csv')

    @app.route("/")
    def home():
        return render_template('home.html')

    @app.route("/movies")
    def movies():
        lst = repository.movie_lsts
        desc_lst = repository.desc_lst
        direct_lst = repository.director_lst

        for movie, desc, director in zip(lst, desc_lst, direct_lst):
            movie.description = desc
            movie.director = director

        page_amount = 10

        cursor = request.args.get('cursor')
        if cursor is None:
            cursor = 0
        else:
            cursor = int(cursor)

        first_page_url = None
        last_page_url = None
        next_page_url = None
        prev_page_url = None

        if cursor > 0:
            prev_page_url = url_for('movies', cursor=cursor - page_amount)
            first_page_url = url_for('movies')

        if cursor + page_amount < len(lst):
            next_page_url = url_for('movies', cursor=cursor + page_amount)

            last_cursor = page_amount * int((len(lst) / page_amount))
            if len(lst) % page_amount == 0:
                last_cursor -= page_amount
            last_page_url = url_for('movies', cursor=last_cursor)

        return render_template('movies.html', movie_lst=lst[cursor:cursor+10], desc_lst=desc_lst, first_page_url=first_page_url, last_page_url=last_page_url, next_page_url=next_page_url, prev_page_url=prev_page_url, direct_lst=direct_lst)

    @app.route("/login")
    def login():
        username = request.args.get('LoginUsername')
        password = request.args.get('LoginPassword')
        return render_template('login.html')

    return app

