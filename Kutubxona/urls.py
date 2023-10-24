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
    path('hamma_kutubxonachilar/', hamma_kutubxonachilar),

    # vazifa

    path('hamma_mualliflar/', hamma_muallif),
    path('muallif/<str:ismi>/', tanlangan_muallif),
    path('hamma_kitoblar/', hamma_kitob),
    path('books/<int:son>/', kitob),
    path('hamma_recordlar/', hamma_record),
    path('hamma_talabalar/', hamma_talabalar),
    path('tirik_mualliflar/', tirik_muallif),
    path('sahifa_kop_kitob/', sahifa_kop_kitob),
    path('kitobi_kop_muallif/', kitobi_kop_muallif),
    path('record_tartiblash/', record_tartiblash),
    path('tirik_muallif_kitob/', tirik_muallif_kitob),
    path('badiiy_kitoblar/', badiiy_kitoblar),
    path('eng_yoshi_katta_muallif/', eng_yoshi_katta_muallif),
    path('kitob_muallif/', kitob_muallif),
    path('tanlangan_record/<int:son>/', tanlangan_record),
    path('bitiruvchi_talaba_record/', bitiruvchi_talaba_record),

    # mashq

    path('talaba_ochir/<int:son>/', talaba_ochir),
    path('kitob_ochir/<int:son>/', kitob_ochir),
    path('muallif_ochir/<int:son>/', muallif_ochir),
    path('record_ochir/<int:son>/', record_ochir),
    path('kutubxonachi_ochir/<int:son>/', kutubxonachi_ochir),

    # update malumot

    path('talaba_update/<int:son>/', talaba_update),
    path('kitob_update/<int:son>/', kitob_update),
    path('kutubxonachi_update/<int:son>/', kutubxonachi_update),
    path('muallif_update/<int:son>/', muallif_update),
    path('record_update/<int:son>/', record_update),

]
