from setuptools import setup

OPTIONS = {
    'argv_emulation': True,
    'iconfile': '../data/icon.icns'
    }

setup(
    app= ['main.py'],
    name = 'miniGL',
    options = {'py2app': OPTIONS},
    setup_requires=['py2app', 'numpy', 'Pillow', 'pyOpenGL'],
)