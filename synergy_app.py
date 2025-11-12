import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Synergy Analyzer", layout="wide")

st.title("🤝 ML-Based Framework for Enhancing Inter-Organizational Synergy")
st.write("This dashboard visualizes collaboration efficiency and bottlenecks identified by the ML system.")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("synergy_analysis_results.csv")

data = load_data()

# Display data
st.subheader("📊 Collaboration Analysis Data")
st.dataframe(data)

# Summary stats
st.subheader("📈 Summary Statistics")
st.write(data.describe())

# Bottleneck Analysis
bottlenecks = data[data["bottleneck_flag"] == "Bottleneck"]
st.subheader("🚨 Bottleneck Organizations")
st.dataframe(bottlenecks)

# Visualization
st.subheader("📉 Project Delays by Organization")
fig, ax = plt.subplots()
ax.bar(data["organization"], data["project_delay_days"], color="skyblue")
ax.set_xlabel("Organization")
ax.set_ylabel("Delay (Days)")
ax.set_title("Project Delays by Organization")
st.pyplot(fig)

# Recommendations
st.subheader("💡 AI Recommendations")
for index, row in bottlenecks.iterrows():
    st.markdown(f"**{row['organization']}** → {row['recommendation']}")

st.success("✅ Analysis complete.")
