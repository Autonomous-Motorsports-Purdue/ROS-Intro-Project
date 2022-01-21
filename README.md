# ROS-Intro-Project

This project involves creating a ROS package that uses turtlesim. The objective is to create a simulation where one turtle is controlled by the user (using turtle_teleop_key) and the other turtle follows the controlled turtle *without using the tf package*. An idea of what this should look like can be seen below where the green turtle is controlled using turtle_teleop_key and the white turtle follows the green turtle.

![Turtle Following Example](/media/turtle_follow.png)

## Brief Overview
In order to complete this task a basic understanding of ROS is required. You will need to complete the [core ROS tutorials](http://wiki.ros.org/ROS/Tutorials) to solidify core concepts and understand the ROS packages/nodes you will use in this project (turtlesim, turtle_teleop_key, etc.). 

This project was inspired by the [intro tf tutorials](http://wiki.ros.org/tf/Tutorials). Although optional, I would recommend going through these tutorials to gain an understanding of how to solve this problem using tf's. And if you are interested, I would also recommend checking out the other [ROS Navigation tutorials](http://wiki.ros.org/navigation/Tutorials) as they may also contain some helpful information for this challenge.

The challenge of this project is to replicate the `turtle_tf_demo.launch` in the [intro tf tutorials](http://wiki.ros.org/tf/Tutorials) without using tf! Doing this will allow you to gain a solid understanding of the core concepts of ROS as well as appreciate the role and power of the tf package.

Finally, this project will get you familiar with Git/GitHub, and our code review workflow (PRs). Please consult [our GitHub guide](https://docs.google.com/document/d/1lt0BorKFiq0WkigpkvPjANQa4m6CsIo9VEz6uAMz1ZQ/edit?usp=sharing) and feel free to ask the software leads any questions if you get stuck.

## Goal of the Project

A demonstration of what is expected should have taken place in the first software meeting you attend. If you joined after the first software meeting, approach a software lead so they could show you what we expect from you. This project will not only help you understand how to work with ROS, but also how to navigate the ROS wiki and finding resources to help you in a project. "Googling" things is probably one of the most fundamental skills of a developer!

Once you finish this project, you will be considered a software team member and be expected to contribute towards AMP's codebase.

## Instructions for the Project
Note: This project assumes you know at least some basic git / version control. If you are stuck at any point in the project, feel free to reach out to the Software Leads for guidance.

### Getting Started with a Workspace and Version Control
1. Install ROS Kinetic Kame on your Ubuntu 16.04 Virtual Machine per steps 1 and 2 of the instructions provided in the [AMP ROS Learning Guide](https://docs.google.com/document/d/1TD68GuHSs1Ub-vxHttd87Ktm60BSqcbSFBRRalwmUzU/edit?usp=sharing) (This may change as there are talks to port v1 to [Noetic](http://wiki.ros.org/noetic)) **AND** make sure you have gone through the [core ROS tutorials](http://wiki.ros.org/ROS/Tutorials).
2. Initialize a ROS catkin workspace in the home directory of the VM, and name it `intro-project`.
3. Initialize git inside the project folder. Make sure that when you `ls`, you can see the `build/`, `devel/`, and `src/` directories.
4. Checkout to a new branch which will contain all the files for your project. This can be done via the following command: 
```bash
git checkout -b solution-dev
``` 
5. Add and commit your initial workspace to this branch, you can name this commit `initial commit`.
```bash
git add . && git commit -m "initial commit"
```

### Linking your Project to a Remote Repository
1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repository to your GitHub account, make sure the fork is public for code review.
2. In your project, configure the remote repository by running the command:
```bash
git remote add origin <link-to-your-fork>
```
3. Setup an upstream link and push the commit with the command:
```bash
git push --set-upstream origin solution-dev
```
4. You can now work on the project and have it saved in a remote repository. This allows you to work on the project in multiple devices easily and protects your project from accidents!

### Submitting your Project via a Pull Request
1. Make sure the branch `solution-dev` in your fork of this repository has your project. Make sure all files are in the branch by running `git status`, it will tell you if there are any inconsistencies between your local project and the remote repository.
2. In this Repository's website (on github.com), create a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to merge your development branch into this repo's master branch. Add the GitHub users @zghera, @alanssitis, and @Reschivon as reviewers for your PR.
3. Respond to any code-review comments until you have approvals from all code reviewers. Once things looks good, the software leads will give you our approval and then close the PR (your great solution can't sitting in the repo unfortunately).
4. Be proud of your great work and get ready to contribute to the AMP codebase!

## Resources
Here are some resources you may find useful:
* http://wiki.ros.org/ROS/Tutorials/CreatingPackage
* http://wiki.ros.org/ROS/Tutorials/UnderstandingServicesParams
