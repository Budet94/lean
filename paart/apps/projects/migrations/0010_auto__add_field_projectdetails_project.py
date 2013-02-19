# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ProjectDetails.project'
        db.add_column('projects_projectdetails', 'project',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['projects.Project'], unique=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ProjectDetails.project'
        db.delete_column('projects_projectdetails', 'project_id')


    models = {
        'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        'projects.benefit': {
            'Meta': {'ordering': "['label']", 'object_name': 'Benefit'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.classification': {
            'Meta': {'ordering': "['label']", 'object_name': 'Classification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.fiscalyear': {
            'Meta': {'ordering': "['label']", 'object_name': 'FiscalYear'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'projects.opportunity': {
            'Meta': {'ordering': "['label']", 'object_name': 'Opportunity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.project': {
            'Meta': {'ordering': "['label']", 'object_name': 'Project'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['agencies.Agency']"}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.projectbudget': {
            'Meta': {'object_name': 'ProjectBudget'},
            'benefits': ('django.db.models.fields.TextField', [], {}),
            'director': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infrastructure': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'limitations': ('django.db.models.fields.TextField', [], {}),
            'presumptions': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.Project']", 'unique': 'True'}),
            'requirements': ('django.db.models.fields.TextField', [], {}),
            'risks': ('django.db.models.fields.TextField', [], {})
        },
        'projects.projectdetails': {
            'Meta': {'object_name': 'ProjectDetails'},
            'benefit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Benefit']"}),
            'benefit_other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'end_period': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'end_period'", 'to': "orm['projects.FiscalYear']"}),
            'explanation': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opportunity': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projects.Opportunity']", 'symmetrical': 'False'}),
            'other_agencies': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.Project']", 'unique': 'True'}),
            'sharing_benefit': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sharing_benefit'", 'symmetrical': 'False', 'to': "orm['projects.Benefit']"}),
            'stage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Stage']"}),
            'start_period': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'start_period'", 'to': "orm['projects.FiscalYear']"}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Topic']"}),
            'topic_other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        'projects.projectinfo': {
            'Meta': {'object_name': 'ProjectInfo'},
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Classification']"}),
            'classification_other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'expected_results': ('django.db.models.fields.TextField', [], {}),
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fiscal_year'", 'to': "orm['projects.FiscalYear']"}),
            'goals': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'methodology': ('django.db.models.fields.TextField', [], {}),
            'milestones': ('django.db.models.fields.TextField', [], {}),
            'needs': ('django.db.models.fields.TextField', [], {}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.Project']", 'unique': 'True'}),
            'purpose': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Purpose']"}),
            'purpose_other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'sponsor': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'projects.purpose': {
            'Meta': {'ordering': "['label']", 'object_name': 'Purpose'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.stage': {
            'Meta': {'ordering': "['label']", 'object_name': 'Stage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'projects.topic': {
            'Meta': {'ordering': "['label']", 'object_name': 'Topic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['projects']