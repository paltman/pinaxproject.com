from datetime import datetime

from django.db import models



class Release(models.Model):
    
    version = models.CharField(max_length=10)
    stable = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=datetime.now)


class ReleaseFile(models.Model):
    
    release = models.ForeignKey(Release)
    # @@@ needs to work with existing download system
    file = models.FileField(upload_to="downloads")
    md5_hash = models.CharField(max_length=32)
    sha1_hash = models.CharField(max_length=40)
    
    def file_type(self):
        return self.file.name.rsplit(".")[-1]
