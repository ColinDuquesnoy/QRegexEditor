from setuptools import setup, find_packages
import sys
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


requirements = []


# Data files to install
if sys.platform == 'win32':
    data_files = []
else:
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
    author_email='colin.duquesnoy@gmail.com',
    maintainer='Colin Duquesnoy',
    maintainer_email='Colin Duquesnoy',
    description='PyQt regex editor',
    keywords=["regular expression editor"],
    install_requires=requirements,
    cmdclass=cmdclass,
    url='https://github.com/ColinDuquesnoy/QRegexEditor',
    entry_points={
        'gui_scripts': [
            'QRegexEditor = qregexeditor.app.main:main'
        ],
        'pyqt_distutils_hooks': [
            'fix_qt_imports = qregexeditor._hooks:fix_qt_imports']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Widget Sets',
    ]
)
