eb status  -status of eb
eb appversion -> deployment history https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-appversion.html




#Save the file, and then deploy your application by running eb deploy. When you run eb deploy, the EB CLI bundles up the contents of your project directory and deploys it to your environment.
~/ebdjango$ eb deploy

If you are using Git with your project, see Using the EB CLI with Git.

When the environment update process completes, open your web site with eb open:

~/ebdjango$ eb open

 (http://django-env.grtw6epeki.eu-west-3.elasticbeanstalk.com)

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html



how to start :

##########################
#aws:
eb status  -status of eb
eb appversion -> deployment history https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-appversion.html
eb deploy
eb open
eb ssh




####################migrations->
python manage.py makemigrations ebdjango
python manage.py migrate
python manage.py collectstatic
python manage.py runserver



#################python manage.py shell

>>> import django
>>> django.setup()
from ebdjango.models import TVSetting
In [2]: TVSetting.objects.all()
Out[2]: []


