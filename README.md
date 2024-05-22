# Swedish Dishes
Welcome to Swedish Dishes, a restaurant website that offers a unique culinary experience with a focus on traditional and modern Swedish cuisine. This project showcases the menu, allows customers to book a table, and provides information about the restaurant.

The live website can you find here! - https://my-project-4-524b015374ef.herokuapp.com/




## Swedish Dishes is a web application designed to enhance the dining experience by providing an easy-to-navigate platform where users can explore the menu, learn about the restaurant, and make reservations.

![hero Img ](../Projket-4/myapp/static/myapp/img/Hero-img%20Swedish.JPG.jpg)

# Features
- Menu Display: View a variety of dishes offered at Swedish Dishes, complete with descriptions and seasonal ingredients. Wich you can get to by pressing "Meny" will open a PDF 
 ![hero Img ](../Projket-4/myapp/static/myapp/img/meny%20swedish.JPG)
- Table Booking: Users can book a table by providing their details and selecting a date and time.
 ![alt text](../Projket-4/myapp/static/myapp/img/book%20table%20swedish.jpg)

- Login system ![alt text](../Projket-4/myapp/static/myapp/img/nav-swedish.JPG)
Wich is nessecary to book a table at our resturant that will pop up after you login. 

- Error with booking 
I put in a 15 minuter timer wich makes it impossible to book a table 18:00 and somelse comes and book 18:10 or 17:46 so there wont be to many orders at the same time. 
![alt text](image.JPG)

- Responsive Design: The website is designed to be fully responsive and user-friendly across different devices.

## Admin panel
- As admin you are able to see how many are coming and who is the person that booked the table. 
### NEWS!
As an admin you are able to write and update the news on your website with a text and a picture wich will be showed in the bottom of the website
![alt text](img/News%20swedish.JPG)


## Technologies Used
- Frontend: HTML, CSS, JavaScript, Bootstrap 5
- Backend: Django
- Database: SQLite (for development), PostgreSQL (for production)
- Hosting: Heroku
- Static and Media Files: Cloudinary
## Setup and Installation

1. I Linked my heroku to my rep from github 
2. Put in the config vars for Cloudinary, database and secret key 
3. I ran "Deploy bransch" 
4. And then the program was online.  

# Admin panel 
If you want to take a look at the admin panel go to this link https://my-project-4-524b015374ef.herokuapp.com/admin/
- And use the username *** and password **(You will find these inside the submission form)
1. Firt you will see inside "MYAPP" Customer and News. 
2. Customer is the bookings 
3. News is where you can upload images to the "NEWS" 


# Cred 
Shoutout to https://www.youtube.com/@TechWithTim for helping me understand the fundimentals with the diffrence between "project" and "app" 
He helpt me alot with the fundimentals on how django is built. 

# Bugs 

There are an really annoying bug that I haven't been able to fix yet wich is with Cloudinary. For some reason the images that lay inside the "static" file doesnt load
but the images for "news" does. I had a bug where nothing from the static file loaded like the css but i fixed that. 

I am looking at designing the login and logout sites, but i used a template from a command i dont remember. But it made a laborinth for me. If you are intrested in what i mean with laborinth take a look at "templates" and "allauth" & "account" 

# Sheers! 
