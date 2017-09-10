from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pybiblio',
      version='0.0.0',
      description='Analysis of bibliographic information using python',
      long_description='A tool for creating and gradding assignments in the Jupyter Notebook using the Virtual Programming Lab plugging and Moodle',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Education',
        'License :: Free For Educational Use',
      ],
      keywords='Scopus',
      url='http://github.com/jdvelasq/pybiblio',
      author='Juan D. Velasquez, Johana Garces',
      author_email='jdvelasq@unal.edu.co',
      license='MIT',
      packages=['pybibio'],
      include_package_data=True,
      zip_safe=False)
