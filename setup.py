from distutils.core import setup


setup(
    name="django-mailer",
    version=__import__("mailer").__version__,
    description="A reusable Django app for queuing the sending of email",
    long_description=open("docs/usage.rst").read(),
    author="Pinax Team",
    author_email="developers@pinaxproject.com",
    url="http://github.com/pinax/django-mailer/",
    packages=[
        "mailer",
        "mailer.management",
        "mailer.management.commands",
    ],
    package_dir={"mailer": "mailer"},
    package_data={'mailer': ['locale/*/LC_MESSAGES/*.*']},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Framework :: Django",
    ],
    setup_requires=[
        'Django >= 1.4',
        'lockfile >= 0.8',
        ],

)
