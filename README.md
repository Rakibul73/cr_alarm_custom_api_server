# Custom API Server for [CR Alarm](https://github.com/Rakibul73/CR_Alarm) & [CR Alarm Admin](https://github.com/Rakibul73/cr_alarm_admin)

This is a simple Flask-based API server that provides endpoints to interact with timestamp and text data. It allows you to add data using both POST and GET methods and retrieve the stored data. This can be useful for various applications, including implementing an alarm system.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)

---


## Installation

To run this API server, you need Python and Flask installed on your system.

1. Clone this repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd cr_alarm_custom_api_server
   ```

3. Install the required dependencies:

   ```bash
   pip install flask
   ```

4. Start the Flask development server:

   ```bash
   python api.py
   ```

The server should now be running at `http://localhost:5000`.

## Usage

You can interact with the API server using HTTP requests. You can use tools like `curl`, Postman, or create your own client application.

## Endpoints

### `GET /`

- Description: A simple hello world endpoint to check if the server is running.

- Example Request:

  ```bash
  curl http://localhost:5000/
  ```

- Example Response:

  ```
  Hello from Flask! it is hosted in pythonanywhere
  ```

### `GET /get_timestamp`

- Description: Get the stored timestamp and text from the previous POST request.

- Example Request:

  ```bash
  curl http://localhost:5000/get_timestamp
  ```

- Example Response:

  ```json
  {
    "timestamp": "Sat, 02 Sep 2023 10:19:51 GMT",
    "text": "Your stored text here"
  }
  ```

### `POST /add_data`

- Description: Add data to the system. It stores the provided input value and updates the timestamp.

- Example Request:

  ```bash
  curl -X POST -d "input=Your input value here" http://localhost:5000/add_data
  ```

- Example Response:

  ```json
  {
    "success": true
  }
  ```

### `GET /add_data_get`

- Description: Handle GET requests to update the timestamp and retrieve the current timestamp and stored text.

- Example Request:

  ```bash
  curl http://localhost:5000/add_data_get
  ```

- Example Response:

  ```json
  {
    "timestamp": "Sat, 02 Sep 2023 10:19:51 GMT",
    "text": "Your stored text here"
  }
  ```

---

