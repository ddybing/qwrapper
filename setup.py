from setuptools import setup, find_packages

setup(
    name='qwrapper',
    version='0.1.1',
    description='A QEMU wrapper for Python',
    author='Daniel Dybing',
    author_email='danieldy@uia.no',
    packages=find_packages(),
    install_requires=[
        'pygdbmi',
        'qemu.qmp',
        # List your project dependencies here
        # For example:
        # 'numpy>=1.18.1',
        # 'pandas>=1.0.1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)