from django.contrib import admin
from portfolio.models import Portfolio

admin.site.register(Portfolio)

# class PostAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': SimpleMDEWidget(wrapper_class='simplemde-box-admin', options=options)},
#     }
#
# class PortfolioAdmin(admin.ModelAdmin):
#     form = PortfolioForm
#
#     class Media:
#         css = {
#             'all': ('css/simplemde.css',)
#         }