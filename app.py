
import streamlit as st

st.set_page_config(
    page_title="AI Landing Page Generator",
    page_icon="🚀"
)

st.title("🚀 AI Landing Page Generator")

st.write(
    "Generate attractive landing page headlines "
    "using AI copywriting frameworks."
)

# User inputs

product = st.text_input(
    "Enter Product or Service Name"
)

page_type = st.selectbox(
    "Select Landing Page Type",
    ["SaaS", "E-commerce", "Course", "Service", "App"]
)

framework = st.selectbox(
    "Select Copywriting Framework",
    ["AIDA", "PAS", "FAB"]
)

problem = st.text_input(
    "Enter Customer Problem (for PAS)"
)

# Generate button

if st.button("Generate Landing Page"):

    if not product.strip():
        st.warning("Please enter a product name.")

    elif framework == "PAS" and not problem.strip():
        st.warning("Please enter a customer problem.")

    else:

        if framework == "AIDA":
            headline = f"Discover the Power of {product} Today!"

        elif framework == "PAS":
            headline = f"Struggling with {problem}? Try {product}!"

        else:
            headline = f"Experience the Benefits of {product}!"

        st.success("Landing Page Generated!")

        st.subheader("Generated Headline")
        st.write(headline)

        st.subheader("Page Type")
        st.write(page_type)

        st.subheader("Framework")
        st.write(framework)

        st.info("Thank you for using our generator!")
