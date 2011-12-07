from setuptools import setup, find_packages

version = "0.1"

long_description = ""
try:
    long_description=file('README').read()
except Exception:
    pass

license = ""
try:
    license=file('MIT_License.txt').read()
except Exception:
    pass


setup(
    name = 'django-cms-sorl-pictures',
    version = version,
    description = 'Django CMS Sorl Pictures Plugins',
    author = 'Luke Jernejcic',
    author_email = 'luke@jernejcic.com',
    url = 'http://github.com/mostlybinary/django-cms-sorl-pictures',
    packages = find_packages(),
    package_data={
        'cms_sorl_pictures': [
            'templates/*/*.html',
            'templates/*/*/*.html',
            'static/*/css/*.css',
            'static/*/images/*',
            'static/*/js/*.js',
        ],
    },
    zip_safe=False,
    install_requires=[
        "django-cms>=2.2",
        "sorl-thumbnail>=11.09.1",
    ],

    download_url= 'https://mostlybinary@github.com/mostlybinary/django-cms-sorl-pictures.git',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=long_description,
    license=license,
    keywords = "django cms sorl thumbnails photos pictures",
)
