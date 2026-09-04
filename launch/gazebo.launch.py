import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    package_name = 'robot_pkg'

    pkg_share = FindPackageShare(package=package_name).find(package_name)

    default_model_path = os.path.join(
        pkg_share,
        'urdf',
        'robot.urdf.xacro'
    )

    model = LaunchConfiguration('model')

    robot_description = Command([
        'xacro ',
        model
    ])

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {
                'robot_description': robot_description
            }
        ]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen'
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('ros_gz_sim'),
            '/launch/gz_sim.launch.py'
        ]),
        launch_arguments={
            'gz_args': '-r empty.sdf'
        }.items()
    )

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'robot1',
            '-topic', 'robot_description'
        ],
        output='screen'
    )

    return LaunchDescription([

        DeclareLaunchArgument(
            name='model',
            default_value=default_model_path,
            description='Absolute path to robot URDF/XACRO'
        ),

        gazebo,

        joint_state_publisher_node,

        robot_state_publisher_node,

        spawn_robot,
    ])