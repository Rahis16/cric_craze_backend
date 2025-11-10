from django.contrib import admin
from .models import LiveStream, CrouselData


# Register your models here.
@admin.register(LiveStream)
class LiveStreamAdmin(admin.ModelAdmin):
    list_display = ('title', 'teams', 'type', 'created_at')

@admin.register(CrouselData)
class CrouselDataAdmin(admin.ModelAdmin):
    list_display = ('order', 'created_at')
    ordering = ('order',)
    readonly_fields = ('created_at',)
    fields = ('image', 'order', 'created_at')
