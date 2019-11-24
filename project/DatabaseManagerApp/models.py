# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase.
    text = models.TextField(db_column='Text')  # Field name made lowercase.
    textclassid = models.IntegerField(db_column='TextClassId')  # Field name made lowercase.

    class Meta:
        db_table = 'Article'


class NormalizedOrderedWord(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    word = models.TextField(db_column='Word')  # Field name made lowercase.

    class Meta:
        db_table = 'NormalizedOrderedWord'


class NotValuableWord(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    word = models.TextField(db_column='Word')  # Field name made lowercase.

    class Meta:
        db_table = 'NotValuableWord'


class TextClass(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.

    class Meta:
        db_table = 'TextClass'
