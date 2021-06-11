from django.contrib import admin
from django.urls import  path
from .views import *

urlpatterns = [    


    #PUBLICO
    path('<str:slug>', pagina, name='pagina'),

    #USER
    path('listado-paginas/', listado_paginas, name='listado_paginas'),
    path('nueva_pagina/', nueva_pagina, name='nueva_pagina'),
    path('editar_pagina/<pagina_id>', editar_pagina, name='editar_pagina'),
    path('eliminar_pagina/<pagina_id>', eliminar_pagina, name='eliminar_pagina'),

]