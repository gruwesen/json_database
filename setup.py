from setuptools import setup

setup(
    name='json_database',
    version='0.4.0',
    packages=['json_database', 'json_database.utils'],
    url='https://github.com/OpenJarbas/json_database',
    license='MIT',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    install_requires=["pyxdg", "fasteners"],
    description='searchable json database with persistence'
)
