from django.contrib import admin

import models

admin.site.register(models.Repository)
admin.site.register(models.Series)
admin.site.register(models.PackageSource)
admin.site.register(models.GithubRepository)

