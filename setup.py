from setuptools import setup, find_packages
try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass = {'build_ui': build_ui}
except ImportError:
    cmdclass = {}


def read_version():
    """
    Reads the version without self importing
    """
    with open("qregexeditor/__init__.py") as f:
        lines = f.read().splitlines()
        for l in lines:
            if "__version__" in l:
                return l.split("=")[1].strip().replace('"', "").replace(
                    "'", '')


requirements = ['pyqode.qt']


# Data files to install
data_files = [
    ('share/applications/', ['share/qregexeditor.desktop']),
    ('share/pixmaps/', ['share/qregexeditor.png'])
]


setup(
    name='QRegexEditor',
    version=read_version(),
    packages=find_packages(),
    data_files=data_files,
    author='Colin Duquesnoy',
    author_email='c.duquesnoy@sirmogames.com',
    description='PyQt regex editor',
    install_requires=requirements,
    cmdclass=cmdclass,
    entry_points={
        'gui_scripts': [
            'QRegexEditor = qregexeditor.app.main:main'
        ]
    }
)
