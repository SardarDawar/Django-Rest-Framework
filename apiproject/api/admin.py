from django.contrib import admin

# Register your models here.
from .models import finder,Address,Images

from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.contrib import admin


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None,renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" /></a> %s ' % \
                          (image_url, image_url, file_name, _('Change:')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class ImageWidgetAdmin(admin.ModelAdmin):
    image_fields = []

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.image_fields:
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageWidgetAdmin, self).formfield_for_dbfield(db_field, **kwargs)
class ImageAdmin(ImageWidgetAdmin):
    image_fields = ['image',]


class finderAdmin(ImageWidgetAdmin):
    list_display = ['id', 'Name', 'Date_lost','ContactNumber']
    image_fields = ['Photo',]

#class ImageAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
 #   fields = ( 'image_tag','image', )
  #  readonly_fields = ('image_tag',)

#admin changing title
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class MyAdminSite(AdminSite):
    site_title = ugettext_lazy('Finder')
    site_header = ugettext_lazy('Finder')
    index_title = ugettext_lazy('Finder')




my_admin_site =MyAdminSite()
my_admin_site.register(finder,finderAdmin),
my_admin_site.register(Address)
my_admin_site.register(Images,ImageAdmin)

