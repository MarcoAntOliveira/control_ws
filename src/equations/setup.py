from setuptools import find_packages, setup

package_name = 'equations'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marco',
    maintainer_email=' marcoolivera096@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simulator_node = equations.simulator_node:main',
            'signal_node =  equations.signal_generator:main',
            'drone = equations.drone_simulator:main'
        ],
    },
)
