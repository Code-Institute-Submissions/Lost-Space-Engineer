# Lost Space Engineer

Lost Space Enigneer is a text based adventure game where the player explores a ship and fixes system and collects tools. The game finishes when the player fixes all the systems and heads to the command center.

To visit the live version of the site (hosted by Heroku) click [here](https://lost-space-engineer.herokuapp.com/)


## User Stories
- As a user, I would like to be able to choose a direction
- As a user, I would like to be able to store tool in an inventory system
- As a user, I would like to have tools with durability
- As a user, I would like to have objectives to complete the end game

## UX

### Wireframes and Designs

Below are a couple of screenshots of flowcharts created for this project.

![Game Start](/documentation/flowcharts/game-beginning.png)

![System Room](/documentation/flowcharts/sub-system-logic.png)

![Tool Room](/documentation/flowcharts/tool-room.png)

![Game Map](/documentation/flowcharts/game-map.jpg)


## Features 

Below are a list of key features and future features.

### Existing Features
- __First Load__
    - The user is prompted with a welcome message.
    - The user is asked to type play when they are ready to enter the game.

    ![Welcome Message](/documentation/readme/welcome-message.png)

- __Input Validation__
    - When the user enters a word the system doesn't recognise it prompts the user with a warning

    ![Validation](/documentation/readme/input-validation.png)

- __Inventory__
    - While explore the game the user can find tools and place them in their inventory

    ![Inventory 1](/documentation/readme/inventory.png)
    
    ![Inventory 2](/documentation/readme/inventory-slots.png)

- __Objectives__
    - There are 4 objectives to repair before the user can complete the game

    ![Objectives](/documentation/readme/objectives.png)

### Features Left to Implement
- __Scenario based Messages__
    - Currently there are standard messages for each stage. I want to add messages that give the game more depth based on objectives being completed.

- __Enermies (NPC)__
    - Currently the game only has objectives to complete. I want to add NPCs to the game which the user has to defeat to progress

- __Health__
    - Currently there is no health in the game. I want to add this in conjunction with enermies as they will be able to inflict damage to the player.


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

## Data Model

### Classes

- __Inventory__
    - This class looks after the inventory within the game. 
    - There is a function to add items to the inventory, this is also used to modify items. 
    - There is a function to print the inventory and what is in each slot.
    - There is a function to return the values of the item name and durability.
    - Then there is the __iter__ and __next__ which enables the class to be iterable.

```
class Inventory(object):
    """
    Stores the Tools in 6 slots.
    This also has functions to add items to the inventory,
    print an inventory list
    """
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.slot] = item

    def __str__(self):
        out = '\t'.join(['slot', 'Name', 'Dur'])
        for item in self.items.values():
            out += '\n' + '\t'.join([str(x) for x in
                                    [item.slot, item.name, item.durability]])
        return out

    def tool_status(self, tool):
        for item in self.items.values():
            if item.slot == tool:
                return item.name, item.durability
            else:
                continue
            raise StopIteration

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.items.values():
            if item.name == "empty":
                return item.name, item.slot
            else:
                continue
            raise StopIteration
```
- __Items__
    - This is a simple function that the Invetory Class calls on to Add, modify and print the items in the inventory

```
    class Item(object):
    """
    Class for defining the Tools atributes (Slot number, Name, Durability)
    """
    def __init__(self, slot, name, durability):
        self.slot = slot
        self.name = name
        self.durability = durability
```
- __Sub Systems__
    - The SubSystem class controls the 4 objectives in the game.
    - This controls the status of each objective

```
    class SubSystem:
    """
    Class to store the sub system
    It stores System, Power Status and Fixed Status
    """
    def __init__(self, system, power, fixed):
        self.system = system
        self.power = power
        self.fixed = fixed

    def system_status(self):
        if self.fixed is False:
            return False
        else:
            return True

    def power_change(self, system, power):
        if power is True:
            print(f"{system} is currently online and doesn't need repairing")
        else:
            self.power = True
            print(f"{system} is coming online")

    def repair(self, fixed):
        if self.fixed is True:
            print("System is currently in working order")
        else:
            self.power = True
            self.fixed = True
```



## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The site was deployed to Heroku. The steps to deploy are as follows: 
- We need to install everything in the requirements.txt file. To do this we run the following command 
 
    ```pip3 install -r requirements.txt```
- 
- Login to Heroku and on the dasboard click New and then click Create new app
- Give the App a name and select your region, then click create app
- Click settings and then click Reveal config Vars. This is where we need to set a couple of things.
- In the Key box enter `PORT` and in the value enter `8000`
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