from distutils.core import setup

setup(
    name='django-auditlog',
    version='0.3.3',
    packages=['auditlog', 'auditlog.migrations'],
    package_dir={'': 'src'},
    url='https://github.com/knyazz/django-auditlog',
    license='MIT',
    author='Jan-Jelle Kester',
    author_email='janjelle@jjkester.nl',
    description='Audit log app for Django',
    install_requires=[
        'Django>=1.7',
        'jsonfield>=1.0.3',
    ]
)
