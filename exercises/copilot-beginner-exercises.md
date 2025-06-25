# GitHub Copilot Exercises: Analytics Dashboard (Beginner Track)

Welcome to the GitHub Copilot training session! This document provides a series of exercises designed to help you practice core Copilot features within our "Developer Insights Analytics Dashboard" project.

The goal for this session is to build your confidence by using Copilot as a **personal tutor** and an **intelligent assistant**. You will learn to explore a professional-grade application, understand its technologies, and make safe, guided changes.

## Introduction & Key Concepts

You may have some prior experience with Copilot. Today, we will drill those skills in the context of a real-world application. Don't worry if you aren't familiar with all the technologies used—we will use Copilot to learn about them!

**Key Copilot Interactions:**

* **Chat View:** Your primary tool for asking questions (`@workspace`), explaining code (`/explain`), and generating tests (`/tests`) or documentation (`/doc`).
* **Inline Chat (`Cmd+I` / `Ctrl+I`):** Perfect for making small, targeted edits to a selection of code without leaving the editor.
* **Code Completion:** The "autocomplete" feature that suggests code as you type.
* **Context Variables (`#`):** Used to provide specific context like files (`#file:app/main.py`) or selections (`#selection`).

## Essential Tips for Effective Copilot Usage

Apply these best practices throughout all exercises:

**Context is Critical**
- Always use `#file:` when asking about specific files
- Use `@workspace` for broad project questions  
- Combine context variables for more precise answers: `#file:app/main.py #file:tests/test_main.py`

**Iterative Learning Approach**
- Don't try to understand everything at once - ask follow-up questions
- Use `/explain` to understand code you didn't write
- Use `/tests` and `/doc` to generate supporting materials

**Efficient Editing Workflow**
- Use Inline Chat (`Cmd+I`/`Ctrl+I`) for small, targeted changes
- Use the Chat view for planning larger changes or understanding concepts
- Let autocomplete do the heavy lifting for boilerplate code

**Validation Process**
1. Make a change with Copilot's help
2. Run tests to verify nothing broke: `pytest -v`
3. Test manually in the browser if it's a UI change
4. Use `/tests` to generate new tests for your features

**Remember**: Use Copilot as your assistant, but you remain in control of your code decisions.

---

## Section 0: Understanding the Project and its Technology

**Goal:** Before changing any code, let's use Copilot to understand what this project does and the libraries it's built with. These exercises are crucial for building a foundation for the tasks ahead.

### Exercise 0.1: What is This Project?

* **Purpose:** To get a high-level understanding of the project's goals and structure.
* **Aim:** Practice using the `@workspace` participant for broad project questions.
* **Steps:**
    1.  Open the Copilot Chat view in VS Code.
    2.  In the chat input, ask Copilot for an overview:
        ```
        @workspace /explain What is the main purpose of this project? Based on the README and the code, what are the key features it provides?
        ```
    3.  Review Copilot's summary. It should mention the FastAPI backend, data analysis, and the interactive frontend.

### Exercise 0.2: Understanding the Technology Stack

* **Purpose:** To learn about the main libraries used in the project.
* **Aim:** Use Copilot as a tutor to explain unfamiliar technologies.
* **Steps:**
    1.  First, let's look at the project's dependencies. In the Copilot Chat, ask:
        ```
        #file:requirements.txt /explain What are the main libraries listed here? Briefly explain what FastAPI, pandas, and uvicorn are used for.
        ```
    2.  Now, let's dive deeper into each one. Ask Copilot a follow-up question for each technology:
        * **For the Backend:** `Based on #file:app/main.py, what is a "path operation decorator" in FastAPI (like @app.get(...))?`
        * **For Data Analysis:** `Based on #file:app/data_config.py, what is a pandas DataFrame? How is it being used to read the CSV file?`
        * **For the Frontend:** `Based on #file:app/templates/index.html, what is Chart.js? How does it create a visual chart from data?`

---

## Section 1: Exploring the Live Application

**Goal:** Now that you understand the technologies, use Copilot Chat to understand how they are connected in *this specific application*.

### Exercise 1.1: Understanding the API Layer

* **Purpose:** To see how FastAPI is used to serve data to the frontend.
* **Aim:** Practice using the `#file` variable to focus Copilot on a specific part of the application.
* **Steps:**
    1.  In the Copilot Chat view, type the following prompt to ask about the main application file:
        ```
        #file:app/main.py /explain Explain the main API endpoints in this file. How does the `/api/analysis/technology-usage` endpoint work and what parameters does it take?
        ```
    2.  Analyze the response. Copilot should detail the query parameters (`source`, `column`, `top_n`) and explain that this is the core endpoint for analytics.

### Exercise 1.2: Understanding the Frontend and API Interaction

* **Purpose:** To understand how the web interface is built and how it fetches data from the API.
* **Aim:** Ask Copilot to connect the dots between HTML structure, JavaScript, and the backend API.
* **Steps:**
    1.  Open `app/templates/index.html` so you can see the code.
    2.  In the Copilot Chat view, ask:
        ```
        #file:app/templates/index.html /explain How do the dropdown menus (like 'data-source-select') in this HTML file trigger an API call? Where in the JavaScript is the chart updated with the data from the API?
        ```
    3.  Review the explanation to understand the flow: User changes a dropdown -> `runAnalysis()` is called -> API is queried -> `createTechnologyChart()` is called.

### Exercise 1.3: Tracing a Function's Usage

* **Purpose:** To learn how different parts of the code are connected.
* **Aim:** Practice using the `#usage` variable to find where a specific function is being used.
* **Steps:**
    1.  The `data_config.py` file contains the core analysis logic. Let's find where its main function is used.
    2.  In the Copilot Chat view, type:
        ```
        #usage:app.data_config.DataManager.analyze_technology_usage /explain Where is this analysis function being called in the project?
        ```
    3.  Copilot should point you to the `/api/analysis/technology-usage` endpoint in `app/main.py`, showing you how the API layer uses the data engine.

---

## Section 2: Making Your First Changes (Guided Implementation)

**Goal:** Use Copilot's code generation and editing features to make small, visible changes to the application. This section focuses on building confidence through low-risk modifications.

### Exercise 2.1: Changing the Chart's Appearance

* **Purpose:** To make a simple, visual change to the frontend.
* **Aim:** Practice using **Inline Chat (`Cmd+I` / `Ctrl+I`)** for a targeted edit.
* **Steps:**
    1.  Open `app/templates/index.html`.
    2.  Locate the `createTechnologyChart` function in the `<script>` section. Inside it, you'll find the `new Chart(...)` block.
    3.  **Select the entire `type: 'bar',` line.**
    4.  Press `Cmd+I` (or `Ctrl+I`) to open Inline Chat.
    5.  Type the instruction: **`change the chart type to a pie chart`** and press Enter.
    6.  Copilot will suggest changing `'bar'` to `'pie'`. Accept the suggestion.
    7.  Save the file and refresh your browser. The dashboard should now display a pie chart!

### Exercise 2.2: Adding a Footer to the Page

* **Purpose:** To add a new static element to the HTML page.
* **Aim:** Practice using **Code Completion** based on comments.
* **Steps:**
    1.  In `app/templates/index.html`, scroll to the bottom of the `<body>` section, just before the closing `</body>` tag.
    2.  On a new line, type a comment:
        ```html
        <!-- Add a footer with copyright information -->
        ```
    3.  Press Enter to move to the next line. Copilot should automatically suggest the HTML code for a footer.
    4.  Accept the suggestion by pressing `Tab`. Save the file and refresh your browser to see the new footer.

### Exercise 2.3: Adding a New Filter to the Backend

* **Purpose:** To implement a small but complete feature that modifies the backend logic and the API.
* **Aim:** Practice using autocomplete and making coordinated changes across files.
* **Task:** We will add a new query parameter, `min_count`, to the `technology-usage` API to filter out technologies used by fewer than N people.
* **Steps:**
    1.  **Modify the Data Engine:**
        * Open `app/data_config.py` and find the `analyze_technology_usage` function definition.
        * Add a new parameter to the function signature: `min_count: int = 0`.
        * Inside the function, after the line `sorted_techs = sorted(tech_counts.items(), key=lambda x: x[1], reverse=True)[`, add a new line and a comment: `# Filter out technologies with a count less than min_count`.
        * Let Copilot's **autocomplete** generate the filtering logic for you. Accept it.
    2.  **Update the API Endpoint:**
        * Open `app/main.py` and find the `/api/analysis/technology-usage` endpoint function.
        * Add `min_count: int = 0` to its function signature as a query parameter.
        * Update the call to `data_manager.analyze_technology_usage` to pass the new `min_count` value through.
    3.  **Test Your Change:**
        * Run the application and open your browser to the dashboard.
        * Manually add `&min_count=20000` to the URL and press Enter.
        * Observe how the chart updates to show fewer technologies.

---

## Section 3: Documenting and Testing Your Work

**Goal:** Use Copilot to automatically generate documentation and tests for the feature you just added.

### Exercise 3.1: Generating Documentation

* **Purpose:** To quickly create developer documentation for your new feature.
* **Aim:** Practice using the `/doc` slash command.
* **Steps:**
    1.  Go back to `app/data_config.py`.
    2.  Highlight the entire `analyze_technology_usage` function that you modified.
    3.  Open the Chat View and type:
        ```
        #selection /doc Generate an updated docstring for the selected function. Make sure to describe the new `min_count` parameter.
        ```
    4.  Copilot will generate a complete docstring. Review it, then copy and paste it into your code.

### Exercise 3.2: Generating a New Test Case

* **Purpose:** To ensure your new feature works as expected and is protected against future changes.
* **Aim:** Practice using the `/tests` slash command to create a targeted unit test.
* **Steps:**
    1.  Open the Chat View.
    2.  Provide Copilot with the context of your test file and your application logic:
        ```
        #file:tests/test_main.py #file:app/main.py /tests

        Generate a new pytest function for `test_main.py`. The test should call the `/api/analysis/technology-usage` endpoint with the `min_count` query parameter set to a high value (e.g., 5000). It should verify that:
        1. The response status code is 200
        2. The response contains fewer technologies than a call without min_count
        3. All returned technology counts are >= the min_count value
        ```
    3.  Copy the generated test function into `tests/test_main.py`.
    4.  Open your terminal and run `pytest`. Your new test should now run and pass!

---

## Section 4: Bonus Exercises (Advanced Practice)

**Goal:** For learners who want to explore more advanced Copilot features and get deeper into the codebase.

### Exercise 4.1: Understanding the Data Pipeline

* **Purpose:** To trace how data flows through the entire application.
* **Aim:** Practice using multiple context variables together.
* **Steps:**
    1.  In the Copilot Chat view, ask:
        ```
        #file:app/data_config.py #file:app/main.py /explain 

        Trace the data flow: starting from when a zip file is placed in the data/ folder, how does it become available for analysis in the web interface? Include the automatic extraction, data source registration, and API availability.
        ```
    2.  Follow up with a more specific question about the data extraction process:
        ```
        #file:app/data_config.py How does the _ensure_data_extracted method work? What happens if I add a new zip file while the application is running?
        ```

### Exercise 4.2: Exploring Error Handling

* **Purpose:** To understand how the application handles edge cases and errors.
* **Aim:** Practice using Copilot to understand defensive programming patterns.
* **Steps:**
    1.  Ask Copilot about error handling:
        ```
        #file:app/main.py /explain What are all the different types of errors this API can return? How does it validate user input and handle missing data?
        ```
    2.  Look at a specific error case:
        ```
        #file:app/data_config.py What happens if a CSV file is corrupted or a required column is missing? How does the application handle this gracefully?
        ```

### Exercise 4.3: Performance Considerations

* **Purpose:** To learn about performance optimization in data analysis applications.
* **Steps:**
    1.  Ask about performance:
        ```
        @workspace What are the potential performance bottlenecks in this application when dealing with large CSV files? How could caching or optimization be implemented?
        ```

---

## Section 4: Bonus Exercises (Advanced Practice)

**Goal:** For learners who want to explore more advanced Copilot features and get deeper into the codebase.

### Exercise 4.1: Understanding the Data Pipeline

* **Purpose:** To trace how data flows through the entire application.
* **Aim:** Practice using multiple context variables together.
* **Steps:**
    1.  In the Copilot Chat view, ask:
        ```
        #file:app/data_config.py #file:app/main.py /explain 

        Trace the data flow: starting from when a zip file is placed in the data/ folder, how does it become available for analysis in the web interface? Include the automatic extraction, data source registration, and API availability.
        ```
    2.  Follow up with a more specific question about the data extraction process:
        ```
        #file:app/data_config.py How does the _ensure_data_extracted method work? What happens if I add a new zip file while the application is running?
        ```

### Exercise 4.2: Exploring Error Handling

* **Purpose:** To understand how the application handles edge cases and errors.
* **Aim:** Practice using Copilot to understand defensive programming patterns.
* **Steps:**
    1.  Ask Copilot about error handling:
        ```
        #file:app/main.py /explain What are all the different types of errors this API can return? How does it validate user input and handle missing data?
        ```
    2.  Look at a specific error case:
        ```
        #file:app/data_config.py What happens if a CSV file is corrupted or a required column is missing? How does the application handle this gracefully?
        ```

### Exercise 4.3: Performance Considerations

* **Purpose:** To learn about performance optimization in data analysis applications.
* **Steps:**
    1.  Ask about performance:
        ```
        @workspace What are the potential performance bottlenecks in this application when dealing with large CSV files? How could caching or optimization be implemented?
        ```

Congratulations! You have successfully used GitHub Copilot to understand the technologies in a professional application, explore its structure, and extend it with a new feature. You've practiced the most important commands and workflows to help you in your daily development tasks.

