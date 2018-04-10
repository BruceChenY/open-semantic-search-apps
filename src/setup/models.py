from django.db import models

class Setup(models.Model):

	title = models.CharField(max_length=1000, blank=True)
	description = models.TextField(blank=True)

	language = models.CharField(max_length=2, default="en", blank=True)

	languages = models.CharField(max_length=300, default="en", blank=True)
	languages_force = models.CharField(max_length=300, default="en", blank=True)
	
	ocr = models.BooleanField(default=True)

	ocr_languages = models.CharField(max_length=300, default="en", blank=True)

	ocr_descew = models.BooleanField(default=False)

	ocr_pdf = models.BooleanField(default=True)
	
	ner_spacy = models.BooleanField(default=True)

	ner_stanford = models.BooleanField(default=False)