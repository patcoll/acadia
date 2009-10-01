from django.contrib import admin

class CustomAdminSite(admin.sites.AdminSite):
    index_template = None
    login_template = None
    app_index_template = None

    def get_urls(self):
        # from django.conf.urls.defaults import patterns, url
        urls = super(CustomAdminSite, self).get_urls()
        # TODO: iterate through apps, grab and prepend custom admin URLs from a certain location. see django.db.models.loading
        # from django.db.models.loading import get_apps, get_app, get_models, get_model, register_models
        # my_urls = patterns('',
        #     url(r'^nav/$', self.admin_view(some_view))
        # )
        # from acadia.pages.urls import admin_urlpatterns as pages_admin_urlpatterns
        # return pages_admin_urlpatterns + urls
        return urls

admin.site = CustomAdminSite()