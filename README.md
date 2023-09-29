# Twitter to MongoDB Web Interface

This Python project uses the Twitter API to monitor tweets addressed to Chandigarh police with specific hashtags (#chandigarhpolice, #crime, #pcr) and stores them in a MongoDB database. Authorized users can access the stored tweets through a web interface.

## Prerequisites

Before running the project, ensure you have the following:

- Python 3.x installed
- MongoDB installed and running locally
- Twitter Developer Account with API credentials

## Installation

1. Clone the GitHub repository:

   ```bash
   git clone https://github.com/your-username/twitter-chandigarh-police.git
   cd twitter-chandigarh-police
   ```

2. Install the required Python packages:

   ```bash
   pip install tweepy Flask Flask-PyMongo bson
   ```

3. Set up Twitter API credentials:
   - Replace the placeholders in the `tweepy.py` file with your Twitter API credentials:
     - `consumer_key`
     - `consumer_secret`
     - `key`
     - `secret`

4. Set up MongoDB:
   - Make sure MongoDB is running on your local machine.
   - Modify the `app.config['MONGO_URI']` in the `app.py` file if your MongoDB setup requires a different URI.

## Usage

1. Start the Twitter monitoring script:

   ```bash
   python tweepy.py
   ```

   This script continuously monitors Twitter for tweets addressed to Chandigarh police with the specified hashtags and stores them in the MongoDB database.

2. Start the web application:

   ```bash
   python app.py
   ```

   The web interface will be accessible at `http://localhost:5000`. Users can log in and view the stored tweets.

## Web Interface Features

- **Login**: Users can log in using their credentials.
- **Logout**: Users can log out of their accounts.
- **View Tweets**: Users can view tweets stored in the MongoDB database.
- **Post Tweets**: Users can post new tweets to the database.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was created by [Your Name].
- Special thanks to the [Chandigarh Police](https://www.chandigarhpolice.gov.in/) for their dedication to public safety.

If you have any questions or need assistance, please feel free to contact [Your Email Address].

Enjoy using the Twitter to MongoDB Web Interface for Chandigarh Police!
