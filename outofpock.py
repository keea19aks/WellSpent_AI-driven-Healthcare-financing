import streamlit as st
import pandas as pd

# Load Excel file
@st.cache_data
def load_data():
    file_path = "fee-publication-data-jan22-dec22-(for-download).xlsx"  # Update with your actual file path
    df = pd.read_excel(file_path, sheet_name="1_TOSP TOF and Bill data")  # Load the relevant sheet
    return df

# Load the dataset
df = load_data()



#st.write("Columns in DataFrame:", df.columns.tolist())


# Extract relevant columns (adjust based on the file structure)
columns_needed = ["Procedure", "Hospital Setting", "Ward Type", "P50 Bill"]
df = df[columns_needed].dropna()  # Remove any empty rows

# Streamlit UI
st.title("💰 Out-of-Pocket Medical Cost Calculator")
st.markdown("Use this tool to estimate your medical expenses based on procedure and hospital setting.")

# User selections
procedure = st.selectbox("🔹 Select Your Procedure:", df["Procedure"].unique())
hospital_setting = st.selectbox("🏥 Select Hospital Setting:", df["Hospital Setting"].unique())
ward_type = st.selectbox("🛏️ Select Ward Type:", df["Ward Type"].unique())

# Filter data based on selection
filtered_data = df[
    (df["Procedure"] == procedure) &
    (df["Hospital Setting"] == hospital_setting) &
    (df["Ward Type"] == ward_type)
]

# Display results
if not filtered_data.empty:
    avg_bill = filtered_data["P50 Bill"].values[0]
    st.subheader(f"💲 Estimated Bill: **${avg_bill:,.2f}**")

    # Insurance and subsidy options
    insurance_coverage = st.slider("📄 Insurance Coverage (%)", 0, 100, 50)  # Default 50%
    gov_subsidy = st.slider("🏛️ Government Subsidy (%)", 0, 100, 30)  # Default 30%

    # Calculate out-of-pocket cost
    covered_by_insurance = avg_bill * (insurance_coverage / 100)
    covered_by_subsidy = avg_bill * (gov_subsidy / 100)
    out_of_pocket = avg_bill - (covered_by_insurance + covered_by_subsidy)

    st.subheader(f"🧾 Estimated Out-of-Pocket Cost: **${out_of_pocket:,.2f}**")

else:
    st.warning("No data found for the selected options. Please try different selections.")

# Footer
st.markdown("---")
st.caption("📌 Note: This is an estimation tool. Actual costs may vary.")

