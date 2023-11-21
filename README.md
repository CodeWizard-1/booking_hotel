![Alt text](image-2.png)

<br>

[View the deployed site on Heroku](https://booking-hotel-a07bb3df7136.herokuapp.com/)
## Table Of Contents:
1. [Design & Planning](#design-&-planning)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Agile Methodology](#agile-methodology)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Database Diagram](#database-diagram)
    
2. [Features](#features)
    * [Navigation](#Navigation-bar)
    * [Footer](#footer)
    * [Home page](#home-page)
    * [add your pages](#)
    * [Login page](#profile-page)
    * [Sign up page](#signup-page)

3. [Technologies Used](#technologies-used)
4. [Libraries](#libraries-used)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Acknowledgment](#acknowledgment)

## Design & Planning:

### User Stories
User Story 1: As a website user, I want to see a list of available hotels in a selected city so I can choose one for booking.

User Story 2: As a website user, I want to see detailed information about a hotel, including photos, prices, and descriptions, to make an informed decision

User Story 3: As a website user, I want to have the ability to filter hotels by various criteria, such as price, rating, and location, to simplify my selection
User Story 4: As a website user, I want a search function to find a hotel by its name, so I can quickly locate a specific hotel

User Story 5: As a website user, I want to register an account to access additional features, such as saving favorite hotels

User Story 6: As a website user, I want the option to recover my password if I forget it, to regain access to my account

User Story 7: As a website user, I want the ability to book a hotel by selecting dates and providing necessary information

User Story 8: As a website user, I want to see a booking confirmation with order details

User Story 9: As a website user, I want to see my past booking history to keep track of and manage my reservations

User Story 10: As a website user, I want the option to cancel a hotel booking in case my plans change

User Story 11: As a website user, I want to read reviews from other guests about hotels to evaluate service quality

User Story 12: As a website user, I want to be able to like and comment to share my experience

User Story 13: As a website user, I want to add hotels to my favorites list for future consideration

User Story 14: As a website user, I want to see the total cost of my stay, including any additional expenses

User Story 15: As a website user, I want to see information about the amenities and services offered by each hotel

User Story 16: As a website user, I want to see the contact information for hotels to get in touch with them

User Story 17: As a website user, I want the ability to log in to my account using my username and password

### Wireframes

**Data base Models**


**Interface Model**
![Alt text](Home.png) ![Alt text](<Sign Up.png>)   ![Alt text](<Sign In.png>) ![Alt text](<Hotels in city.png>) ![Alt text](<Hotel description.png>)  ![Alt text](<Room description.png>) ![Alt text](Booking.png)  ![Alt text](<Success page.png>) ![Alt text](<my booking.png>) ![Alt text](<Sign Out.png>) ![Alt text](<Mobile Home.png>) ![Alt text](<Mobile Hotel description.png>) ![Alt text](<Mobile Room description.png>)    
### Agile Methodology
When working on the project using the Agile approach, I took each user story and carefully determined its significance and priority. I introduced labels to distinguish tasks by their importance.

**Definition and Planning:**

At the beginning of each iteration, I conducted planning and selected user stories for work. I identified which ones were "must-have" for the successful completion of the project and which were "could-have" or "should-have" for improving functionality.

![Alt text](label.png)


**Iteration Creation:**

Each iteration represented a specific period, usually a few days, during which I focused on completing the selected user stories.

**Applying Labels and Updating Status:**

Labels like "must-have," "should-have," and "could-have" were used to indicate the importance of the task. 

**Updating on the Kanban Board:**

The Kanban board on GitHub visualized the entire development process. Moving tasks through columns reflected their current status, from "To Do" to "In Progress," and "Done."

![Alt text](kanban.png)

**Regular Reviews and Retrospectives:**

At the end of each iteration, I conducted a review of completed work and held a retrospective to identify improvements in the process.

**Repetition:**

In the next iteration, I took new user stories, re-evaluating their priority and importance to continue the project's development.

This approach helped me effectively manage priorities and focus on important tasks in each iteration, ensuring the project progressed in the desired direction.


### Typography
Explain font you've used for your project
### Colour Scheme
Screenshoot of the colour scheme for your project
### DataBase Diagram
Image of the database diagram for your project, you can name your database models as well and how they are connected

## Features:
Explain your features on the website,(navigation, pages, links, forms, input fields, CRUD....)
## Technologies Used
List of technologies used for your project
## Testing
Important part of your README!!!
### Google's Lighthouse Performance
Screenshots of certain pages and scores (mobile and desktop)
### Browser Compatibility
Check compatability with different browsers (Firefox, Edge, Chrome)
### Responsiveness
Screenshots of the responsivness, pick few devices
### Code Validation
Validate your code HTML, CSS, JS & Python (Validate all your templates, static files, views, forms, models, urls), display screenshots
### Manual Testing user stories
Test all your user stories, you an create table 
User Story |  Test | Pass
--- | --- | :---:
paste here you user story | what is visible to the user and what action they should perform | &check;
- attach screenshot
### Manual Testing features
Test all your features, you can use the same approach 
| Status | feature
|:-------:|:--------|
| &check; | description
- attach screenshot
### Automated testing
If you created automated tests, insert screenshoots of your coverage and number of tests
## Bugs
List of bugs and how did you fix them, you can create simple table
| Bug | Fix
|:-------:|:--------|
|   |    |
## Deployment
This website is deployed to Heroku from a GitHub repository, the following steps were taken:

#### Creating Repository on GitHub
- First make sure you are signed into [Github](https://github.com/) and go to the code institutes template, which can be found [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- Then click on **use this template** and select **Create a new repository** from the drop-down. Enter the name for the repository and click **Create repository from template**.
- Once the repository was created, I clicked the green **gitpod** button to create a workspace in gitpod so that I could write the code for the site.

#### Creating an app on Heroku
- After creating the repository on GitHub, head over to [heroku](https://www.heroku.com/) and sign in.
- On the home page, click **New** and **Create new app** from the drop down.
- Give the app a name(this must be unique) and select a **region** I chose **Europe** as I am in Europe, Then click **Create app**.

#### Create a database On ElephantSQL
- Log into the [ElephantSQL](https://www.elephantsql.com/) website and click **Create new Instance**
- Enter a **Name** and keep the plan as **Tiny Turtle Free**, then **tags** field can be left blank, Select a region closest to you, I selected **EU-West-1(Ireland)** as I'm in Ireland. Then click **Review** and afterward click **create an instance**.
- On The Dashboard click on your database instance name.
- You will see the details for your database instance, in the URL section click on the copy icon to copy the database URL.
- Head over to gitpod and create a **Database URL** environment variable in your env.py file and set it equal to the copied URL.

#### Deploying to Heroku.
- Head back over to [heroku](https://www.heroku.com/) and click on your **app** and then go to the **Settings tab**
- On the **settings page** scroll down to the **config vars** section and enter the **DATABASE_URL** which you will set equal to the elephantSQL URL, create **Secret key** this can be anything,
**CLOUDINARY_URL** this will be set to your cloudinary url and finally **Port** which will be set to 8000.
- Then scroll to the top and go to the **deploy tab** and go down to the **Deployment method** section and select **Github** and then sign into your account.
- Below that in the **search for a repository to connect to** search box enter the name of your repository that you created on **GitHub** and click **connect**
- Once it has been connected scroll down to the **Manual Deploy** and click **Deploy branch** when it has deployed you will see a **view app** button below and this will bring you to your newly deployed app.
- Please note that when deploying manually you will have to deploy after each change you make to your repository.
## Credits
List of used resources for your website (text, images, snippets of code, projects....)
## Acknowledgment
Mention people who helped you with your project(mentor, colleagues...)
