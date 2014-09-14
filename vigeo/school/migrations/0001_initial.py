# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'school_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('correct_answer', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('possible_answer0', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('possible_answer1', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'school', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'school_question')


    models = {
        u'school.question': {
            'Meta': {'object_name': 'Question'},
            'correct_answer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'possible_answer0': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'possible_answer1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['school']