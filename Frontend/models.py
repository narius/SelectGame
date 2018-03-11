from django.db import models
from django.utils.translation import gettext


# Create your models here.
class model_link(models.Model):
    '''
        A model to keep track of all links

        link is the address, exampel "SelectGame:index"
        text is the text that will be shown on the webb
        authenticated if True the user must be authenticated to see the link
    '''
    link = models.CharField(max_length=100, verbose_name=gettext("link"))
    text = models.CharField(max_length=30, verbose_name=gettext("text"))
    authenticated = models.BooleanField(default=False)
    glyphicon = models.CharField(max_length=100, verbose_name=gettext("glyphicon"), null=True, blank=True)

    class Meta:
        verbose_name = gettext('link')
        verbose_name_plural = gettext('links')

    def __str__(self):
        return self.link+" "+self.text


class model_accordion(models.Model):
    header = models.CharField(max_length=100, verbose_name=gettext("header"))
    links = models.ManyToManyField(model_link, verbose_name=gettext("links"))
    glyphicon = models.CharField(max_length=100, verbose_name=gettext("glyphicon"), null=True, blank=True)

    class Meta:
        verbose_name = gettext('accordion')
        verbose_name_plural = gettext('accordions')

    def __str__(self):
        return self.header
