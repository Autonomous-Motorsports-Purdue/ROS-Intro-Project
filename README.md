# intro-project

## Objective
This project involves creating a ROS package that uses turtlesim. The objective is to create a simulation where one turtle is controlled by the user (using turtle_teleop_key) and the other turtle follows the controlled turtle *without using the tf package*. An idea of what this should look like can be seen below where the green turtle is controlled using turtle_teleop_key and the white turtle follows the green turtle.

![Turtle Following Example](/turtle_follow.png)

## Resources
In order to complete this task a basic understanding of ROS is required. You will need to complete the [core ROS tutorials](http://wiki.ros.org/ROS/Tutorials) to solidify core concepts and understand the ROS packages/nodes you will use in this project (turtlesim, turtle_teleop_key, etc.). 

This project was inspired by the [intro tf tutorials](http://wiki.ros.org/tf/Tutorials). ALthough optional, I would recommend going through these tutorials to gain an understanding of how to solve this problem using tf's. And if you are interested, I would also recommend checking out the other [ROS Navigation tutorials](http://wiki.ros.org/navigation/Tutorials) as they may also contain some helpful information for this challenge.

The challenge of this project is to replicate the `turtle_tf_demo.launch` in the [intro tf tutorials](http://wiki.ros.org/tf/Tutorials) without using tf! Doing this will allow you to gain a solid understanding of the core concepts of ROS as well as appreciate the role and power of the tf package.

Finally, this project will get you familiar with Git/GitHub, and our code review workflow (PRs). Please consult [our GitHub guide](https://docs.google.com/document/d/1lt0BorKFiq0WkigpkvPjANQa4m6CsIo9VEz6uAMz1ZQ/edit?usp=sharing) and feel free to ask the software leads any questions if you get stuck.

## Submission Instructions
1. Please fork this repository.
2. Push your newly created catkin workspace (initialize the git repository at 'build', 'devel', 'src' level) on the master branch.
3. Create a new branch (name it something like solution-dev) and develop your soltuion within that branch.
4. Push committs to remote as you iterately develop your solution. 
5. Once your solution is complete and pushed, create a pull request to merge your development branch into master. Add the software leads (GitHub users @zghera, @gfaout, and @ihagedo) as reviewers for your PR.
6. Respond to any code-review comments until you have approvals from all code reviewers.
7. Be proud of your great work and get ready to contribute to contribute to the AMP codebase!
