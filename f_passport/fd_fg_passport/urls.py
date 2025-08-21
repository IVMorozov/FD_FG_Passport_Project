"""
URL configuration for fd_fg_passport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path
from pathlib import Path
import os
from django.conf.urls.static import static
from dotenv import load_dotenv
from core.views import (
    LandingView, 
)

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
# MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
# TELEGRAM_BOT_API_KEY=os.getenv('TELEGRAM_BOT_API_KEY')
# TELEGRAM_USER_ID=os.getenv('TELEGRAM_USER_ID')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingView.as_view(), name='landing'),    
]

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = BASE_DIR / "staticfiles"