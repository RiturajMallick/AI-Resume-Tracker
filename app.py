import streamlit as st
import requests

# Function to get job listings (From JSearch API)
def get_job_listings(query, location):
    api_key = "f677772889msh1aa0d674284462ap1cf2a7jsn2f2557275e02"  # Replace with your API key
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {"X-RapidAPI-Key": api_key, "X-RapidAPI-Host": "jsearch.p.rapidapi.com"}
    params = {"query": query, "location": location, "num_pages": 1}

    response = requests.get(url, headers=headers, params=params)
    jobs = response.json().get("data", [])
    return jobs

# Streamlit UI
st.title("🚀 AI Resume Tracker")
st.write("Upload your resume and find job listings along with recruiter emails!")

uploaded_file = st.file_uploader("Upload your Resume (PDF/DOCX)", type=["pdf", "docx"])

if uploaded_file:
    st.success("✅ Resume Uploaded Successfully!")
    job_query = st.text_input("Enter Job Role", "Software Engineer")
    job_location = st.text_input("Enter Location", "Remote")

    if st.button("Find Jobs"):
        jobs = get_job_listings(job_query, job_location)
        if jobs:
            for job in jobs:
                st.write(f"**{job['job_title']}**")
                st.write(f"📍 {job['job_city']}, {job['job_country']}")
                st.write(f"🔗 [Apply Here]({job['job_apply_link']})")
                st.write("---")
        else:
            st.warning("No jobs found! Try another search.")
