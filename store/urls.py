
from django.urls import path
from store import views as s

urlpatterns=[
    path('',s.HomePage,name="home"),
    path('bike',s.Bikers,name="bikes"),
    path('modalstore',s.ModalStore,name="modal"),
    path('compbike/<str:coname>',s.Combikes,name="cobike"),
    path('showBike/<str:cname>/<str:pname>',s.Details,name="detail")
     
]