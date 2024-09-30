# Serverflow-UI: Simulating Load Balancing, Caching, Rate Limiting, and Scalability

This project is a web-based application that simulates and visualizes key aspects of server-side architecture, including **load balancing**, **caching**, **rate limiting**, and **scalability**. Built using Flask for the backend and HTML/JavaScript for the frontend, the app allows users to observe the effects of these concepts in real-time. The app is designed for educational purposes and includes deployment on Heroku.

## Features

- **Load Balancing**: Simulate load distribution across multiple servers.
- **Caching (using Redis)**: Cache responses to reduce load and improve response time.
- **Rate Limiting**: Limit the number of requests a user can make within a time frame.
- **Scalability**: Visualize the scaling of services by simulating server loads.
- **Real-time Visualization**: Charts and dynamic UI to display current load, cached requests, and request serving.

## Project Structure

- **Backend**: Flask, Redis (for caching), Flask-Limiter (for rate limiting), NGINX (load balancing).
- **Frontend**: HTML, CSS, JavaScript (Chart.js for real-time visualizations).
- **Deployment**: Heroku with Gunicorn (WSGI server), GitHub Actions for CI/CD.

## Screenshots

<!-- Add a link or upload screenshots here -->

## Prerequisites

- Python 3.9+
- Redis (for caching)
- Git
- Heroku CLI (for deployment)
- GitHub Actions (for CI/CD)

## Installation

1. **Clone the repository:**

    ```bash
    git clone git@github.com:yourusername/load_tester.git
    cd load_tester
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Redis locally (if not using Heroku Redis):**

    Install Redis by following the instructions for your operating system [here](https://redis.io/download).

5. **Create a `.env` file for environment variables:**

    ```bash
    touch .env
    ```

    Add the following:

    ```bash
    REDIS_HOST=localhost
    REDIS_PORT=6379
    ```

6. **Run the application:**

    ```bash
    flask run
    ```

7. **Access the app:**

    Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Deployment

### Deploy to Heroku

1. **Set up Heroku CLI** and log in:

    ```bash
    heroku login
    ```

2. **Create a new Heroku app**:

    ```bash
    heroku create your-app-name
    ```

3. **Set up Redis on Heroku**:

    ```bash
    heroku addons:create heroku-redis:hobby-dev
    ```

4. **Deploy using Git:**

    ```bash
    git push heroku main
    ```

5. **Open your deployed app:**

    ```bash
    heroku open
    ```

### CI/CD with GitHub Actions

1. **Set up GitHub Actions** by creating a `.github/workflows/deploy.yml` file for automated deployment.

2. Add your **Heroku API key** as a secret in your GitHub repository under **Settings → Secrets → Actions → HEROKU_API_KEY**.

3. Every push to the `main` branch will trigger the deployment pipeline automatically.

## Usage

### Visualizing Load Balancing, Caching, and Rate Limiting

1. **Make a Request:**

    Go to the homepage and enter some data to simulate a request. Select whether to use caching or not.

2. **View Server Loads:**

    Check the **Server Load** section to see how the request load is distributed across simulated servers.

3. **Cached Responses:**

    If caching is enabled, responses will be cached for 10 seconds to simulate Redis caching.

4. **Rate Limiting:**

    The app limits users to 10 requests per minute, which can be observed in real-time.

### Example API Requests

- **Make a Request with Data:**

    ```bash
    http://localhost:5000/request?data=mydata
    ```

- **Check Server Load:**

    ```bash
    http://localhost:5000/load
    ```

## Contributing

Feel free to fork this repository and submit pull requests. Contributions to improve functionality or extend the project are always welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
