# NewsPrism

NewsPrism is a web application that allows users to browse and search for news articles. The application is built using Python for the backend, with HTML, CSS, and JavaScript for the frontend. It uses MySQL as the database to store user data and article information.

## Features

- **Browse Top Headlines**: Users can view top headlines from various news sources.
- **Search**: Users can search for news articles based on keywords.
- **User Authentication**: Users can sign up, log in, and log out to access personalized features.
- **Save Favorites**: Logged-in users can save favorite articles for future reference.
- **Responsive Design**: The application is designed to work well on desktop and mobile devices.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Dyr0tH/NewsPrism.git
   ```
2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Set up MySQL database:

   - Create a MySQL database named `newsprism`, A `b` is provided for quick setup.
   - Update the database configuration in `Handlers/db_connectivity.py`.
4. Run the application:

   ```
   flask --app ./main.py run
   ```
5. Access the application in your web browser:

   ```
   http://localhost:5000/
   ```

## Contributing

Contributions are welcome! If you would like to contribute to NewsPrism, please fork the repository and submit a pull request with your changes.
