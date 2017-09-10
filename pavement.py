"""paver config file"""

# from testing python book
from paver.easy import sh
from paver.tasks import task, needs

@task
def pypi():
    """Instalation on PyPi"""
    sh('python setup.py sdist')
    sh('twine upload dist/*')

@task
def local():
    """local install"""
    sh("pip uninstall pybiblio")
    sh("python setup.py install develop")



@task
def default():
    """Tests"""
    sh("python pybiblio/pybiblio.py scopus.csv")
    
