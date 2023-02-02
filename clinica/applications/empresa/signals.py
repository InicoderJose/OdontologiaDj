# -*- coding: utf-8 -*-
from django.db.models.signals import post_save, pre_save
	#I have used django user model to use post save, post delete.
from .models import Tecnologia, Servicio
from django.dispatch import receiver

    

