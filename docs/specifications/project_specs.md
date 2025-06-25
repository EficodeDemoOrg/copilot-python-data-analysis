# Project Specification: Codebase Insights Analyzer MVP

## 1. Project Goal

To create a simple, full-stack web application that visualizes data from the Stack Overflow 2023 Developer Survey. The application will serve as the starting point for a GitHub Copilot training session. This MVP version will read data directly from a local CSV file and display it on a frontend chart.

## 2. Technology Stack

* **Backend:** Python 3.10+ with FastAPI
* **Data Handling:** Pandas
* **Web Server:** Uvicorn
* **Frontend:** HTML5, JavaScript (ES6+), Chart.js
* **Dependency Management:** `pip` with `venv` and a `requirements.txt` file
* **Testing:** Pytest

## 3. Project Structure

```
python-fullstack/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   └── survey_results_public.csv
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── templates/
│       └── index.html
│
└── tests/
    ├── __init__.py
    └── test_main.py
```

## 3. Data Source

* **Source:** [Stack Overflow Developer Survey 2023 on Kaggle](https://www.kaggle.com/datasets/stackoverflow/stack-overflow-2023-developer-survey)
* **File:** Download the `survey_results_public.csv` file.
* **Action:** Place this file inside a `/data` directory within the project.


## 4. Core Component Specifications

### 4.1. Backend (`app/main.py`)

* **Framework:** FastAPI
* **Objective:** Create a web server that serves the frontend and provides a single data API endpoint.

**Endpoints:**

1.  **Root Endpoint (`/`)**
    * **HTTP Method:** `GET`
    * **Description:** Serves the main frontend page (`index.html`).
    * **Implementation:** Use a `FileResponse` or `HTMLResponse` from `fastapi.responses` to return the contents of `app/templates/index.html`.

2.  **Data Endpoint (`/api/languages/popular`)**
    * **HTTP Method:** `GET`
    * **Description:** Analyzes the survey data to find the top 10 most used programming languages and returns them.
    * **Logic:**
        1.  Use Pandas to read the `data/survey_results_public.csv` file.
        2.  Access the `LanguageHaveWorkedWith` column.
        3.  The data in this column is a single string with languages separated by semicolons (e.g., "HTML/CSS;Python;Rust"). The code must parse these strings for each respondent.
        4.  Count the occurrences of each individual language.
        5.  Identify the top 10 most frequent languages.
    * **Response Body Schema:** Return a JSON object with two keys: `labels` (an array of language name strings) and `values` (an array of their corresponding counts).
        ```json
        {
          "labels": ["Python", "JavaScript", "HTML/CSS", ...],
          "values": [50000, 48000, 45000, ...]
        }
        ```

### 4.2. Frontend (`app/templates/index.html`)

* **Objective:** A single-page application to display the language popularity data.

**Structure:**

1.  **HTML Boilerplate:** A standard HTML5 structure.
2.  **Title:** Set the page title to "Developer Insights".
3.  **Heading:** An `<h1>` element with the text "Most Popular Programming Languages 2023".
4.  **Chart Canvas:** A `<canvas>` element with a specific `id` (e.g., `languageChart`). This is where Chart.js will render the chart.
5.  **Script Includes:**
    * Include **Chart.js** via a CDN link: `<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>`
    * Include a `<script>` block for the application's custom JavaScript.

**JavaScript Logic (within the `<script>` block):**

1.  Use the `fetch()` API to make a `GET` request to the `/api/languages/popular` endpoint when the page loads.
2.  Once the data is received, parse the JSON response.
3.  Get the `<canvas>` element by its ID.
4.  Use the `labels` and `values` from the API response to create a new Chart.js instance.
5.  Render a **bar chart** displaying the top 10 languages and their usage counts.

### 4.3. Dependencies (`requirements.txt`)

The file must contain:
For the web server
fastapi
uvicorn[standard]

For data handling
pandas

For testing
pytest
requests

## 5. Testing Structure and Plan

### 5.1. Test Directory (`tests/`)

* All tests should reside in the `tests/` directory to keep them separate from the application code.

### 5.2. Test Plan (`tests/test_main.py`)

* **Objective:** Create basic unit tests for the FastAPI application to ensure the API endpoint is working as expected.
* **Framework:** Use `pytest` and FastAPI's `TestClient`.

**Tests to Implement:**

1.  **Test API Endpoint Status Code:**
    * **Name:** `test_popular_languages_status_code`
    * **Action:** Send a `GET` request to `/api/languages/popular`.
    * **Assertion:** Assert that the HTTP status code is `200` (OK).

2.  **Test API Response Structure:**
    * **Name:** `test_popular_languages_response_structure`
    * **Action:** Send a `GET` request to `/api/languages/popular` and parse the JSON response.
    * **Assertions:**
        * Assert that the response body is a dictionary.
        * Assert that it contains a key named `labels`.
        * Assert that it contains a key named `values`.
        * Assert that the value of `labels` is a list.
        * Assert that the value of `values` is a list.

3.  **Test API Response Data:**
    * **Name:** `test_popular_languages_data_length`
    * **Action:** Send a `GET` request to `/api/languages/popular`.
    * **Assertion:** Assert that the `labels` list and the `values` list both contain exactly 10 items.