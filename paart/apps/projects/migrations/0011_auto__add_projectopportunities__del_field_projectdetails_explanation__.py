# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProjectOpportunities'
        db.create_table('projects_projectopportunities', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.Project'], unique=True)),
            ('explanation', self.gf('django.db.models.fields.TextField')()),
            ('other_agencies', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('projects', ['ProjectOpportunities'])

        # Adding M2M table for field opportunity on 'ProjectOpportunities'
        db.create_table('projects_projectopportunities_opportunity', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectopportunities', models.ForeignKey(orm['projects.projectopportunities'], null=False)),
            ('opportunity', models.ForeignKey(orm['projects.opportunity'], null=False))
        ))
        db.create_unique('projects_projectopportunities_opportunity', ['projectopportunities_id', 'opportunity_id'])

        # Adding M2M table for field sharing_benefit on 'ProjectOpportunities'
        db.create_table('projects_projectopportunities_sharing_benefit', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectopportunities', models.ForeignKey(orm['projects.projectopportunities'], null=False)),
            ('benefit', models.ForeignKey(orm['projects.benefit'], null=False))
        ))
        db.create_unique('projects_projectopportunities_sharing_benefit', ['projectopportunities_id', 'benefit_id'])

        # Deleting field 'ProjectDetails.explanation'
        db.delete_column('projects_projectdetails', 'explanation')

        # Deleting field 'ProjectDetails.other_agencies'
        db.delete_column('projects_projectdetails', 'other_agencies')

        # Removing M2M table for field sharing_benefit on 'ProjectDetails'
        db.delete_table('projects_projectdetails_sharing_benefit')

        # Removing M2M table for field opportunity on 'ProjectDetails'
        db.delete_table('projects_projectdetails_opportunity')


    def backwards(self, orm):
        # Deleting model 'ProjectOpportunities'
        db.delete_table('projects_projectopportunities')

        # Removing M2M table for field opportunity on 'ProjectOpportunities'
        db.delete_table('projects_projectopportunities_opportunity')

        # Removing M2M table for field sharing_benefit on 'ProjectOpportunities'
        db.delete_table('projects_projectopportunities_sharing_benefit')


        # User chose to not deal with backwards NULL issues for 'ProjectDetails.explanation'
        raise RuntimeError("Cannot reverse this migration. 'ProjectDetails.explanation' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'ProjectDetails.other_agencies'
        raise RuntimeError("Cannot reverse this migration. 'ProjectDetails.other_agencies' and its values cannot be restored.")
        # Adding M2M table for field sharing_benefit on 'ProjectDetails'
        db.create_table('projects_projectdetails_sharing_benefit', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectdetails', models.ForeignKey(orm['projects.projectdetails'], null=False)),
            ('benefit', models.ForeignKey(orm['projects.benefit'], null=False))
        ))
        db.create_unique('projects_projectdetails_sharing_benefit', ['projectdetails_id', 'benefit_id'])

        # Adding M2M table for field opportunity on 'ProjectDetails'
        db.create_table('projects_projectdetails_opportunity', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectdetails', models.ForeignKey(orm['projects.projectdetails'], null=False)),
            ('opportunity', models.ForeignKey(orm['projects.opportunity'], null=False))
        ))
        db.create_unique('projects_projectdetails_opportunity', ['projectdetails_id', 'opportunity_id'])


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.Project']", 'unique': 'True'}),
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
        'projects.projectopportunities': {
            'Meta': {'object_name': 'ProjectOpportunities'},
            'explanation': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opportunity': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projects.Opportunity']", 'symmetrical': 'False'}),
            'other_agencies': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.Project']", 'unique': 'True'}),
            'sharing_benefit': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sharing_benefit'", 'symmetrical': 'False', 'to': "orm['projects.Benefit']"})
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