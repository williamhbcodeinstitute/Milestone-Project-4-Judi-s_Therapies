# Judi's Therapies
________________________

This site has been designed to showcase the different therapies of the owner Judi and products offered for sale by therapist Judi.
The Products available relate to the two main therapies presented namely, reflexology and bach flower remedies.
Each product is displayed with a brief description of its uses and the price. Once selected items can be added to the
the bag and running price total will appear in the basket.

## UX
________________________

has been designed to attract users of the site to purchace relevent books and equipment to enhance their own therapie buisness.
The site enables the user to register an account then login to have their own profile. From there any purchaces made
are added to the basket and also to the profile of the user so order numbers are stored and can be viewed by the admin
and the user.

## Features
__________________

* The user is able to enter the site and from there click on the top right hand link 'My Account' gives the
user the option to register an account or login.

* By clicking register the user is taken to a register form where they will be able to fill it out to store
their information to the site for billing puproses. As a superuser I have to authenticate the users email address through the
admin panel once created. I tested this with my Tutor "Akshat_Garg_mentor" where he registered an account and I verified it
through the admin panel.

* After registering an account the user will be able to browes the products on the store and add them to the shopping bag with the
ability to, choose number of products and if product did have a size choose that also. With more time I would have
added more products with enabled to choose size but as the products on the site do not require it they have not been included.
However through the product admin you can add an item with the selection of size as an option. 

* The user will have the option to checkout through 'Toasts' messages or by pressing the secure checkout button.
all the transactions can be made through the bag app using Stripe secure payments.

* The user can not add or update products unless authenticated by the admin as a superuser.

## Technologies used
_____________________

* Django frameworks - can find all requirements installed in 'requirements.txt'
- used to create all apps for the website listing the urls, models, tests and views to enable all parts of 
the website to flow.

* Allauth - Used for all profile details including login, email, password changes and signup.

* HTML5 - Used for all templates using bootstrap loads.

* CSS3 - Used to style the bootstrap parts of the site.

* JavaScript 

### Links to libraries:

* https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js
* https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js
* https://code.jquery.com/jquery-3.4.1.min.js
* https://kit.fontawesome.com/e9c73d7092.js
* https://js.stripe.com/v3/

## Testing
________________________

* For testing I have gone through the whole process of working the flow of registering, logging in, adding item 
to bag, updating the bag to then secure checkout. I have tested this with my Mentor aswell to prove the flow and functionality of the site.

* I have also tested the different screen sizing through development tools on the site.

# Deployment
________________________

I have deployed my site through github and heroku.

* github-master-branch-link: https://williamhbcodeinstitute.github.io/Milestone-Project-4-Judi-s_Therapies/.
* github-link: https://github.com/williamhbcodeinstitute/Milestone-Project-4-Judi-s_Therapies

* Heroku-link: https://whb-judi-therapies.herokuapp.com/

## Heroku Deployment
________________________

I was able to delpoy to heroku with the following commands:
1. install heroku CLI - 'heroku login -i'
2. create requirements.txt file - 'pip freeze --local > requirements.txt'
3. create Procfile - 'echo web: python app.py > Procfile'
4. Deploy changes to Heroku using Git:

* git add .
* git commit -m ""
* git push -u heroku master

I began to deploy with AWS webservers but had trouble with change of code used on the servers as
they had changed from the video tutorials. I did however manage to get the aws buckets linked with my project 
can find the settings in requirements.txt : botocore==1.19.9 : boto3==1.16.

* I am aware that I need to deploy properly with AWS and also there are settings to do with changing the user accounts passwords,
but to time constraints this is all I can submit right now.

## Credits

________________________

## Media

Images uploaded from my computer.


## Acknowledgements
* Code Institute tutors,
* slack_ID : 'Akshat_Garg_mentor'
* slack_ID : 'miklos_ci '



