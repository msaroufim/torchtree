from setuptools import setup

setup(
    name='treetorch',
    version='0.1',
    description='Module for building spatial partitioning trees',
    author='Mark Saroufim',
    author_email='marksaroufim@gmail.com',
    url='http://wwww.marksaroufim.com',
    packages=['treetorch'],
      long_description="""\
        Module for building spatial partitioning trees.
        Supported tree types:
            * KD
            * PCA
            * Random projection

        Also includes a generic interface to support new tree types easily
      """,
      classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Data structures",
      ],
      keywords='kd-tree rp-tree pca-tree nearest-neighbor',
      license='GPL',
      install_requires=[
        'pytorch',
      ],
      )