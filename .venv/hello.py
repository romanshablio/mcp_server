from flask import Flask, request, jsonify, render_template
from markupsafe import escape
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
app = Flask(__name__)

def search_query(query):
    search_url = f"https://www.google.com/search?q={query}"
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        results = []
        for result in soup.select('.tF2Cxc'):
            title = result.select_one('.DKV0Md').text
            description = result.select_one('.VwiC3b').text
            results.append({'title': title, 'description': description})
        return results
    else:
        return []



@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/')
def hello_world():
  return 'Hello, World!'

# @app.route('/about')
# def about():
#   return 'This is the about page'

# @app.route('/user/<username>')
# def show_user_profile(username):
#   return f'User {username}'

@app.route('/search/', methods=['GET'])
@app.route('/search/<name>')
def index():
   return render_template('index.html', __name__=__name__)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']  # Получаем запрос из формы
    results = search_query(query)  # Выполняем поисковый запрос
    return render_template('index.html', results=results)



# @app.route('/search', methods=['GET'])
# def search():
#     query = request.args.get('query')  # Получаем запрос из параметра URL
#     results = search_query(query)
#     return 'Hello, World!', jsonify(results)  # Возвращаем результат в формате JSON

# if __name__ == "__main__":
#     app.run(debug=True)