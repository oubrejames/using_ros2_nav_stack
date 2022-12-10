from setuptools import setup

package_name = 'nubot_nav'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml',
                                   'config/nav2_params.yaml',
                                   'config/nubot_nav_urdf.rviz',
                                   'launch/manual_explore.launch.xml',
                                   'launch/explore.launch.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='oubre',
    maintainer_email='oubrejames@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['explore = nubot_nav.explore:main'
        ],
    },
)
