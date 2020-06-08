<h1 align="center">
  A Django-based Blog
</h1>

<h2> Summary </h2>

A fully featured blog created using the Django framework 

<h2> Technologies </h2>

* Django web framework
* Bootstrap

<h2> Application Features </h2>

- Home page designed to display all blog posts submits by the users of the application
- User registration page for users to sign up
- User login page for users to sign into the app
- Ability for logged in users to create, update and delete blog posts
- User posts page to display all blog users by a user
- User profile page where users can update their username, email or profile picture
- Password reset page to provide valid users with the ability to reset password
- Pagination to limit posts on the home page to a certain number

<h2> Techinal Details</h2>

<h3> Project Structure </h3>
The project is split into two apps, blog and users.

The blog app deals with post creation, updates and deletes. It is in charge of displaying all blog posts on the home page as well
posts by specific users.

The users app deals with new user registration and user profile creation.

<h3> Views </h3>

The blog app makes use of generics view from Django. Generic class-based views like ListView, DetailView, CreateView, UpdateView 
and DeleteView are to perform CRUD (create, read, update and detail) operation.

The user app makes use of function-based views to render the login and profile pages.

<h3> Authentication </h3>

For class-based views, authenication (where required) is done using Django provided mixins such as **LoginRequiredMixing** and
**UserPassesTestMixin**

For function-based views, authenication is performed using the **@login_required** decorator.


<h2> Deployment </h2>
<h3> How to deploy in a local environment </h3>

Run the following command should the web app on **127.0.0.1:8000**

`python manage.py runserver`

<h3> How to deploy in production (onto a linux server using Linode) </h3>

Server: **Linode nanode plan**
