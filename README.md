---
# Build Connected
---
## Website Purpose:
The aim of the website is to connect different professional subjects in the construction industry. Main contractors can register on the website and advertise jobs that need to be carried out by other professional. All users can also check contact details of particular professional to have them price a particular job. All users can add, edit, find or delete jobs that they adverise on the jobs board.
All users can register on the website and check if any job is available in their own category, they can perform a search in the jobs database to find jobs that might be available in their county. They can search jobs from a particular contractor, check if the starting time suit them. Sub contractors once find a job that they are able and interested on carrie out they can apply by sending their availability and price to the contractor that advetize the jobs thorogh the contact form on the website.
All users of the website need to register and provide contact details in order to use the service. They can also edit or delete their profile.


## Content:
>> [Website Structure](#website-structure)  
>> [User Stories](#user-stories)  
>> [Design Choices](#design-choices)   
>> [Wireframes](#wireframes)   
>> [Technologies Used](#technologies-used)   
>> [Implemented Features](#implemented-features)  
>> Future Features  
>> Testing  
>> Bugs  
>> Deployment 
>> Credits  
>> Acknowledgements

## Website Structure

The website is compose on a landing page that welcome the user. On the top of the page there is the navigation bar with the website name on the left and the user options on the right. The login and register links will be there with a third link to provide the user with a short information about the purpose of the website and the value join the of the service provided to the users. At the center of the page the main logo and name of the website with a bigger button to login/register and enter the website.
At the bottom of the main page links to linkedin and twitter accounts.
The registered user can access his/her profile page where more actions will be displayed in the navigation bar such jobs options (home, add new job, my jobs, my profile and log out). The user will be able to edit or delete only the jobs that create and can be found in my jobs page. 
The user will also be able to edit and delete his profile and submit prices for the jobs that he is interested on carry out.  

*Build Connected Website Structure*
![](./lib/static/docs/website-structure.png)

For this project two database are created one for the users (contractors database) and one for the jobs advertized. Both database are created on mongo db, for non relational database cloud storage.

## User Stories  

Find user stories in a separate document [user-stories.md](./lib/static/docs/user-stories.md)

## Design Choices

### Fonts  
I have chosen Roboto forn for the whole website
### Color Palette  
Color Palette image was taken with [Coolors](https://coolors.co/)  

![](./lib/static/docs/build-connected-color-palette.png) 

## Wireframes
The wireframes were done usin [Balsamiq](https://balsamiq.com/)

First version wireframes

- [Landing page](./lib/static/docs/wireframes/first-version/landing-page.png)
- [Home page](./lib/static/docs/wireframes/first-version/homepage.png)
- [Profile page](./lib/static/docs/wireframes/first-version/profile-page.png)
- [Log In form](./lib/static/docs/wireframes/first-version/log-in-form.png)  
- [Register form](./lib/static/docs/wireframes/first-version/register-form.png) 
- [Add Job page](./lib/static/docs/wireframes/first-version/add-job-page.png)  
- [My Jobs Page](./lib/static/docs/wireframes/first-version/my-jobs-page.png)
- [Search form](./lib/static/docs/wireframes/first-version/perform-search.png)  

Final wireframes

- [landing page](./lib/static/docs/wireframes/final-version/updated-landing-page.png)  
- [home page](./lib/static/docs/wireframes/final-version/updated-homepage.png)
- [job info page](./lib/static/docs/wireframes/final-version/job-info.png)
- [profile page](./lib/static/docs/wireframes/final-version/updated-profile-page.png)
- [edit profile page](./lib/static/docs/wireframes/final-version/edit-profile.png)  
- [delete profile page](./lib/static/docs/wireframes/final-version/delete-profile-page.png)
- [login page](./lib/static/docs/wireframes/final-version/updated-login-page.png)  
- [register page](./lib/static/docs/wireframes/final-version/updated-register-page.png)
- [my jobs page](./lib/static/docs/wireframes/final-version/updated-my-jobs.png)
- [add job page](./lib/static/docs/wireframes/final-version/updated-add-job-page.png)
- [delete job page](./lib/static/docs/wireframes/final-version/delete-job-page.png)  
- [jobs search result page](./lib/static/docs/wireframes/final-version/jobs-search-result.png)
- [user search result page](./lib/static/docs/wireframes/final-version/user-search-result.png)  
- [contact form](./lib/static/docs/wireframes/final-version/contact-form.png) 
- [change password](./lib/static/docs/wireframes/final-version/change-password.png)
- [admin dashboard](./lib/static/docs/wireframes/final-version/admin-dashboard.png)  
- [admin manage jobs](./lib/static/docs/wireframes/final-version/admin-manage-jobs.png)  
- [admin manage users](./lib/static/docs/wireframes/final-version/admin-manage-users.png)  

## Technologies Used  

### Languages used

HTML to create elements in the page  
CSS to style elements in the page  
Python to add functionality to  the website and interaction with database  
JavaScript to add elements functionality  

Flask microframework
### Libraries  
Materialize CSS to style the elements  
Google Fonts for Roboto font  
Font Awesome for the icons  
JQuery
### Tools  
* Github - Used for version control
* Gitpod.io workspace - Used to develop the project and push versions to the Github repository  
* Chrome developer tool  
* Microsoft word - For user stories and strategy plane sheets  
* Balsamiq - For wireframes  
* EmailJS - To allow contact forms to send emails  
* Sweet Alert - To display status message after the email is sent  
* Coolors - Used to create a color palette  
* Am I responsive - used to create Build Connected mockup image
* Heroku - To deploy the project online
* mongodb - To create and store no relational data  
* werkzeug.security - To secure passwords  

### Implemented Features 

* Responsive mobile first design
* Organized database data in two collections
* Created a registration form
* Created a login form
* Implemented edit and delete profile functionality
* Implemented change password functionality
* Implemented create, find, edit, delete jobs functionality
* Created contact form to contact users
* Created contact form to apply for jobs
* Created an admin dashboard to manage database
* Created message after user's actions
* Created a log out functionality
* Job apply button displayed for jobs ads from other users
* Users can modify or delete only their own entries in the page my_jobs