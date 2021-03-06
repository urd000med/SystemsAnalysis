"""SystemsAnalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" # why does django give a section for howto here, but not in ANY other files? like... a models helper would be kinda nice, those things are a HUGE pain to write.
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import SignUpView

urlpatterns = [
    path('me/',views.me),
    path('admin/',views.adm),
    path('del/<str:type>/<str:id>/<str:power>', views.dele),
    path('makeadmin/<str:id>/<str:power>',views.makeadmin),
    path('', views.home),
    path("accounts/profile/",views.userpage),
    path('accounts/',include('django.contrib.auth.urls')), # login and signup features
    path('signup/',SignUpView.as_view(), name = 'signup'),
    path('a/',views.testview),
    path('articles/<str:type>',views.posts),
    path('create/',views.create),
    path('post/<str:id>',views.post), # the naming convention on this is VERY bad :)
    path('noti/', views.notifications),
    path('contact/', views.contact),
    path('test/', views.testview),

    # admin page for managing site content, and giving users permissions
] # one of the form things... will need to change in prod mode
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
