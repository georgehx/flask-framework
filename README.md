# Flask on Heroku

Here are the steps and things to note:

Step 1: requirements.txt
First you need to set correct versions of Python modules in requirements.txt.
The only reason you need to do it is to make sure the Heroku app you deployed will have same behavior as on your local machine. Therefore theoretically this is not necessary. However I noticed that I would get Unable to push, found Python/Conda app error when I do: git push heroku master
Now when we add the following to the requirements.txt, we are basically asking Heroku to make new downloads of these dependencies in the versions as specified in requirements.txt.
Now the way to add is put following into requirements.txt:
Flask==1.1.1
pandas==0.25.1
bokeh==1.3.4
gunicorn==20.0.4

This is because the above 4 packages were used in our app.py python file. If more modules were used then it's best to be included as well.

The following command will print all the module's current version in your current local environment into a requirements.txt.
pip freeze > requirements.txt

To check individual module versions, do:
pip freeze | grep gunicorn
pip freeze | grep bokeh
pip freeze | grep pandas
pip freeze | grep Flask

After this step, your requirements.txt should be ok. This txt file is the problem of most of the issues so make sure you set it right.

Similar to this, set runtime.txt to your local environment's python version:
python --version
I have python 3.7.4 locally so set my runtime.txt to it instead of old value 3.6.5



Step 2: app.py

This is the main python file. The following basically says from your server app's address (e.g wind2.heroku.com), if it ends with '/' as 'https://wind2.herokuapp.com/', then it renders the 'index.html'

@app.route('/')
def index():
    return render_template('index.html')

If there is a '/plot' as 'https://wind2.herokuapp.com/plot', then it renders another html. The function name could be an action item. Action item is set in the html file. For example, methods = 'GET' or 'POST' is used to receive actions from a Form, or some other button. 'POST' is for receive. get_stock function has code to use Quandl API and request .csv format and parse into dataframe. People usually use JSON format over csv. I spent most hours on figuring out how to do Bokeh plotting. Basically you need to set up a fig as figure, then plot then set script, div = components(fig), to pass these into html. Html file will have places to receive scripts/div.

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    ticker = request.form['name_ticker']
    df = get_stock(ticker)

Step 3: HTML

Below e.g is for how to set up form button called 'Submit', note method is 'post', and action is 'plot'.
For home.html it's the plot page and its html is very simple.

<form id='userinfoform_lulu' method='post' action='plot' >
<p>
Name: <input type='text' name='name_ticker' />
</p>
<p>
<input type='submit' value='Submit' />
</p>
</form>

Step 4: Deploy
Can follow below guide. If cannot find app then use this:


So:
heroku create wind2
https://git.heroku.com/wind2.git (get wind2's git location)






This project is intended to help you tie together some important concepts and
technologies from the 12-day course, including Git, Flask, JSON, Pandas,
Requests, Heroku, and Bokeh for visualization.

The repository contains a basic template for a Flask configuration that will
work on Heroku.

A [finished example](https://lemurian.herokuapp.com) that demonstrates some basic functionality.

## Step 1: Setup and deploy
- Git clone the existing template repository.
- `Procfile`, `requirements.txt`, `conda-requirements.txt`, and `runtime.txt`
  contain some default settings.
- There is some boilerplate HTML in `templates/`
- Create Heroku application with `heroku create <app_name>` or leave blank to
  auto-generate a name.
- (Suggested) Use the [conda buildpack](https://github.com/thedataincubator/conda-buildpack).
  If you choose not to, put all requirements into `requirements.txt`

  `heroku config:add BUILDPACK_URL=https://github.com/thedataincubator/conda-buildpack.git#py3`

  The advantages of conda include easier virtual environment management and fast package installation from binaries (as compared to the compilation that pip-installed packages sometimes require).
  One disadvantage is that binaries take up a lot of memory, and the slug pushed to Heroku is limited to 300 MB. Another note is that the conda buildpack is being deprecated in favor of a Docker solution (see [docker branch](https://github.com/thedataincubator/flask-framework/tree/docker) of this repo for an example).
- Deploy to Heroku: `git push heroku master`
- You should be able to see your site at `https://<app_name>.herokuapp.com`
- A useful reference is the Heroku [quickstart guide](https://devcenter.heroku.com/articles/getting-started-with-python-o).

## Step 2: Get data from API and put it in pandas
- Use the `requests` library to grab some data from a public API. This will
  often be in JSON format, in which case `simplejson` will be useful.
- Build in some interactivity by having the user submit a form which determines which data is requested.
- Create a `pandas` dataframe with the data.

## Step 3: Use Bokeh to plot pandas data
- Create a Bokeh plot from the dataframe.
- Consult the Bokeh [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
  and [examples](https://github.com/bokeh/bokeh/tree/master/examples/embed).
- Make the plot visible on your website through embedded HTML or other methods - this is where Flask comes in to manage the interactivity and display the desired content.
- Some good references for Flask: [This article](https://realpython.com/blog/python/python-web-applications-with-flask-part-i/), especially the links in "Starting off", and [this tutorial](https://github.com/bev-a-tron/MyFlaskTutorial).
