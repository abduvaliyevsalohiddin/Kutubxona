from django.contrib import admin
from django.urls import path

from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('', homepage),
    path('kitoblar/', hamma_kitoblar),
    path('ayol_muallif/', ayol_mualliflar_kitoblari),
    path('books/<int:son>/', kitob),

    # vazifa

    path('hamma_mualliflar/', hamma_muallif),
    path('muallif/<str:ismi>/', tanlangan_muallif),
    path('hamma_kitoblar/', hamma_kitob),
    path('books/<int:son>/', kitob),
    path('hamma_recordlar/', hamma_record),
    path('hamma_talabalar/', hamma_talabalar),

    # mashq

    path('talaba_ochir/<int:son>/', talaba_ochir),
    path('kitob_ochir/<int:son>/', kitob_ochir),
]
