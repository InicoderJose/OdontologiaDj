from django.db import models

class servicioManager(models.Manager):

    def buscar_entrada(self, categoria, se):

        if len(categoria) > 0:
            return self.filter(
                especialidad__name = categoria,
                public = True
            ).order_by('-created')

        if len(se) > 0:
            return self.filter(
                title = se,
                public = True
            )
        else:
            return self.filter(
                title__icontains = se,
                public = True
            )
        #else:
            #return self.filter(
                #title__icontains = kword,
                #public = True
            #).order_by('-created')