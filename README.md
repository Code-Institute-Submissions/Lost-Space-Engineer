# Lost Space Engineer

Lost Space Enigneer is a text based adventure game where the player explores a ship and fixes system and collects tools. The game finishes when the player fixes all the systems and heads to the command center.

To visit the live version of the site (hosted by Heroku) click [here](https://lost-space-engineer.herokuapp.com/)


## User Stories
- As a user, I would like to be able to choose a direction
- As a user, I would like to be able to store tool in an inventory system
- As a user, I would like to have tools with durability


## UX

### Wireframes and Designs

Below are a couple of screenshots of flowcharts created for this project.

![Game Start](/documentation/flowcharts/game-beginning.png)

![System Room](/documentation/flowcharts/sub-system-logic.png)

![Tool Room](/documentation/flowcharts/tool-room.png)


## Features 

Below are a list of key features and future features.

### Existing Features


### Features Left to Implement


## Technologies Used

During development of the site a number of programs and web based applications were used. You can find a list of the below:

[Lucidcharts](https://www.lucidchart.com/pages/) - Used to create the Flowcharts

[Github](https://github.com/) - Used to host the project

[Gitpod](https://www.gitpod.io/) - Used as a cloud based IDE to code the project

[GIT](https://en.wikipedia.org/wiki/Git) - Used for version control

[Heroku](https://www.heroku.com/) - Used to host the deployed site

[Promp Toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/)

Code that was used to develop this site are:

[Python](https://www.python.org/)


## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

 The site was deployed to Heroku. The steps to deploy are as follows: 
 - We need to install everything in the requirements.txt file. To do this we run the following command 
 
    ```pip3 install -r requirements.txt```
 - Login to Heroku and on the dasboard click New and then click Create new app
 - Give the App a name and select your region, then click create app
 - Click settings and then click Reveal config Vars. This is where we need to set a couple of things.
 - In the Key box enter PORT and in the value enter 8000
 - Next we need to add 2 buildpacks. One for python and one for nodejs. Please note that they need to be in an order. python needs to be at the top of the list with nodjs below.
 - Click deploy from the menu at the top, then click github.
 - enter the repositry name and click search. If found the repositry will appear below, click connect.

[Link to deployed site](https://lost-space-engineer.herokuapp.com/)

### Local Deployment

If you would like to make a clone of this repository, you can type the following command in your IDE terminal:

- `git clone https://github.com/robcole-dev/Lost-Space-Engineer.git`

Alternatively, if using Git pod, you can click below to create your own workspace using this repository.

[![Open in Git pod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/robcole-dev/Lost-Space-Engineer)

Please make sure to install the requirements using ```pip3 install -r requirements.txt``` in your terminal

## Credits 

### Content

[Prompt Toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/)

[Pygothem 2019](https://youtu.be/TjUTaFcxXYo)

### Acknowledgments

- Tim (Mentor)
- Mihaela (Wife)