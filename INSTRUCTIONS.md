# Instructions

**Note:** This project assumes you know at least some basic git version control.

Most of the things that are laid out are done from the terminal. It can be
overwhelming and you may not understand what is going on, that is okay. If you
are stuck at any point in the project, feel free to reach out to the Software
Leads or anyone else for help!

If this is your first time using ROS, go through the
[core ROS tutorials](http://wiki.ros.org/ROS/Tutorials) to get yourself
comfortable. It goes over installation process and all of the basics, you don't
have to go through all of them. They are a good reference for ROS.

## Step I: Setting up a VM

Instructions for setting up a VM on Windows and MacOS are different.

- [Windows](https://davidbombal.com/ubuntu-20-04-install-windows-10-using-vmware-player/).

- MacOS:
  - If you have an Apple Silicon laptop, work with @alanssitis to get it set up.
  - [Old Intel Macs](https://fossbytes.com/how-to-install-ubuntu-20-04-lts-virtualbox-windows-mac-linux/)

Setting up a VM is very tedious, and can be very annoying. So best of luck!

## Step II: Getting Started with a Workspace and Version Control

1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this
   repository to your GitHub account, make sure the fork is public for code review.
   It is your own copy of this repo!

2. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
   your fork of this repository on your machine.

3. Create and checkout to a new
   [branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches);
   this branch will store all the progress for your project. This can be done via
   the following command:

```bash
git checkout -b solution-dev
```

4. Initialize a ROS catkin workspace in the home directory of the VM, and name
   it `intro-project`.Make sure that when you run `ls`, you can see the `build/`,
   `devel/`, and `src/` directories.

5. Add and commit your initial workspace to this branch, you can name this
   commit `initial commit`.

```bash
git add . && git commit -m "initial commit"
```

6. Link the solution branch to remote and push the commit with:

```bash
git push --set-upstream origin solution-dev
```

7. You can now work on the project and have it saved in a remote repository.
   This allows you to work on the project in multiple devices easily and protects
   your project from accidents!

## Step III: Working on the Project

The [core ROS tutorials](http://wiki.ros.org/ROS/Tutorials) uses a bit of
turtlesim. We will be using more of it. If you weren't here for the first
meeting where we showed a demo of what we want, contact @alanssitis.

Here is a diagram of what should be the structure of your project when it is up
and running! It does not have to be exact, so feel free to use it for inspiration.

![Diagram of expected node layout for the project](/media/project_node_layout.png)

The only thing you will actually be coding is the node that will provide
instructions to the `follower_turtle` and a launch file that will get it up
and running.

## Step IV: Submitting your Project via a Pull Request

1. Make sure the branch `solution-dev` in your fork of the AMP repo has your
   project. You can run `git status` in your local machine to check if your fork
   is up to date.

2. In this Repository's website (on github.com), create a
   [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
   to merge your development branch into this repo's master branch. Add the GitHub
   users @alanssitis, and @Reschivon as reviewers for your PR.

3. Respond to any code-review comments until you have approvals from all code
   reviewers. Once things looks good, the software leads will give you our approval
   and then close the PR (your great solution can't sitting in the repo unfortunately).

4. Be proud of your great work and get ready to contribute to the AMP codebase!
