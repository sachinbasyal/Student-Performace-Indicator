# Student-Performace-Indicator

An end-to-end MLOps project implementing a **<ML_ALGOs** to predict....

This project demonstrates a production-ready workflow using **DVC (Data Version Control)** for reproducibility, **NLTK** for advanced text processing, and a modular architecture.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Project Architecture](#project-architecture)
- [Running the Pipeline](#running-the-pipeline)
- [Inference & Prediction](#inference--prediction)
- [Pipeline Stages](#pipeline-stages)
- [Results](#results)


## Prerequisites

* **Python 3.12+** (Tested on Windows 11 with Python 3.12.7)
* **Microsoft C++ Build Tools**: Required for compiling specific Python dependencies (e.g., `ruamel.yaml` used by DVC).
    * *Install "Desktop development with C++" via Visual Studio Build Tools 2022.*


## Installation & Setup

These instructions are for **Windows (Command Prompt / PowerShell)**.

### 1. Environment Setup
Create and activate a virtual environment to keep dependencies isolated.

:: Create virtual environment

    py -3.12 -m venv .venv

:: Activate the environment

    .\.venv\Scripts\activate

### 2. Install Dependencies
Update your package tools and install the required libraries.

:: Upgrade core 

    python -m pip install --upgrade pip setuptools wheel

:: Install project requirements

    pip install -r requirements.txt


## Project Architecture

    ├── data/                           # Data Store
    │   ├── raw/                        # Original immutable datasets
    │   ├── ingested/                   # Split datasets (train.csv, test.csv)
    │   └── processed/                  # Cleaned text & TF-IDF matrices (.pkl)
    │
    ├── models/                         # Model Registry (Artifacts)
    │   └── stacking_model.pkl          # The trained Stacking Ensemble model
    │
    ├── src/                            # Source Code
    |   ├── __init__.py                 <-- REQUIRED
    │   ├── data/
    |   |   ├── __init__.py             <-- REQUIRED (Allows: from src.data import ...)
    │   │   ├── data_ingestion.py       # Loads raw data, splits Train/Test
    │   │   └── data_preprocessing.py   # Cleaning, Lemmatization, Stopwords
    │   ├── features/
    │   │   ├── __init__.py             <-- REQUIRED (Allows: from src.features import ...)
    │   │   └── build_features.py       # TF-IDF Vectorization (Trigrams, 10k features)
    │   └── models/
    │   |    ├── __init__.py            <-- REQUIRED (Allows: from src.models import ...)
    │   |    ├── train_model.py         # Stacking Ensemble training logic
    │   |    └── evaluate_model.py      # Metrics calculation (Accuracy, F1)
    |   | 
    |   └── prediction/
    |        ├── __init__.py            <-- REQUIRED (Allows: from src.prediction import ...)
    |        └── predict_model.py
    │
    ├── dvc.yaml                        # DVC Pipeline Definitions
    ├── params.yaml                     # Central Configuration (Hyperparameters)
    └── metrics.json                    # Model Performance Metrics
    │
    ├── setup.py                        # Building your application as a package



## Running the Pipeline
This project uses DVC (Data Version Control) to manage the ML pipeline.

1. Initialize (First Run Only)
If you are setting this up for the first time:

    * git init  (git bash)
    * dvc init

2. Reproduce Pipeline
Run the entire end-to-end workflow (Ingestion → Preprocessing → Training → Evaluation). DVC will only run stages that have changed.

    * dvc repro

3. DVC Diagram (Pipelines)
* dvc dag

4. View Metrics
Check the performance of the trained model.

    * dvc metrics show


## Inference & Prediction
- Project in progress...
