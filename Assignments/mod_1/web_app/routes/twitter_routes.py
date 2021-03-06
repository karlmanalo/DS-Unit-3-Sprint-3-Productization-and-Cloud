from flask import Blueprint, jsonify, request, render_template

twitter_routes = Blueprint('twitter_routes',__name__)

@twitter_routes.route('/twitter.json')
def twitter():
    tweets = [
        {"id":1,"user":'@user',"tweets":'i like apples'},
        {"id":2,"user":'@user2',"tweets":'i like green apples'},
        {"id":3,"user":'@user3',"tweets":'i like oranges'},
        {"id":4,"user":'@user4',"tweets":'i like pineapples'}
    ]
    return jsonify(tweets)


@twitter_routes.route('/twitter')    
def twitter_for_humans():
    tweets = [
        {"id":1,"user":'@user',"tweets":'i like apples'},
        {"id":2,"user":'@user2',"tweets":'i like green apples'},
        {"id":3,"user":'@user3',"tweets":'i like oranges'},
        {"id":4,"user":'@user4',"tweets":'i like pineapples'}
    ]
    return render_template('twitter.html',message='Here are some Tweets',tweets=tweets)

@twitter_routes.route('/twitter/new')
def new_tweet():
    print("FORM DATA:",dict(request.form))
    return jsonify({
        "message": "TWEET CREATED OK",
        "tweet": dict(request.form)
    })