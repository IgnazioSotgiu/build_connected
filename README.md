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
>> [Database Structure](#database-structure)  
>> [Design Choices](#design-choices)   
>> [Wireframes](#wireframes)   
>> [Technologies Used](#technologies-used)   
>> [Implemented Features](#implemented-features)  
>> [Future Features](#future-features) 
>> [Testing](#testing)  
>> [Bugs](#bugs)  
>> [Deployment](#deployment)
>> [Credits](#deployment)  
>> [Acknowledgements](#acknowledgement)

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

## Database Structure
Build Connected database is structured in 2 collections:
![Database Structure]()  

### users 
Each user record has the following fields:
* _id
* username  
* company_name
* contractor_type
* categories
* county
* country
* email  
* phone_number  
* password  

The _id field is the ObjectId given wehn a new user registers  
Contractor_type, categories, county, and country are entered selecting values from dropdown selection elements to keep values format consistent accross all records and avoid typo errors from user input.
The email value have to pass the python validator to allow the user to register.  
The phone number accepts numbers only.  
### jobs
Each jobs record has the following fields:  
* job_title  
* category  
* employer  
* contact_phone_number  
* contact_email
* county  
* starting_date  
* urgent  
* description  
* date_job_created  
* created_by  


A Single user can add multiple jobs into he jobs database  
When a user creatres a new job record the value for "created_by" and "employer" are given automatically  from the user's record (username and company name). For the construction type, categories, county and country the values are chosen from a dropdown selection to keep a consistent format accross all records. The email value have to pass the python validator in order to allow the user to create a job record. Phone number field accepts numbers as input. Starting date is selected with a data picker to keep consistent format accross all records. The field date_job_created will be given by the app with datetime.date.today().

### User Actions:
register  
log in  
add new job  
edit job  
delete job 
edit profile  
edit password  
delete profile  
contact contractor  
contact employer    
log out  
search contractors by:
* name  
* category  
* county 

search jobs by:
* employer 
* category 
* county  

## Design Choices

### Fonts  
I have chosen Roboto forn for the whole website
### Color Palette  
Color Palette image was taken with [Coolors](https://coolors.co/)  

![](./lib/static/docs/build-connected-color-palette.png) 

## Wireframes
The wireframes were done usin [Balsamiq](https://balsamiq.com/)

[First version wireframes](./lib/static/docs/first-wireframes.md)

[Final wireframes](./lib/static/docs/final-wireframes.md)


## Technologies Used  

### Languages used

* HTML to create elements in the page  
* CSS to style elements in the page  
* Python to add functionality to  the website and interaction with database  
* JavaScript to add elements functionality  

* Flask microframework
### Libraries  
* Materialize CSS to style the elements  
* Google Fonts for Roboto font  
* Font Awesome for the icons  
* JQuery
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

## Future Implementations
* As a Owner I want charge a fee to users to use the service
* As a Owner I want create a review database to allow users to rate one another and gain exposure
* As a Owner I want display reviews on users profile (rating)  

## Testing  

Validation services:
* W3C HTML validator  
[HTML Result](./lib/static/docs/html-validator-result.md)  
* W3C CSS validator  
[CSS Result](./lib/static/docs/validator-screenshots/CSS_validator.png)   
* JSHint Javascript  
[script.js Result](./lib/static/docs/validator-screenshots/js_validator_screenshots/script.js_validator.png)  
[sendEmail.js Result](./lib/static/docs/validator-screenshots/js_validator_screenshots/emailjs_validator.png)
* Python validator  
[Python result](./lib/static/docs/validator-screenshots/python_validator/python_views_validator.png)

Find the testing information in a separate file:  
[User Acceptance Test](./lib/static/docs/user-acceptance-test-build-connected.pdf)

## Bugs  
Here the bugs found during the development and testing of the website:

The following steps were used when the bug was found:

Following the steps to trigger and report the bug:

1. Give a short description of the problem
1. Steps to trigger the bug:
    1. Click the element
    1. What expect to happen
    1. What happened instead?
1. Description of the unwanted behaviour.
1. Solution found if the problem was solved  

### List of bugs found in separate file [bugs.md](./lib/static/docs/bugs.md)  

## Deployment 

## Credits  

## Aknowledgement  
