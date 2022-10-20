# Online Bookstore App


![Book Store First Page Look](https://drive.google.com/file/d/1RMog3AXkeklJwx4wmYZKuqVgy1fJOMeE/view?usp=sharing) 

<details>
<summary>
More screenshots
</summary>

![Bokstore demo](https://drive.google.com/file/d/1b4YlAG_tYLVfyAKfisIc6u4OkU7pe2q_/view?usp=sharing)
![Bookstore debugger demo](https://drive.google.com/uc?export=view&id=1Nwz642ORdTCd6KdsaN28Tt142K3wH-pt)
##### For the best experience, please use a device with a width of at least 350px


</details>
## About the app

This app is based on the book Django for Professionals by William vincent.
I have learned the following by developing the app based on the book.

* How to use Docker in Django
* How to implement test driven development in django 
* How to integrate Postgres Sql in Django  
* How to optimize app performance using django-debug-toolbar
* How to implement security features before deployment

## Built using:
- Python with Django framework and Jinja templating language
- Docker

## Getting started:
- Clone this repository or fork it
    - To clone this repository type git clone `https://github.com/Henoker/bookstore.git` on your command line
    - To fork this repository, click fork button of this repository then type git clone `https://github.com/<your username>/bookstore.git`
- Install all the dependencies of this project by typing `docker-compose up -d --build ` on the command line
- configure your Postgres Databse 
- Migrate the database by typing `docker-compose exec web python manage.py makemigrations accounts` on the command line
- Run the project locally by typing `docker-compose exec web python manage.py runserver` on the command line
    - NB: to run it on your local network, type `python manage.py runserver 0.0.0.0:8000`
- You project will be accessible in your localhost or local network.


## License
Distributed under the [MIT](https://github.com/Henoker/bookstore/blob/master/LICENSE) License. See [`LICENSE`](https://github.com/Henoker/bookstore/blob/master/LICENSE) for more information.

## Contact
- Henock Beyene Testfatsion - [hennybany@gmail.com](mailto:hennybany@gmail.com)
- Project link: https://github.com/Henoker/bookstore

## Love my effort?

<a href='https://www.linkedin.com/in/henock-beyene-tesfatsion-921ba54b/' target='_blank'><img height='35' style='border:0px;height:34px;' src='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Ffree-icon%2Flinkedin_174857&psig=AOvVaw2bZ1EFAdHHLsRolYrURA8q&ust=1666373482250000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCJDc-Y2r7_oCFQAAAAAdAAAAABAE' border='0' alt='Hire me at LinkedIN' />