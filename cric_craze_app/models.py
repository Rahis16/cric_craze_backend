from django.db import models


class CrouselData(models.Model):
    image = models.ImageField(upload_to='crousel_images/')
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']


# Create your models here.
class LiveStream(models.Model):
    STREAM_TYPE_CHOICES = [
        ('yt', 'YouTube'),
        ('m3u8', 'M3U8'),
        ('embed', 'Embedded Link'),
    ]

    title = models.CharField(max_length=255)
    teams = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=STREAM_TYPE_CHOICES)
    src = models.CharField(max_length=500, help_text="YouTube video ID or stream URL")

    flag_left = models.URLField(max_length=500, blank=True, null=True)
    flag_right = models.URLField(max_length=500, blank=True, null=True)
    start_time = models.DateTimeField(null=True, blank=True)  # ✅ new field for match schedule
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    
class AppVersion(models.Model):
    version_code = models.PositiveIntegerField()
    version_name = models.CharField(max_length=20)
    apk_file = models.FileField(upload_to='apks/', help_text="Upload APK here", null=True, blank=True)
    force_update = models.BooleanField(default=False)
    release_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.version_name} ({self.version_code})"    
    
    @property
    def download_link(self):
        if self.apk_file:
            return self.apk_file.url
        return ""
