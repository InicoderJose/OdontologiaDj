from django.db.models.signals import pre_save, post_save,post_delete
from .models import Sonrisa
from django.dispatch import receiver
from PIL import Image
import imagehash
import os

   

