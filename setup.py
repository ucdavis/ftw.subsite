from setuptools import setup, find_packages
import os

version = '2.0.1.dev0'

tests_require = [
    'collective.mockmailhost',
    'ftw.builder',
    'ftw.testing [splinter]',
    'plone.app.portlets',
    'plone.app.testing',
    'pyquery',
    'ftw.testbrowser',
    'ftw.builder',
    ]

setup(name='ftw.subsite',
      version=version,
      description="",
      long_description=open('README.rst').read() + '\n' +
      open(os.path.join('docs', 'HISTORY.txt')).read(),

      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers

      classifiers=[
          'Framework :: Plone',
          'Framework :: Plone :: 4.1',
          'Framework :: Plone :: 4.2',
          'Framework :: Plone :: 4.3',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],

      keywords='ftw subsite',
      author='4teamwork AG',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/ftw.subsite',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'ftw.upgrade>1.14.0',
          'plone.formwidget.contenttree',
          'plone.formwidget.namedfile',
          'plone.namedfile',
          'setuptools',
          'plone.app.dexterity',
          'plone.directives.form',
          'plone.app.relationfield',
          'plone.autoform',
          'plone.behavior',
          'ftw.simplelayout [contenttypes]',
          'Products.contentmigration',
          'plone.app.contenttypes<1.2b, >1.1b',
          'plone.app.event',
          'ftw.builder',
          'Plone',
      ],

      tests_require=tests_require,
      extras_require={'tests': tests_require},

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
