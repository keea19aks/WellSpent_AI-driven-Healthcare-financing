# WellSpent_AI-driven-Healthcare-financing

## Project Overview
WellSpent is an **AI-powered financial planning app** designed to help users **estimate, predict, and optimize their healthcare expenses**. It provides real-time cost estimations, AI-driven policy matching, and predictive modeling for future medical expenses.

## Key Features
**Real-time Hospital Cost Estimator** - Uses actual hospital fee data to predict medical expenses.
**AI-Powered Insurance Policy Matching** - Suggests the best insurance coverage based on health & financial needs.
**Future Healthcare Cost Prediction** - Machine learning models estimate hospitalization & medication costs.
**Grants & Reimbursement Tracking** - Helps users maximize available subsidies & reimbursements.
**Seamless Singpass Integration** - Pulls real-time healthcare data for better accuracy.

## How It Works
1. **User Logs in with Singpass** → Auto-fetches healthcare & insurance details.
2. **Dashboard Overview** → Displays estimated out-of-pocket costs & insurance coverage.
3. **AI Analysis** → Predicts future medical expenses & coverage gaps.
4. **Policy Recommendations** → Suggests optimized insurance plans.
5. **Real-time Updates** → Tracks grants, reimbursements & policy changes.

## Installation & Setup
### **Prerequisites**
- Python 3.8+
- Jupyter Notebook
- Required libraries (install using `pip install -r requirements.txt`)

### **Running the Project**
1. Clone the repository:
   ```bash
   git clone https://github.com/Sudhishna-Janavi/WellSpent_AI-driven-Healthcare-financing.git
   ```
2. Navigate to the project folder:
   ```bash
   cd WellSpent_AI-driven-Healthcare-financing
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## Dataset Information
- **fee-publication-data.xlsx**: Real hospital cost data for treatment price prediction.
- **insurance.csv**: Used to train AI models for policy matching & cost estimation.

## Tech Stack
- **Python** (pandas, numpy, scikit-learn, XGBoost)
- **Jupyter Notebook** (for model training & testing)
- **Flask/FastAPI** (for backend API integration - future implementation)
- **Singpass API, MOH & CPF APIs** (for real-time data retrieval)

## Link to out-of-pocket calculator: https://outofpock.streamlit.app/ 
