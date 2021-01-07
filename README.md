Simple example app to store results of played match inside company 

Example deployment: https://tomaszd.herokuapp.com
### Api 
```
eb status  -status of eb
eb appversion -> deployment history https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-appversion.html
```
Save the file, and then deploy your application by running eb deploy. When you run eb deploy, the EB CLI bundles up the contents of your project directory and deploys it to your environment.
```
~/ebdjango$ eb deploy
```
If you are using Git with your project, see Using the EB CLI with Git.
When the environment update process completes, open your web site with eb open:
~/ebdjango$ eb open
 (http://django-env.grtw6epeki.eu-west-3.elasticbeanstalk.com)
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html


how to start :

##########################
# aws:
```
eb status  -status of eb
eb appversion -> deployment history https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-appversion.html
eb deploy
eb open
eb ssh
```
```
#############      migrations  ################
python manage.py makemigrations ebdjango
python manage.py migrate
python manage.py collectstatic
############# run #####################
python manage.py runserver
```


### to download cards:
```
scp -r -i /home/tomaszd/.ssh/aws-eb ec2-user@35.181.7.123:/home/ec2-user/Results/Results_2019_July/* .
eb ssh
crontab -e
see when the scripts will do the stuff
```

```
source /opt/python/run/venv/bin/activate
mkdir -p ~/LOGS
mkdir -p ~/Results
cd /opt/python/current/app/ebdjango/../PriceChecker/
touch ~/LOGS/logi.txt
python collection_helper.py > ~/LOGS/logi.txt
```
### to debug locally
```
#################python manage.py shell

>>> import django
>>> django.setup()
from ebdjango.models import TVSetting
In [2]: TVSetting.objects.all()
Out[2]: []
```
### to save db data 
```
###########################DATABASE############################3
source /opt/python/run/venv/bin/activate
cd /opt/python/current/app
python manage.py dumpdata --indent 4  ~>db.json
python manage.py loaddata ~/db.json
```
### to store pip  reqs:
```
pip3 requirements + venv ->  ebdjango/bin/venv3/bin/activate
django2.0:
source ./bin/venv3/bin/activate
```
