from setuptools import setup, find_packages

setup(
    name='qwrapper',
    version='0.1.0',
    author='Ali, Daniel and Sirén',
    author_email='danieldy@uia.no',
    description='This package is a wrapper for easily controlling QEMU by the use of QMP and gdb.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/your-repo',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'qemu.qmp',
        'pygdbmi',
    ],
    python_requires='>=3.6',
)