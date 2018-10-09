# debianitram [at] gmail.com
# Junio 2017

from django.contrib import admin

from rest_framework.filters import SearchFilter


# Agregamos la búsqueda ignorando acéntos. 
LOOKUP_PROFIXES = {'*': 'unaccent__icontains'}
LOOKUP_PROFIXES.update(SearchFilter.lookup_prefixes)



class PublicadoListFilter(admin.SimpleListFilter):
    title = 'Publicado'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'publicado'

    def lookups(self, request, model_admin):
        return (
            ('true', 'Publicados'),
            ('false', 'No Publicados'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'true':
            return queryset.exclude(publicado__isnull=True)
        if self.value() == 'false':
            return queryset.filter(publicado__isnull=True)




class SearchUnaccentFilter(SearchFilter):
    lookup_prefixes = LOOKUP_PROFIXES