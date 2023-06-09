# README - Web Scraping Shopping Offers with Django

This repository contains a Django project that utilizes web scraping to gather shopping offers from various websites and displays the best offers to the user.

## Project Structure

The repository structure is as follows:

```
├── manage.py
├── shopping_offers/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── offers/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── scraper.py
│   ├── tests.py
│   └── views.py
├── static/
│   └── css/
│       └── style.css
├── templates/
│   └── base.html
└── README.md
```

- `manage.py`: Django management script for running development server and managing the project.
- `shopping_offers/`: Django project directory.
- `offers/`: Django app directory containing the main functionality for scraping and displaying offers.
- `static/`: Directory for static files such as CSS stylesheets.
- `templates/`: Directory for HTML templates used by the Django app.
- `README.md`: This file you are currently reading, providing information about the project and how to use it.

## Setup and Installation

To set up and run the project locally, follow these steps:

1. Ensure you have Python and Django installed on your system.

2. Clone the repository to your local environment:

   ```bash
   git clone https://github.com/your-username/shopping-offers.git
   ```

3. Navigate to the project directory:

   ```bash
   cd shopping-offers
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://localhost:8000` and start exploring the shopping offers.

## Usage

Once the project is set up and the development server is running, you can access the web application through your browser. The application will display the best shopping offers scraped from various websites.

Users can browse through the offers, search for specific products, and sort them based on price or relevance. They can also view detailed information about each offer and visit the original source website to make a purchase.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch to make your modifications:

   ```bash
   git checkout -b your-branch
   ```

3. Make the desired changes and improvements to the code.

4. Commit your changes:

   ```bash
   git commit -m "Description of your changes"
   ```

5. Push your changes to the remote repository:

   ```bash
   git push origin your-branch
   ```

6. Open a pull request on GitHub and provide a detailed description of your changes.

## License

This project is licensed under the [MIT License](LICENSE). Please see the `LICENSE` file for more details.

## Contact

If you have any questions or suggestions regarding this project, feel free to contact the author:

Name: Lucas Sanabria
Email: sanabrialucas97@gmail.com

Thank you for your interest in this project! We hope you find it useful for scraping shopping offers and finding the best deals.