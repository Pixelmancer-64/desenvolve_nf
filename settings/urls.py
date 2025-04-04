from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('autenticacao.urls')),
    path('', include('desenvolve_nf.urls')),
    
    path('capacitacao-profissional/', include('cursos.urls')),    
    # path('capacitacao-profissional/palestras/', include(('palestras.urls', 'palestras'), namespace ='palestras')),
    path('financas/', include('financas.urls')),
    path('eventos/', include('eventos.urls')),

    path('casa-do-trabalhador/', include('casa_do_trabalhador.urls')),
    path('bem-estar-animal/', include('bemestaranimal.urls')),
    path('servicos/iluminacao/', include('iluminacao.urls')),
    path('almoxarifado/', include('almoxarifado.urls')),

    path('administracao/', include('administracao.urls')),    
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
