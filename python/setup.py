from setuptools import setup

APP = ['main.py']
OPTIONS = {'argv_emulation': True, 'includes': ['EXTERNAL LIBRARY'], }

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app', 'numpy', 'Pillow', 'pyOpenGL'],
)