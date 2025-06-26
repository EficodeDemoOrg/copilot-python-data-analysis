# GitHub Copilot Workshop #1: Essential Recap

This document provides a condensed summary of the key concepts from the first GitHub Copilot workshop. Its purpose is to get you up to speed on the fundamental principles and features of the tool, enabling you to participate effectively in our upcoming sessions.

## 1. Fundamental Concepts

To use Copilot effectively, it's important to understand these basic terms:

* **Prompt:** The question or instruction you provide to Copilot.
* **Context:** The surrounding information Copilot uses to understand your request. This includes your open files, selected code, workspace files, and chat history. The quality of your context is the most critical factor for getting good results.
* **Token:** A piece of text or code (roughly 3–5 characters) that the AI model uses to process your prompt. A model's "context window" is the maximum number of tokens it can consider at one time.

## 2. Managing Context: The Key to Quality Results

Copilot's "awareness" is defined by its context window. Forgetting this is the most common reason for poor-quality responses.

**What goes into the context?**
Copilot automatically gathers context from several sources, including:
* An indexed version of your open workspace
* The files you have open in your IDE
* Your cursor position within a file
* Highlighted segments of code
* Your chat history and current prompt
* System instructions and custom instruction files

**Why it matters:**
The context window is finite. If you have many irrelevant files open, they can "pollute" the context, pushing out more relevant information and leading to generic or incorrect suggestions.

**Best Practice:**
Actively manage your context. Before asking a complex question, close irrelevant files. When you need Copilot to focus on specific information, provide it explicitly using `#file:` or `@workspace` to ensure it's prioritized.

## 3. The Difference: AI Assistant vs. AI Agent

Understanding this distinction is key to using the right tool for the job.

* **AI Assistant (You are in control):** Think of this as an expert junior developer at your side. You are the driver. It responds to your specific requests, explains code, generates snippets, and completes well-defined tasks. It excels at the work that precedes implementation: understanding, planning, and learning.
    * **Features:** Code Completion, Inline Chat (`Cmd+I`), Ask Mode, Edits Mode.

* **AI Agent (You delegate the work):** Think of this as a senior colleague to whom you can delegate a complete task. You define the high-level goal, and the agent plans and executes the necessary steps. It can interact with your files, run tools, and iteratively solve problems based on the results.
    * **Feature:** Agent Mode in the Chat View.

## 4. How to Interact with Copilot: Key Commands

In the VS Code Chat, there are three primary symbols you will use to communicate your intent clearly.

| Symbol | Name | Purpose & Use Case |
| :--- | :--- | :--- |
| **`@`** | **Participants** | Specifies the "domain expert" or broad context for your query. Key examples are `@workspace`, `@vscode`, and `@terminal`. |
| **`/`** | **Commands** | Declares your *intention*. These are shortcuts for specific instructions. The most important are `/explain` and `/help`. |
| **`#`** | **Variables** | Provides an *explicit reference* to a specific item, so Copilot doesn't have to guess what's important. You can reference a `#file:`, `#symbol:`, or `#selection`. |

## 5. Understanding Copilot Usage: Choosing the Right Model

Every time you send a prompt to Copilot, the service intelligently routes this **request** to the most appropriate AI model. Your choice of model is determined by the task's complexity, and this choice has implications for speed, intelligence, and the consumption of your subscription's "Premium Request" allowance.

### The Trade-off: Speed vs. Intelligence

Generally, AI models exist on a spectrum:
* **Faster Models:** Are more economical and provide rapid responses, making them ideal for tasks like autocompleting code or answering simple, factual questions.
* **More Intelligent Models:** Possess superior reasoning capabilities, allowing them to tackle complex architectural problems, analyze entire codebases, and generate more nuanced solutions. These models are computationally more expensive and have higher latency.

### Premium Request Multipliers

The "cost" of a request is measured by a **Premium Request multiplier**, which serves as a price indicator for the model's computational power. Your subscription includes a monthly pool of these request units.

* **You don't choose the model directly.** Copilot selects it for you based on your prompt.
* A simple task might use a model with a **low multiplier (e.g., 0 or 1)**, consuming few or no units.
* A complex `@workspace` query will automatically use a powerful model with a **high multiplier (e.g., 10 or 50)**, consuming more units.

The incentive is to match your workflow to the task. For a simple question, get a fast answer. For a difficult problem, Copilot automatically leverages its best resources for you.

For the exact multipliers of each model, you can refer to the official documentation:
* **[Understanding and Managing Premium Requests in Copilot](https://docs.github.com/en/copilot/managing-copilot/understanding-and-managing-copilot-usage/understanding-and-managing-requests-in-copilot#examples-of-premium-request-usage)**
* **[Choosing the Right AI Model for Your Task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task)**

### An Important Note on Agent Mode and Tool Use

Here is a key detail about how requests are counted:
> A request happens every time you type a prompt and send it.

Crucially, when you use Agent Mode for a complex task, the agent might decide to use its internal tools multiple times (e.g., read a file, search the workspace, then edit another file). **This entire chain of thought and tool usage is part of fulfilling your single, initial prompt.** The individual tool invocations by the agent do **not** consume additional Premium Requests.

This makes Agent Mode a very efficient way to solve complex problems.

## 6. Building Advanced Workflows

You can move beyond single prompts by chaining concepts and models together to solve complex problems.

* **Prompt Chaining:** This is the technique of using the output from one prompt as the input for the next. This allows you to break down a large problem into a series of manageable steps.
    * **Example Workflow:**
        1.  **Prompt 1 (Ideation):** `@workspace Suggest 3 ways to improve the performance of this function.`
        2.  **Prompt 2 (Specification):** `Based on suggestion #2, create a detailed technical specification in markdown for implementing a caching layer.`
        3.  **Prompt 3 (Implementation):** `Using the spec in #file:spec.md, generate the Python code for the caching module.`

* **Model Chaining:** For complex problems, you can use a powerful model for planning and a faster model for execution. For example, use a model with high reasoning capabilities to generate a technical specification, then switch to a faster model for generating the code based on that clear spec.

## 7. Guiding the AI: The Role of Instruction Files

To ensure consistency and provide a persistent "memory" for your project, you can use custom instruction files.

* **File:** `.github/copilot-instructions.md`
* **Purpose:** This file acts as a permanent set of guidelines for Copilot within your repository. Its contents are automatically added to the context for relevant queries.
* **Use Cases:**
    * **Enforce Coding Standards:** "Always use the `logging` module instead of `print()` statements."
    * **Define Architectural Patterns:** "When creating a new API endpoint, it must be added to an `APIRouter` in the `app/api/` directory, not in `main.py`."
    * **Guide Agents:** Provide high-level principles for agents to follow, ensuring their output aligns with your project's conventions.

This file is a powerful tool for guiding both Assistant and Agent modes and scaling best practices across a team.

## 8. Your Next Steps: Hands-On Exercises

The most effective way to learn is by doing. We have prepared two repositories for you.

**1. For Late-comers & Beginners (Recommended Starting Point):**

If you missed the first session, please start here. This project is simpler and the exercises are designed to teach the fundamental commands.

* **Starting Repository:** [https://github.com/EficodeDemoOrg/copilot-python-weather-cli](https://github.com/EficodeDemoOrg/copilot-python-weather-cli)
* **Exercises:** Follow the instructions in the `Copilot-Exercises.md` file in that repository.

**2. Main Workshop Project:**

This is the project we will use in our next group session. After you are comfortable with the basics from the weather-cli app, you can move on to these exercises.

* **Main Repository:** [https://github.com/EficodeDemoOrg/copilot-python-data-analysis](https://github.com/EficodeDemoOrg/copilot-python-data-analysis)

Inside the `exercises` directory of this repository, you will find distinct paths for different skill levels, allowing you to choose between using Copilot as an AI assistant or delegating work to the agent.

## 9. Further Reading

To deepen your understanding, we recommend these external resources:

* **Official VS Code Documentation:** [VS Code Copilot Features](https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features)
* **Understanding the Value:** [Is GitHub Copilot Worth It? (getdx.com)](https://getdx.com/blog/copilot-worth-it/)
* **Advanced Prompting Technique:** [Prompt Chaining Guide](https://www.promptingguide.ai/techniques/prompt_chaining)