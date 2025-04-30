# ENVOApp: Your Guide to Environmental Sustainability 🌍

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

ENVOApp is an interactive application designed to empower users with the knowledge and tools to make informed, eco-conscious choices in their daily lives. Whether you're a seasoned environmentalist or just starting your sustainability journey, ENVOApp offers something for everyone.

## Features

*   **🎮 Environmental Knowledge Quiz:** Test your understanding of environmental issues with an engaging and interactive quiz. Receive personalized feedback and identify areas for further learning.

*   **🌿 Eco-Friendly Alternatives:** Explore a curated list of common household items and discover sustainable alternatives. Learn about their environmental impacts and get practical tips for making the switch.

*   **💬 EcoBot:** Get instant answers to your sustainability questions with our AI-powered EcoBot! Ask about climate change, recycling, eco-friendly habits, and more.

## Technologies Used

*   **Streamlit:**  For creating the interactive web application.
*   **Google Gemini API:**  For powering the EcoBot's natural language understanding and response generation.
*   **Python:** The core programming language.
*   **Libraries:**
    *   `google-generativeai`: For interacting with the Gemini API.
    *   `streamlit`: For the web interface.
    *   `quiz_data.py`: Static quiz questions.
    *   `eco_alternatives.py`: Static eco-alternative data.
    *   `ecobot_data.py`: Static responses and data for the EcoBot.
    *   Additional common libraries such as `requests`, `pandas`, `numpy`, and `more` are included for general purpose functionalities.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone [YOUR_GITHUB_REPO_URL]
    cd ENVOApp
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your Google Gemini API key:**

    *   Obtain a Gemini API key from Google AI Studio: [https://ai.google.dev/](https://ai.google.dev/)
    *   In the main app.py search `GOOGLE_API_KEY` and enter your api key

    ```python
    GOOGLE_API_KEY = "   "  # Enter your API key here
    ```

5.  **Run the Streamlit app:**

    ```bash
    streamlit run ENVOApp.py
    ```

## Usage

1.  Open your web browser and navigate to the URL displayed by Streamlit (usually `http://localhost:8501`).
2.  Explore the three tabs: "🎮 Quiz", "🌿 Eco-Alternatives", and "💬 EcoBot".
3.  Follow the instructions within each section to test your knowledge, discover alternatives, and get answers to your sustainability questions.
