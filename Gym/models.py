from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File

def compress(image):
    im = Image.open(image)
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=60) 
    new_image = File(im_io, name=image.name)
    return new_image

class img(models.Model):
    title = models.TextField()
    cover = models.FileField(upload_to='')

    def save(self, *args, **kwargs):
                new_image = compress(self.cover)
                self.cover = new_image
                super().save(*args, **kwargs)

    def __str__(self):
        return self.title
