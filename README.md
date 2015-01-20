# Corkboard
The special events app that's special.

#Installation for Development
Corkboard uses Django, an amazing Python web framework, and as such it needs a few Python utilities. As of this writing,
Corkboard is compatible with Python 2.7.x and Python 3.x

*Fie and double fie upon the one who does these out of order.*

**Install pip:**  
>`sudo easy_install pip`  

When it comes to Python package managers, pip is the only game in town. It wraps the ironically headache-inducing easy_install
and makes installing python packages a breeze. Be sure to run this command as root (either use sudo or login as root) to install
pip globally.  

**Install virtualenv:**  
>`sudo pip install virtualenv`  

Virtualenv allows you to install Python packages in walled-off virtual environments, which is great when you have multiple projects on one machine,
each of which may depend on a different version of the same package. Perfect for the developer who can't eat her peas if their touching
the carrots.

**Install autoenv:**  
>`sudo pip install autoenv`  
>`echo "source /usr/local/opt/autoenv/activate.sh" >> ~/.bash_profile`  
>`source ~/.bash_profile`   

Place a `.env` file in any directory, and this nifty little program will automatically execute all shell commands contained
therein whenever you `cd` into that directory. Great for activating virtualenvs and issuing threatening console messages.

**Clone this repo**

Unless you're planning on cloning this repo once and then never touching it again, you'll want to clone it via ssh. Make sure
your public key(s) is/are [uploaded to your github profile.](github.com/settings/ssh) If you have no idea what that means, go [here](https://help.github.com/articles/generating-ssh-keys/) 
and follow the instructions for generating an ssh key pair and uploading your public key. Once that's done, `cd` into the directory where you want to clone the project and:  
>`git clone git@github.com:wbrefvem/corkboard.git`  

**Create and activate virtualenv**

After cloning, run the following:
>`cd corkboard`  
>`virtualenv .venv`   

(You can specify a different version of python from your system default by adding `-p <path-to-python-binary>` to the above command.)   
>`source .venv/bin/activate`  
>`echo "source .venv/bin/activate" >> .env`  

You now have an active Python virtual environment. Anything you install through pip will reside here in this environment and may not be available outside
of it.   
  
**Note:** if you run pip as root while your virtualenv is active, your package(s) will be installed globally, *not in your virtualenv.* 
When working with virtualenvs, it's best to install everything under your own username.
  

**Install required packages**

>`pip install -r requirements.txt`

**Run database migrations**  

By default, Corkboard uses SQLite for development. Don't change this unless you really want to. Matter of fact, don't change it even if you really
want to. SQLite is awesome.   

In any case, you'll need to intialize your database schema by running the migrations. Make sure you're in the folder where `manage.py` is located
and run:  
>`python manage.py migrate`  

**Run development server**

You're going to want to use Django's development server for development. Don't use it for production unless you hate sleep
and happiness.  

>`python manage.py runserver 0.0.0.0:8008`  

You will have to choose a different port if something else is running on port `8008`. It's also worth noting that using `0.0.0.0` for the host string
will make your Corkboard installation visible to other machines on the network, assuming your firewall is configured to allow http traffic
on `8008` or whatever port you chose. Use `127.0.0.1` or `localhost` for the host string or configure your firewall to block http traffic on your chosen port
to prevent this. If you run `runserver` without specifying a host and port, it will run on `127.0.0.1:8000` by default.
