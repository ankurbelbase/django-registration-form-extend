from django.conf.urls import url
from signupapp.views import signup

urlpatterns = [

    url(r'^signup/', signup, name = 'signup'),

]
