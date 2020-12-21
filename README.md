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


1. click the 'my account' link in the top right hand corner of the nav bar then click register in the drop down menu.
2. This will take you to the registeration page where you can fill out the information fields required to start an account.
3. Once signed in you can navigate through the store via the main nav links so you can view all products on the site. You can also do this through the search bar at the very top of the site aswell.
4. Then you can add items to your shopping bag by clicking an item and then clicking the 'add to bad' button.
5. After clicking 'add to bag' a toast will appear saying 'secure checkout'
6. This will take you to the secure checkout page where you can then add in your checkout information such as name, address and card details which are handled by STRIPE.
7. After filling out the details and submitting another toast will appear telling your order information and that an email has been sent to the accounts email address.
8. To navigate away from this click the 'judi's therapies logo in the top left corner' or any of the other nav links. The 'checkout other deals button bellow takes you to a page that has no products.

* I applied 2 test verification through Google so that emails can be sent to account holders when registering an account on the site. This can be done by making a temp email through 'https://temp-mail.org/' and registering an account.

* I have also tested the different screen sizing through development tools on the site.

# Deployment
________________________

I have deployed my site through github and heroku.

* github-master-branch-link: (https://williamhbcodeinstitute.github.io/Milestone-Project-4-Judi-s_Therapies/).
* github-link: (https://github.com/williamhbcodeinstitute/Milestone-Project-4-Judi-s_Therapies)

* Heroku-link: (https://whb-judi-therapies.herokuapp.com/)

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

* I have deployed my static and media files to the AWS bucket S3   in requirements.txt : botocore==1.19.9 : boto3==1.16.

* Changed the deployment from SQlite3 to Postgres using python3 manage.py dumpdata products > product_dump.json
* Followed by python3 manage.py loaddata product_dump
* This enabled all my media and static files to be shown on Heroku.
* During deployment I did make the mistake of pushing my Postgres info to github, but using git reset --soft HEAD in the terminal I could revoke the previous push where I had not added Postgres info. Followed by git push origin master --force which pushed everything in sinc.


## Credits

________________________

## Media

Image files stored locally.


## Acknowledgements
* Code Institute tutors,
* slack_ID : 'Akshat_Garg_mentor'
* slack_ID : 'miklos_ci '



