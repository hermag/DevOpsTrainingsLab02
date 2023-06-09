# About the package
This is the example project for the Advanced IT DevOps trainings course. In particular this is the package building recipe for the sample package with two functions.

## Getting started
pip install https://github.com/hermag/DevOpsTrainingsLab02 #eventually have to update

## Add your files

If you would like to contribute feel free, but in the following way

```
cd existing_repo
git remote add origin https://github.com/hermag/DevOpsTrainingsLab02
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- For now there is nothing to inetgrate here

## Collaborate with your team

- Yet no team is here

## Test and Deploy

We are going to use the github actions CI/CD pipeline.

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
DevOpsTrainingsLab02

## Description
This is an example project to show the full simple pipeline from building the package, with running the unit tests. After building the wheel package it will be pushed to the github artifact registry. Later this package will be used in a simple Flask application. The Flask application will be containerized and the container image will be pushed to the GitHub docker registry. After successful push to the container registry the image will be deploied on AWS Free Tier EC2 Instance.

## Badges
We have no badges so far.

## Visuals
No screenshots or other visuals are in the project yet.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
It comes with [MIT License](https://github.com/hermag/DevOpsTrainingsLab02/blob/main/LICENSE.txt).

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
