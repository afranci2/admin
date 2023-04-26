from setuptools import setup, find_packages

setup(
    name='take_home_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'requests',
        "pandas",
        "psycopg2-binary",
        "sqlalchemy"
        # add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'run-app=take_home_project.app:app.run'
        ]
    },
    author='Anthony Francisco',
    author_email='anthony.francisco.aoct@gmail.com',
    description='Anthony Take Home',
    url='https://github.com/afranci2',
)
