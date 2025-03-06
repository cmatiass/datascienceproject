# 🚀 Data Science Project - Structured ML Pipeline

## 📌 Overview
This project focuses on the proper structuring of a Data Science pipeline. It is designed to ensure modularity by breaking down different stages of machine learning workflows into separate modules. The pipeline is executed in the following stages:

1. **📥 Data Ingestion** - Collecting and loading data into the pipeline.
2. **✅ Data Validation** - Ensuring data quality and consistency.
3. **🔄 Data Transformation** - Preprocessing and feature engineering.
4. **🤖 Model Training** - Training machine learning models.
5. **📊 Model Evaluation** - Assessing model performance.

A web application (`app.py`) has been implemented to allow users to make predictions using the trained model. 🖥️

## 🎯 Project Goals
The main objective of this project is to demonstrate a well-structured Data Science workflow while maintaining a modular design. **It does not include data preprocessing or an exploratory data analysis (EDA) since the focus is solely on project structure and model deployment.** A sample dataset has been used for demonstration purposes.

## 🛠️ Steps to Set Up the Project
To replicate this project, follow these steps:

1. **📂 Create a GitHub Repository**
2. **📥 Clone the Repository Locally**, add `.gitignore`, commit changes, and push to origin.
3. **⚙️ Set Up a Conda Environment** and activate it.
4. **📦 Install Dependencies** listed in `requirements.txt`.
5. **📝 Create `template.py`** to define the folder and file structure.
6. **📜 Configure Logging** in `logs/logging.log`.
7. **🔧 Create Common Utility Functions** in `common.py`.
8. **⚙️ Configure `config.yaml`** to manage pipeline settings.
9. **🛠️ Develop Classes and Functions** for each stage in `src/datascience/components/`.
10. **🌐 Implement the Web App (`app.py`)** for real-time predictions.

## 📁 Directory Structure
```
│   .gitignore                      # Specifies files to be ignored by Git
│   app.py                          # Flask web application entry point
│   Dockerfile                      # Container definition for Docker deployment
│   generate_structure.py           # Script to generate directory structure
│   LICENSE                         # Project license information
│   main.py                         # Main entry point for the application
│   params.yaml                     # Model parameters configuration
│   README.md                       # Project documentation and overview
│   requirements.txt                # Python package dependencies
│   schema.yaml                     # Data schema definition
│   setup.py                        # Package installation script
│   struct.txt                      # Project structure listing
│   struct_files.txt                # Alternative project structure file
│   template.py                     # Template file for code generation
│
├───.github                         # GitHub specific configurations
│   └───workflows                   # CI/CD workflow definitions
│
├───artifacts                       # Generated files during pipeline execution
│   ├───data_ingestion              # Files from data ingestion step
│   ├───data_transformation         # Files from data transformation step
│   ├───data_validation             # Files from data validation step
│   ├───model_evaluation            # Files from model evaluation step
│   └───model_trainer               # Files from model training step
│
├───config                          # Configuration files
│
├───logs                            # Application logs
│
├───research                        # Jupyter notebooks for research and experimentation
│
├───src                             # Source code
│   └───datascience                 # Main package
│       ├───components              # Core ML pipeline components
│       ├───config                  # Internal configuration handling
│       ├───constants               # Constant values used across the project
│       ├───entity                  # Data entity definitions
│       ├───pipeline                # ML workflow pipelines
│       ├───utils                   # Utility functions
│       └───__pycache__             # Python cached bytecode files
│
├───static                          # Static web files
├───templates                       # HTML templates for web UI
└───venv                            # Python virtual environment
```

## 🛠️ Technologies Used
- 🐍 Python
- 🌐 Flask (for the web application)
- 🧮 Pandas, NumPy (for data processing)
- 🤖 Scikit-learn (for machine learning)
- 💾 Joblib (for model serialization)
- ⚙️ PyYAML (for configuration management)
- 📜 Logging (for application logs)
- 🐳 Docker (for containerization)
- 🛠️ **DagsHub & MLFlow** (for experiment tracking and reproducibility)

## ▶️ How to Run
To run the project locally:

```bash
# Clone the repository
git clone <repository-url>
cd <repository-folder>

# Create and activate the environment
conda create --name ds_project python=3.10 -y
conda activate ds_project

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python main.py

# Run the web application
python app.py
```

## 🌐 How to Use the Web Application
Once the application is running, follow these steps:

1. **Access the main page**: Open your browser and go to `http://127.0.0.1:8080/`.
2. **Train the model**: Navigate to `http://127.0.0.1:8080/train`. This will execute the full pipeline, from data ingestion to model training.
3. **Return to the main page**: Go back to `http://127.0.0.1:8080/`.
4. **Make a prediction**: Enter values for each variable in the form and click on the `Predict` button.
5. **View the result**: The application will redirect you to `http://127.0.0.1:8080/predict`, where the predicted outcome will be displayed.

## 📈 Experiment Tracking with DagsHub & MLFlow
All executions of the model are tracked using **MLFlow** and are accessible through the **Experiments** section of **DagsHub**. This allows users to:
- View all previous model runs and their respective parameters.
- Compare performance metrics across different executions.
- Access logs and artifacts stored from each experiment.

This ensures full transparency, version control, and reproducibility of the ML workflow. 🚀📊

## 🤝 Contribution
Contributions are welcome! Feel free to fork the repository, make modifications, and create a pull request.

---

This project serves as a template for well-structured Data Science projects, ensuring scalability and maintainability. 🚀✨

