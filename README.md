# Restaurant Rating Site

This is a project that I worked on for a class about web applications and Django

## Author

Connor Warner

## Description

This is a Django Web Application used to keep track of restaurant ratings and reviews.

Models will include the User Model, a Restaurant Model, and a Review Model.

Restaurants can only be added by a superuser via the admin while logged in users can create reviews & ratings for the restaurants

Users have the ability to sign up, login, and logout to use the site.
Regular users (and superusers) can see a list of restaurants, a list of reviews for a specific restaurant, as well as add, update, and delete reviews for a restaurant.

The site makes use of bootstrap to better stylize it.

Tests for the site views check that the view exists at the correct url with the correct content.
Tests for the models check that the behaviors for the models all behave properly.

The site includes the required files and settings for publishing the site using Heroku.


## Database ERD
![Database Entity Relationship Diagram](https://barnesbrothers.ddns.net/cis218/assignment_images/assignment_3/cis218_assignment_3_erd.png "Databse Entity Relationship Diagram")


## Outside Resources Used

None

## Known Problems, Issues, And/Or Errors in the Program

None
