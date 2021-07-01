from paginas.models import *
    
def info_base(request):
    def wrap(request, *args, **kwargs):
        pagina_publicada = Pagina.objects.filter(publicar=True)
        info_base = {
            'pagina_publicada':pagina_publicada,
        }
        return info_base
