#!/usr/bin/env python

from setuptools import setup

app_name = 'wmd'

setup(name='django-%s-editor' % app_name,
        version='0.9.0',
        packages=[app_name],
        package_data = {app_name: ['static/wmd/*.js', 'static/wmd/*.css', 'static/wmd/images/*.png']},
        author = 'Joshua Partogi',
        author_email = 'joshua.partogi@gmail.com',
        url = 'http://github.com/marcuswhybrow/django-wmd-editor/',
        download_url = 'http://github.com/marcuswhybrow/django-wmd-editor/archives/master/',

        license = "BSD License",
        keywords = "django wmd editor",
        python_requires='>=3.8',
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Framework :: Django :: 5.2',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.12',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        platforms = ['any'],
)
