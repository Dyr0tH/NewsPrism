CREATE TABLE IF NOT EXISTS USERS (
  Name VARCHAR(255) NOT NULL,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  bio VARCHAR(255) NOT NULL,
  profile_picture VARCHAR(255),
  PRIMARY KEY (username)
);


CREATE TABLE IF NOT EXISTS ARTICLES (
  article_id INT AUTO_INCREMENT PRIMARY KEY,  -- Auto-incrementing integer for unique ID
  article_picture VARCHAR(255),  -- Stores the article picture as textual name
  article_title VARCHAR(255) NOT NULL,
  article_description TEXT,  -- Use TEXT for longer descriptions
  published_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,  -- Automates published date
  username VARCHAR(255) NOT NULL,
  FOREIGN KEY (username) REFERENCES USERS(username)  -- Foreign key to reference USERS table
);
