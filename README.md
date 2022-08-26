# ROS-Intro-Project

This project involves creating a ROS package that uses turtlesim. The objective
is to create a simulation where one turtle is controlled by the user (using
turtle_teleop_key) and the other turtle follows the controlled turtle _without
using the tf package_. An idea of what this should look like can be seen below
where the green turtle is controlled using turtle_teleop_key and the white
turtle follows the green turtle.

![Turtle Following Example](/media/turtle_follow.png)

## Goals

A demonstration of what is expected should have taken place in the first
software meeting you attend. If you joined after the first software meeting,
approach a software lead so they could show you what we expect from you. This
project will not only help you understand how to work with ROS, but also how to
navigate the ROS wiki and find resources to help you in a project. "Googling"
things is probably one of the most fundamental skills of a developer!

Once you finish this project, you will be considered a software team member and
be expected to contribute towards AMP's codebase.

## Overview

In order to complete this task a basic understanding of ROS is required. You
will need to complete the
[core ROS tutorials](http://wiki.ros.org/ROS/Tutorials) to solidify core
concepts and understand the ROS packages/nodes you will use in this project
(turtlesim, turtle_teleop_key, etc.).

This project was inspired by the
[intro tf tutorials](http://wiki.ros.org/tf/Tutorials). Although optional, I
would recommend going through these tutorials to gain an understanding of how
to solve this problem using tf's. And if you are interested, I would also
recommend checking out the other
[ROS Navigation tutorials](http://wiki.ros.org/navigation/Tutorials) as they
may also contain some helpful information for this challenge.

The challenge of this project is to replicate the `turtle_tf_demo.launch` in
the [intro tf tutorials](http://wiki.ros.org/tf/Tutorials) without using tf!
Doing this will allow you to gain a solid understanding of the core concepts of
ROS as well as appreciate the role and power of the tf package.

Finally, this project will get you familiar with Git/GitHub, and our code
review workflow (PRs). Please consult [our GitHub guide](https://docs.google.com/document/d/1lt0BorKFiq0WkigpkvPjANQa4m6CsIo9VEz6uAMz1ZQ/edit?usp=sharing)
and feel free to ask the software leads any questions if you get stuck.

Ready? Checkout the [Instructions](INSTRUCTIONS.md) to get started. Have fun!

## Resources

Here are some resources you may find useful:

- http://wiki.ros.org/ROS/Tutorials/CreatingPackage

- http://wiki.ros.org/ROS/Tutorials/UnderstandingServicesParams
