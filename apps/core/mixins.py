from dal import autocomplete


class AutocompleteMixin(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return self.model.objects.none()

        qs = self.model.objects.all()

        if self.q:
            return qs.filter(self.query())
        # Controlar el funcionamiento cuando son muchos registros.
        return qs

    def query(self):
        raise NotImplementedError
    

class ModelAdminContext(object):

    modeladmin = None

    def get_context_data(self, **kw):
        # Se agrega context_data de admin a la vista.
        if self.modeladmin:
            kw.update(
                self.modeladmin.admin_site.each_context(self.request)
            )
            
            kw.update({
                'opts': self.modeladmin.model._meta,
                'original': self.object,
                'has_add_permission': self.modeladmin.has_add_permission(
                    self.request
                ),
                'has_change_permission': self.modeladmin.has_change_permission(
                    self.request, self.object
                ),
                'has_delete_permission': self.modeladmin.has_delete_permission(
                    self.request, self.object
                ),
            })

        return super().get_context_data(**kw)