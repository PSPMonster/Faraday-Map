# Faraday-Map

Faraday Clients Map is a Django-based web application that allows managing the locations of Faraday company's clients 📍. </br>
Website displays pins on the map representing approximate locations of homes where Faraday's heat pumps and photovoltaics have been installed 🌍. </br> </br>
The project includes two main pages: </br>
<ul>
  <li>a regular user page where pins are placed in approximate locations (without specific client data)</li>
  <li>an administrator page, accessible at /administrator after logging in, where an administrator can view, add, and remove clients based on permission status.</li>
</ul>

### 🔴 You can find live version of this project <a href="https://mapa.faraday.com.pl/">HERE</a> </br>


# Tech Stack

<p align="center">
  <img src="https://www.djangoproject.com/m/img/logos/django-logo-negative.png" width="190" height="90"/>
  <img src="https://github.com/PSPMonster/Faraday-Map/assets/63736028/7ff49e55-348a-41bb-b383-6a65de5ee37d" width="190" height="100"/>
  <img src="https://getlogovector.com/wp-content/uploads/2021/01/tailwind-css-logo-vector.png" width="190" height="100" />
</p>

# Features

<ul>
  <li>User Page:</li>
  <ul>
    <li>Pins on the map representing approximate locations of homes with installed Faraday systems.</li>
    <li>Access to general information about client locations.</li>
  </ul>

  <li>Administrator Page:</li>
  <ul>
    <li>Access to detailed client data.</li>
    <li>Ability to add new clients.</li>
    <li>Ability to remove existing clients.</li>
  </ul>
</ul>


# How to Run the Project

<ol>
  <li><b>Clone the Repository:</b></li>


  ```
  git clone https://github.com/PSPMonster/Faraday-Map.git
  cd Faraday-Map
  ```

  <li>Create and Activate Virtual Environment:</li>
  
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

  <li>Install Required Libraries:</li>
  
  ```
  pip install -r requirements.txt
  ```

  <li>Apply Database Migrations:</li>
  
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```


  <li>Run the Development Server:</li>
  
  ```
  python manage.py runserver
  ```
  
</ol>


# Notes for the Administrator
<ul>
  <li>The administrator page is accessible at /administrator.</li>
  <li>Administrators with permission level 0 can only view client data.</li>
  <li>Administrators with permission level 1 can view, add, and remove clients.</li>
</ul>

# About the project
This Customer Management System project for <a href="http://faraday.com.pl/">Faraday</a> company is a comprehensive online platform based on Django technology that enables Faraday to effectively manage its customers and maintain regular contact with them. This system was designed to streamline the company's business processes, improve customer service and increase the effectiveness of marketing and sales activities.


