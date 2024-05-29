# Fitness Django Application

## Overview
This is a Django-based web application designed to help users manage their fitness routines. It provides features for tracking workouts, monitoring progress, and setting fitness goals.

## Features
- User registration and authentication
- Workout tracking
- Progress monitoring
- Goal setting

## Prerequisites
- Python 3.8+
- Django 3.2+
- Docker (optional, for containerization)

## Installation

### Using Virtual Environment
1. **Clone the repository:**
    ```bash
    git clone https://github.com/Rubesh-28/Fitness.git
    cd Fitness
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the application:**
    - Copy `fitness/settings_example.py` to `fitness/settings.py`
    - Update `settings.py` with your configuration (e.g., database settings, secret key)

5. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

### Using Docker (Optional)
1. **Build the Docker image:**
    ```bash
    docker-compose build
    ```

2. **Run the containers:**
    ```bash
    docker-compose up
    ```

## Usage
- Access the application at `http://localhost:8000`
- Log in using the superuser credentials created during setup
- Explore the features to track workouts, monitor progress, and set fitness goals

## Configuration
- **Environment Variables:** Use a `.env` file to manage sensitive data (e.g., secret keys, database credentials).
- **Database:** Configure the database settings in `fitness/settings.py`.

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please open an issue or contact me at rubeshkk28@gmail.com.

