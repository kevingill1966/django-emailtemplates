# coding=utf-8
from django.conf import settings
from django.test import TestCase
from django.core import mail
from mock import Mock

from ..registry import EmailTemplateRegistry


class EmailTemplateRegistryTest(TestCase):

    def test_register_template(self):
        registry = EmailTemplateRegistry()
        registry.register('hello_template.html')

    def test_get_help_text(self):
        template_registry = EmailTemplateRegistry()
        template_registry.register('hello_template.html', help_text=u'Hello template',
                                   help_context={'username': u'Name of user in hello expression'})
        help_text = template_registry.get_help_text('hello_template.html')
        self.assertEqual(help_text, u'Hello template')

    def test_get_help_context(self):
        template_registry = EmailTemplateRegistry()
        template_registry.register('hello_template.html', help_text=u'Hello template',
                                   help_context={'username': u'Name of user in hello expression'})
        help_context = template_registry.get_help_context('hello_template.html')
        self.assertIn('username', help_context)

    def test_get_email_templates(self):
        template_registry = EmailTemplateRegistry()
        template_registry.register('hello_template.html', help_text=u'Hello template',
                                   help_context={'username': u'Name of user in hello expression'})
        template_registry.register('simple_template.html', help_text=u'Simple template')
        self.assertEqual(2, len(template_registry.get_email_template_choices()))

    def test_get_email_template_names(self):
        template_registry = EmailTemplateRegistry()
        template_registry.register('hello_template.html', help_text=u'Hello template',
                                   help_context={'username': u'Name of user in hello expression'})
        template_registry.register('simple_template.html', help_text=u'Simple template')
        self.assertIn('hello_template.html', template_registry.get_email_template_choices())
        self.assertIn('simple_template.html', template_registry.get_email_template_choices())



