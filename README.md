# Email/SMS Spam Classifier 📧

This project is a simple tool that helps you identify spam messages in your emails and SMS texts. It's like having a smart filter that separates the important stuff from the junk!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is open-source and uses the MIT license, meaning you're free to use, modify, and share it!



## Description
This project implements an email and SMS spam classifier using machine learning techniques. It leverages NLTK for text processing, TF-IDF for feature extraction, and a Multinomial Naive Bayes classifier for prediction. The application provides an interactive user interface built with Streamlit, allowing users to input messages and receive real-time spam detection results. 🚀



## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Important Links](#important-links)
- [Footer](#footer)



## Features ✨
- **Email/SMS Spam Classification:** Accurately identifies spam messages from regular messages.
- **NLTK Text Processing:** Utilizes NLTK for tokenization, stop word removal, and stemming.
- **TF-IDF Vectorization:** Employs TF-IDF to convert text into numerical features.
- **Multinomial Naive Bayes:** Uses a Multinomial Naive Bayes classifier for efficient and reliable prediction.
- **Streamlit UI:** Provides an interactive and user-friendly interface for real-time classification. 📱



## Tech Stack 💻
- **Programming Language:** Python
- **Libraries:**
  - Streamlit
  - NLTK
  - Scikit-learn
  - Pandas



## Installation ⚙️
1.  Clone the repository:
    ```bash
    git clone https://github.com/Talha4543/Email-SMS-spam-classifier.git
    cd Email-SMS-spam-classifier
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the training script once to download NLTK data:
    ```bash
    python train.py
    ```



## Usage 🚀
1.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
2.  Open the application in your web browser (usually at `http://localhost:8501`).
3.  Enter the message you want to classify in the text area.
4.  Click the "Predict" button.
5.  View the prediction result (Spam or Not Spam). ✅



## How to Use 💡
This project can be used to filter spam messages automatically in various real-world scenarios:

- **Email Filtering:** Integrate the classifier into an email server to automatically filter spam emails.
- **SMS Filtering:** Use the classifier to filter spam SMS messages on mobile devices or SMS gateways.
- **Customer Support:** Analyze customer messages to identify and prioritize urgent issues, filtering out irrelevant spam.
- **Social Media Monitoring:** Detect spam or malicious content on social media platforms.



## Project Structure 📂
```
Email-SMS-spam-classifier/
├── app.py           # Streamlit application
├── model.pkl        # Pre-trained model
├── nltk.txt         # NLTK data
├── Procfile         # Procfile for deployment
├── README.md        # This file
├── requirements.txt # Dependencies
├── setup.sh         # Setup script
├── sms-spam-detection.ipynb # Jupyter Notebook (Exploratory)
├── spam.csv         # Dataset
├── train.py         # Training script
└── vectorizer.pkl   # Vectorizer
```



## Contributing 🤝
Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Submit a pull request. 🎉



## License 📜
This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.



## Important Links 🔗
-   **Repository:** [https://github.com/Talha4543/Email-SMS-spam-classifier](https://github.com/Talha4543/Email-SMS-spam-classifier)



## Footer 🦶
-   **Repository:** [Email-SMS-spam-classifier](https://github.com/Talha4543/Email-SMS-spam-classifier)
-   **Author:** Talha4543
-   **Contact:** [Talha4543's profile](https://github.com/Talha4543)

⭐️ Star the repository if you find it useful! Fork it to contribute! Raise issues for bug reports or feature requests. 🙏
