from setuptools import setup

setup(
    name='my_python_pack',
    version='0.0.0',
    packages=['my_python_pack'],
    install_requires=['setuptools', 'rospy', 'std_msgs'],
    scripts=[
        'scripts/my_node.py',
    ],
)
