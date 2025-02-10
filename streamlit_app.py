import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Epigenetic Clock Database", page_icon="🕑")
st.title("🕰 Epigenetic Clock Database")
st.write(
    """
    The Epigenetic Clock Database is a curated collection of various DNA methylation-based age predictors 
    (also known as **epigenetic clocks**). These clocks estimate chronological age or biological age based on methylation patterns 
    across different tissues, variables, and methodologies.

    This interactive web app allows researchers and practitioners to explore and compare epigenetic clocks 
    based on their features, tissues studied, and statistical performance.
    """
)

# Load the data
@st.cache_data
def load_data():
    df = pd.read_excel("data/EpiClock_sheet.xlsx", sheet_name='table', engine="openpyxl")

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df["first_published_in"] = df["first_published_in"].astype(str).str.replace(",", "").astype(float).astype("Int64")
    df["#features"] = pd.to_numeric(df["#features"], errors="coerce").fillna(0).astype(int)
    df["tissue"] = df["tissue"].fillna("").str.strip().str.lower()
    df["response_variable"] = df["response_variable"].fillna("").str.strip().str.lower()
    df["response_variable"] = df["response_variable"].replace("varies?", "unknown")

    return df

df = load_data()

response_options = ["Chronological Age", "Mitotic Age", "Biomarker Age"]
tissue_options = ["Whole Blood", "Others"]

# Widgets
response_var = st.multiselect("Select Response Variable", response_options, ["Chronological Age"])
tissue_selected = st.multiselect("Select Tissue Type", tissue_options, ["Whole Blood"])

# ensure min/max values for slider
min_year = int(df["first_published_in"].min()) if not df["first_published_in"].isna().all() else 2010
max_year = int(df["first_published_in"].max()) if not df["first_published_in"].isna().all() else 2024
years = st.slider("Years", min_year, max_year, (2020, 2024))

# filter data with matching on the key words
df_filtered = df[
    (df["first_published_in"].between(years[0], years[1])) &
    (
        (
            df["tissue"].apply(lambda x: "whole blood" in x) if "Whole Blood" in tissue_selected
            else df["tissue"].apply(lambda x: x not in ["", "whole blood"]) if "Others" in tissue_selected
            else True  # If nothing is selected, return all tissues
        )

    ) &
    (
        (df["response_variable"].apply(lambda x: 
            ("chronological" in x or "chronological" in response_var) or 
            ("mitotic" in x or "mitotic" in response_var) or
            ("biomarker" in x or "biomarker" in response_var)
        )) if response_var else True  # If empty, include all response variables
    )
]
# rename for display
df_filtered = df_filtered.rename(columns={
    "name": "Clock Name",
    "tissue": "Tissue Type",
    "programme": "Programming Language",
    "method": "Regression Method",
    "response_variable": "Target Variable",
    "#features": "Number of Features",
    "special": "Special Features",
    "web_links": "Code Link",
    "first_published_in": "Year Published",
    "link": "Reference Link",
    "correlation_coefficient_(r²)_with_chronological_age": "R² (Chronological Age)",
    "mean_absolute_deviation_(mad)_with_chronological_age": "MAD (Chronological Age)"
})

st.write("Filtered Rows:", df_filtered.shape[0])  # Debugging check

# Display full table with all columns
if not df_filtered.empty:
    st.dataframe(df_filtered, use_container_width=True)

    # New Scatter Plot to Show All Information**
    df_chart = df_filtered.copy()

    # chart = (
    #     alt.Chart(df_chart)
    #     .mark_circle(size=80)
    #     .encode(
    #         x=alt.X("first_published_in:N", title="Year Published"),
    #         y=alt.Y("#features:Q", title="Number of Features"),
    #         color="response_variable:N",
    #         tooltip=[
    #             alt.Tooltip("name:N", title="Clock Name"),
    #             alt.Tooltip("tissue:N", title="Tissue Type"),
    #             alt.Tooltip("programme:N", title="Programme"),
    #             alt.Tooltip("method:N", title="Method"),
    #             alt.Tooltip("response_variable:N", title="Response Variable"),
    #             alt.Tooltip("#features:Q", title="Feature Count"),
    #             alt.Tooltip("special:N", title="Special Feature"),
    #             alt.Tooltip("web_links:N", title="Code Links"),
    #             alt.Tooltip("correlation_coefficient_(r²)_with_chronological_age:Q", title="R²"),
    #             alt.Tooltip("mean_absolute_deviation_(mad)_with_chronological_age:Q", title="MAD"),
    #         ]
    #     )
    #     .properties(height=500, width=800, title="Epigenetic Clock Features Over Time")
    # )

    st.altair_chart(chart, use_container_width=True)

else:
    st.warning("No matching data found. Try adjusting your filters!")



# year bug (2,020) 
# the leftmost columns to be the names of clock
# figures show the functions of clocks
# standard dataset plugging in, a figure for every clock,
    # maybe use the arthritis dataset as a standard
# login? how to upload their own?
# get this done firstttttt


# effort from past 5-6 years in meth clocks, recurit any other phd in continuing this work? or me the last one
    # yes - happy, then i can talk about this
    # no - secretly finish this and tell her to publish

# crtisim: why not control for cell type in wb clock
    # use epidish https://github.com/sjczheng/EpiDISH to control beforehadn
    # fig1 no control fig2 control using epidish

# in our review, show people how many clocks are out(and what have they been doing in common) 
# there already and people should probably switch focus 