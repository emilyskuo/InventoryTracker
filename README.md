# Inventory Tracker
 
This program allows a user to keep track of an inventory of items across multiple locations, while storing the data locally on their device.
 
### Background
 
It's often hard for me to keep track of my belongings at home, let alone what I have at my boyfriend's place. Whenever I stay over, I'm always asking the questions "What do I have there already?" and "What do I need to bring this time?". To answer the second question, we've started using shared Google Keep checklists - one to track what needs to be transported from my place to his, and another to track the reverse. It works pretty well, for the most part, but there isn't an easy way to move an item from one list to another.
 
My mom splits her time between different houses, and also asks similar questions when it's time to travel. She'll often leave clothes or shoes in one place so that she doesn't need to bring them the next time she visits, but then forgets what was stored and brings duplicates.
 
Given the frequency of these two scenarios, I wanted to create a program that help keep track of what things are where, and how many of them there are.
 
### Goals
 
* View full inventory at once
* Add and delete items from the tracker
* Associate quantity and location with each item
* Update an existing item
* Store data between uses
 
This feature set is the minimum needed to make this program useful to others. The main reason to track an inventory is to be able to see all the items that exist within it, so this was definitely an important feature to include. A user needs to be able to easily add or remove items from their inventory as circumstances change - acquiring a new item or consuming an existing one. Each item within the inventory should also have an associated quantity and location for ease of tracking, and these qualities should be easy for a user to update. Lastly, the inventory should be stored to be recalled at a later point without the program constantly running.
 
### Implementation
 
Originally, I thought I would be able to program the tracker entirely in Python 3, and store data using dictionaries, but then realized that would not have allowed the user to save the inventory after closing the program. I felt this was an important feature, since having a tracker is significantly less useful if the data entered can't be recalled later. In order to achieve this goal, I learned basic MySQL so that data could be stored locally, and be available at a future time. 
 
This left me to decide how to store the attributes associated with each item (ie quantity and location). Instead of adding a new entry for each instance of a given item, I wanted to have a quantity column within the data table - that way, displaying the full inventory is cleaner and easier to read. If I have 10 pairs of socks at home, I would rather see something like `socks: 10` than 10 lines of `socks`. I considered creating separate tables within the database for each location, but ultimately decided to store location as a column, similarly to quantity. This makes updating the location of a given item simpler and faster.
 
Another implementation decision I made was regarding the display of the full inventory. I had thought about showing the full inventory as part of the welcome screen when the program starts, but felt that having the full inventory and menu items would be cluttered and less readable. Instead, I made this one of the main menu items, so it's easily accessible upon request. I also chose to show the user the full inventory when deleting or updating an item and requesting user input to make sure the correct item was being updated.
 
### Non-goals/Future Goals
 
* Ability to archive items instead of deleting
* Including timestamps for updates to the inventory
* Ability to clear the whole inventory table
* Include a way to mark items that need to be moved
* Prioritize which items should be moved first
* Indicate items on loan or borrowed and from/to whom
   * Include when they were borrowed and when they're due back
 
These are a few features I thought of when ideating that I ultimately decided not to include in the program, but would consider for future updates. I would want to conduct user interviews to understand whether these features would be useful.
 
### Constraints
 
I developed this program to submit as a technical work sample for my Hackbright scholarship application - one of the major constraints of this project was time. The time I had to work on this project coincided with my family arriving for the holidays, so I worked to ideate and program between hosting and entertaining.
 
This was also written with just a command-line interface, and no front-end interface. The database is hosted locally, rather than on a server as well, so it's difficult to collaborate on an inventory, or access it remotely.
 
### Learnings
 
This was my first "real" program, so I learned a lot through the process. There were quite a few technical skills that I needed to learn, from MySQL to using GitHub. Outside of that, I also had to learn how to organize the ideas I had into something executable. Talking and writing about my programming are also skills I need to develop further - writing this readme took more time than I would've liked, since it was hard to know what to include and how to frame it. Here's to hoping the next one goes more smoothly!