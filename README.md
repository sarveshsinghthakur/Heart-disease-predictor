# Heart Disease Predictor

This project provides a machine learning model to predict the risk of heart disease based on various health parameters. It includes a Streamlit web application for easy interaction.

## Features

- Predicts the likelihood of heart disease.
- Provides a probability score for the prediction.
- User-friendly interface built with Streamlit.

## Setup Instructions

1.  **Clone the repository (if applicable):**

    ```bash
    git clone <repository_url>
    cd "Heart disease"
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    The application will open in your web browser.

## Model Information

### Input Features

The model expects the following input features:

-   `age`: Age of the patient.
-   `sex`: Sex of the patient (1 = male; 0 = female).
-   `cp`: Chest pain type (0: Typical Angina, 1: Atypical Angina, 2: Non-anginal Pain, 3: Asymptomatic).
-   `trestbps`: Resting blood pressure (in mm Hg).
-   `chol`: Serum cholestoral in mg/dl.
-   `fbs`: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false).
-   `restecg`: Resting electrocardiographic results (0: Normal, 1: ST-T wave abnormality, 2: Left ventricular hypertrophy).
-   `thalach`: Maximum heart rate achieved.
-   `exang`: Exercise induced angina (1 = yes; 0 = no).
-   `oldpeak`: ST depression induced by exercise relative to rest.
-   `slope`: The slope of the peak exercise ST segment.
-   `ca`: Number of major vessels (0-3) colored by flourosopy.
-   `thal`: Thalassemia (1: fixed defect; 2: normal; 3: reversible defect).

### Output

The model outputs a prediction indicating the risk of heart disease (0 = low risk, 1 = high risk) along with the probability.