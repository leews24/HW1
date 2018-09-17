## HW 1
## SI 364 F18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".

### Used Python and PokeAPI documentation
### Referred back to Lecture2 Example2 file


## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications.
# Edit the code so that once you run this application locally and
# go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask
import requests
import json
from flask import Flask, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def main_page():
    return '''
    <h1>SI364F18 HW1</h1>
    <h2>Won Seok (Warren) Lee</h2>
    <ul>
        <li><a href='http://localhost:5000/class'>Problem 1</a></li>
        <li><a href='http://localhost:5000/movie/Ratatouille'>Problem 2 - Ratatouille</a></li>
        <li><a href='http://localhost:5000/movie/Titanic'>Problem 2 - Titanic</a></li>
        <li><a href='http://localhost:5000/movie/dsagdsgskfsl'>Problem 2 - dsagdsgskfsl</a></li>
        <li><a href='http://localhost:5000/question'>Problem 3</a></li>
        <li><a href='http://localhost:5000/problem4form'>Problem 4</a></li>
    </ul>
    '''

@app.route('/class')
def hello_to_you():
    return 'Welcome to SI 364!'

@app.route('/movie/<title>')
def moviedata(title):
    base_url = "https://itunes.apple.com/search"
    # params_dict = {}
    params_dict = {"entity":"movie", "attribute":"featureFilmTerm"}
    params_dict["term"] = title
    resp = requests.get(base_url, params = params_dict)
    text = resp.text
    python_obj = json.loads(text)
    retlist = []
    return str(python_obj)

@app.route('/question')
def formQuestion():
    html_form = '''
    <html>
    <body>
        <form action="/result" method="GET">
            <label>enter your favorite number:</label><br>
            <input type="text" name="favnum" id="favnum"></input>
            <input type="submit" value="Submit"></input><br>
        </form>
    </body>
    </html>
    '''
    return html_form

@app.route('/result',methods=["GET"])
def resultQuestion():
    if request.method == "GET":
        print(request.args)
        favnum = request.args.get("favnum", "")
        return "Double your favorite number is " + str(int(favnum)*2) + "."
    else:
        return "error"

@app.route('/problem4form')
def formp4():
    htmltop = '''<html><body>'''
    htmlbot = '''</body></html>'''
    poke_form = '''
        <form action="" method="GET">
            <label>Enter a Pokemon:</label><br>
            <input type="text" name="favmon" id="favmon"></input>
            <input type="submit" value="Submit"></input><br>
        </form>
    '''
    footer = '''<p style="font-size:60%;">If you do not know the names of any pokemon, try typing in "Pikachu".</p>'''

    if request.method == "GET":
        if len(request.args) != 0:
            ### pulling data from PokeAPI (supports only GET)
            favmon = request.args.get('favmon','')
            print(request.args)
            url = "http://pokeapi.co/api/v2/pokemon/" + favmon.lower()
            resp = requests.get(url)
            favmondict = json.loads(resp.text)
            ### pulling needed data into python items
            typelist = []
            for i in favmondict['types']:
                typelist.append(i['type']['name'])
            imgtext = favmondict['sprites']['front_default']
            ### prepping output string into html format
            if len(typelist) == 1:
                typestr = '''
                    <p>{0} is a {1} type pokemon.</p>
                    <p>Here is a picture of {0}.</p>
                    <img src={3} alt="sprite" height = "100" width = "100">
                    <p>This is displayed using PokeAPI, which only supports the GET method.</p>
                '''.format(favmon.title(), typelist[0], 0, imgtext)
            elif len(typelist) == 2:
                typestr = '''
                    <p>{0} is a {1} and {2} type pokemon.</p>
                    <p>Here is a picture of {0}.</p>
                    <img src={3} alt="sprite" height = "100" width = "100">
                    <p>This is displayed using PokeAPI, which only supports the GET method.</p>
                '''.format(favmon.title(), typelist[0], typelist[1], imgtext)
            else:
                typestr = "missingno"
            return htmltop+poke_form+typestr+htmlbot
        else:
            return htmltop+poke_form+footer+htmlbot
    else:
        return htmltop+poke_form+footer+htmlbot


if __name__ == '__main__':
    app.run(debug=True)


## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL
# 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a
# big dictionary of data on the page. For example, if you go to the URL
# 'http://localhost:5000/movie/ratatouille', you should see something like the
# data shown in the included file sample_ratatouille_data.txt, which contains
# data about the animated movie Ratatouille.
#
# However, if you go to the url http://localhost:5000/movie/titanic,
# you should get different data, and if you go to the url
# 'http://localhost:5000/movie/dsagdsgskfsl' for example,
# you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application
# locally and got to the URL http://localhost:5000/question, you see a form that
# asks you to enter your favorite number.

## Once you enter a number and submit it to the form, you should then see
# a web page that says "Double your favorite number is <number>". For example,
# if you enter 2 into the form, you should then see a page that says
# "Double your favorite number is 4". Careful about types in your Python code!

## You can assume a user will always enter a number only.


## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen
# dynamically in the Flask application, and build it into the above code for a
# Flask application, following a few requirements.

## You should create a form that appears at the route
 # http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends
    # upon the data entered into the submission form and is readable by humans
    # (more readable than e.g. the data you got in Problem 2 of this HW).
    # The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps:
# if you think going slowly and carefully writing out steps
# for a simpler data transaction, like Problem 1, will help build your
# understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you
# expect in your form; you do not need to handle errors or user confusion.
# (e.g. if your form asks for a name, you can assume a user will type a
# reasonable name; if your form asks for a number, you can assume a user will
# type a reasonable number; if your form asks the user to select a checkbox,
# you can assume they will do that.)

# Points will be assigned for each specification in the problem.
