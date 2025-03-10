

# # year bug (2,020) - fixed
# # the leftmost columns to be the names of clock - fixed
# # figures show the functions of clocks
# # standard dataset plugging in, a figure for every clock,
#     # maybe use the arthritis dataset as a standard
# # login? how to upload their own?
# # get this done firstttttt


# # effort from past 5-6 years in meth clocks, recurit any other phd in continuing this work? or me the last one
#     # yes - happy, then i can talk about this
#     # no - secretly finish this and tell her to publish

# # crtisim: why not control for cell type in wb clock
#     # use epidish https://github.com/sjczheng/EpiDISH to control beforehadn
#     # fig1 no control fig2 control using epidish

# # in our review, show people how many clocks are out(and what have they been doing in common) 
# # there already and people should probably switch focus 


# #202502170606 single choice click
# import streamlit as st
# import pandas as pd
# import os
# from st_aggrid import AgGrid, GridOptionsBuilder

# st.set_page_config(page_title="Epigenetic Clock Database", page_icon="🕑")
# st.title("🕰 Epigenetic Clock Database")

# st.write(
#     """
#     The Epigenetic Clock Database is a curated collection of various DNA methylation-based age predictors 
#     (also known as **epigenetic clocks**). These clocks estimate chronological age or biological age based on methylation patterns 
#     across different tissues, variables, and methodologies.

#     This interactive web app allows researchers and practitioners to explore and compare epigenetic clocks 
#     based on their features, tissues studied, and statistical performance.
#     """
# )

# # Load Data
# @st.cache_data
# def load_data():
#     df = pd.read_excel("data/EpiClock_sheet.xlsx", sheet_name='table', engine="openpyxl")

#     df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
#     df["first_published_in"] = df["first_published_in"].astype(str).str.replace(",", "").astype(float).astype("Int64")
#     df["#features"] = pd.to_numeric(df["#features"], errors="coerce").fillna(0).astype(int)
#     df["tissue"] = df["tissue"].fillna("").str.strip().str.lower()
#     df["response_variable"] = df["response_variable"].fillna("").str.strip().str.lower()
#     df["response_variable"] = df["response_variable"].replace("varies?", "unknown")

#     return df

# df = load_data()

# response_options = ["Chronological Age", "Mitotic Age", "Biomarker Age"]
# tissue_options = ["Whole Blood", "Others"]

# # Widgets
# response_var = st.multiselect("Select Response Variable", response_options, ["Chronological Age"])
# tissue_selected = st.multiselect("Select Tissue Type", tissue_options, ["Whole Blood"])

# # Ensure min/max values for slider
# min_year = int(df["first_published_in"].min()) if not df["first_published_in"].isna().all() else 2010
# max_year = int(df["first_published_in"].max()) if not df["first_published_in"].isna().all() else 2024
# years = st.slider("Years", min_year, max_year, (2020, 2024))

# # Apply filters correctly
# df_filtered = df[
#     (df["first_published_in"].between(years[0], years[1])) & 
#     (df["tissue"].apply(lambda x: "whole blood" in x if "Whole Blood" in tissue_selected else x not in ["", "whole blood"]))
# ]

# # Rename columns for display
# df_filtered_display = df_filtered.rename(columns={
#     "name": "Clock Name",
#     "tissue": "Tissue Type",
#     "programme": "Programming Language",
#     "method": "Regression Method",
#     "response_variable": "Target Variable",
#     "#features": "Number of Features",
#     "first_published_in": "Year Published"
# })

# # Ensure session state for selected clock
# if "selected_clock" not in st.session_state:
#     st.session_state.selected_clock = None

# st.subheader("Select a Clock from the Table Below")

# # Use AgGrid for interactive table
# gb = GridOptionsBuilder.from_dataframe(df_filtered_display)
# gb.configure_selection("single", use_checkbox=True)
# grid_options = gb.build()

# grid_response = AgGrid(df_filtered_display, gridOptions=grid_options, height=300, width='100%', theme="streamlit")

# # Update session state with selected row
# selected_rows = grid_response['selected_rows']
# if selected_rows is not None and len(selected_rows) > 0:
#     st.session_state.selected_clock = selected_rows[0].get("Clock Name", None)


# # Function to get figure paths
# FIGURE_FOLDER = "figures"

# def get_figures(clock_name):
#     """Finds and returns a list of figure paths for a given clock."""
#     if clock_name is None:
#         return []
    
#     clock_id = clock_name.replace(" ", "_").lower()
    
#     # Ensure the folder exists
#     if not os.path.exists(FIGURE_FOLDER):
#         return []

#     # Find matching images
#     figures = [
#         os.path.join(FIGURE_FOLDER, f) 
#         for f in os.listdir(FIGURE_FOLDER) if f.startswith(clock_id)
#     ]
    
#     return figures

# # Display figures for selected clock
# if st.session_state.selected_clock:
#     st.subheader(f"Figures for {st.session_state.selected_clock}")
#     figure_paths = get_figures(st.session_state.selected_clock)

#     if figure_paths:
#         for fig_path in figure_paths:
#             st.image(fig_path, caption=os.path.basename(fig_path))
#     else:
#         st.warning("No figures available for this clock.")

import streamlit as st
import pandas as pd
import os
from st_aggrid import AgGrid, GridOptionsBuilder

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

# Load Data
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

# Ensure min/max values for slider
min_year = int(df["first_published_in"].min()) if not df["first_published_in"].isna().all() else 2010
max_year = int(df["first_published_in"].max()) if not df["first_published_in"].isna().all() else 2024
years = st.slider("Years", min_year, max_year, (2020, 2024))

# Apply filters correctly
df_filtered = df[
    (df["first_published_in"].between(years[0], years[1])) & 
    (df["tissue"].apply(lambda x: "whole blood" in x if "Whole Blood" in tissue_selected else x not in ["", "whole blood"]))
]

# Rename columns for display
df_filtered_display = df_filtered.rename(columns={
    "name": "Clock Name",
    "tissue": "Tissue Type",
    "programme": "Programming Language",
    "method": "Regression Method",
    "response_variable": "Target Variable",
    "#features": "Number of Features",
    "first_published_in": "Year Published"
})

# Ensure session state for selected clock
if "selected_clock" not in st.session_state:
    st.session_state.selected_clock = None

st.subheader("Select a Clock from the Table Below")

# Use AgGrid for interactive table
gb = GridOptionsBuilder.from_dataframe(df_filtered_display)
gb.configure_selection("single", use_checkbox=True)
grid_options = gb.build()

grid_response = AgGrid(df_filtered_display, gridOptions=grid_options, height=300, width='100%', theme="streamlit")

# Debug: Print selected_rows to check if row selection is working
# selected_rows = grid_response.get("selected_rows", [])
# if isinstance(selected_rows, list) and len(selected_rows) > 0:
#     selected_rows = pd.DataFrame(selected_rows)  # Convert to DataFrame explicitly
# if isinstance(selected_rows, pd.DataFrame) and not selected_rows.empty:
#     st.write("✅ Debug: Selected Row Data (as DataFrame) ->", selected_rows)  # Print full selected row

#     # Convert first row to dictionary
#     selected_dict = selected_rows.iloc[0].to_dict()

#     # Print available keys
#     st.write("✅ Debug: Available Keys in Selected Row ->", selected_dict.keys())

#     # Extract clock name
#     clock_name = selected_dict.get("Clock Name", "❌ NOT FOUND")
    
#     # Debug print clock name
#     st.write("✅ Debug: Extracted Clock Name ->", clock_name)

#     # Store in session state
#     if clock_name != "❌ NOT FOUND":
#         st.session_state.selected_clock = clock_name
#         st.rerun()  # ✅ Use this instead of experimental_rerun
#     else:
#         st.write("❌ Debug: Could not extract a valid Clock Name.")

FIGURE_FOLDER = "figures"
def get_figures(clock_name):
    """Finds and returns a list of figure paths that contain the clock name."""
    if not clock_name:
        return []

    clock_name_lower = clock_name.strip().replace(" ", "_").lower()  # Normalize clock name


    # List all files in folder
    available_files = os.listdir(FIGURE_FOLDER)

    # Improved filename matching logic
    matching_figures = [
        os.path.join(FIGURE_FOLDER, f)
        for f in available_files
        if clock_name_lower in f.lower().replace(" ", "_").strip()
    ]

    return matching_figures



# Debug: Print selected_rows to check if row selection is working
selected_rows = grid_response.get("selected_rows", [])
if isinstance(selected_rows, list) and len(selected_rows) > 0:
    selected_rows = pd.DataFrame(selected_rows)  # Convert to DataFrame explicitly

if isinstance(selected_rows, pd.DataFrame) and not selected_rows.empty:
    
    # Convert first row to dictionary
    selected_dict = selected_rows.iloc[0].to_dict()

    # Extract clock name
    clock_name = selected_dict.get("Clock Name", "❌ NOT FOUND").strip()

    # Ensure session state exists
    if "selected_clock" not in st.session_state:
        st.session_state.selected_clock = None

    # Store in session state and debug check
    if clock_name != "❌ NOT FOUND":
        st.session_state.selected_clock = clock_name
        st.rerun()
    else:
        st.write("❌ Debug: Could not extract a valid Clock Name.")

# Ensure figures are displayed **only if selected_clock exists**
if st.session_state.selected_clock:
    st.subheader(f"Figures for {st.session_state.selected_clock}")

    # Get figure paths for the selected clock
    figure_paths = get_figures(st.session_state.selected_clock)

    # Display figures
    if figure_paths:
        for fig_path in figure_paths:
            st.image(fig_path, caption=os.path.basename(fig_path))
        st.write(
        """

        **1. Variance Inflation Factor (VIF) Plot**  
        This plot quantifies multicollinearity in the regression model by measuring how much the variance of CpG coefficient estimates is inflated due to correlation with other CpGs. A higher VIF indicates stronger collinearity among CpGs in the model.  

        **2. Trend Consistency Plot**  
        This evaluates the proportion of CpGs whose correlation with age aligns with the sign of their assigned coefficient in the model. As expected, CpGs positively correlated with age should contribute positively to the predicted age, vice versa.

        **3. Predicted Age in Arthritis (Healthy vs. Disease)**  
        This plot compares the predicted age for individuals with and without arthritis. Note that some clocks may have less accurate predictions because the arthritis dataset does not contain all CpGs present in the original model.  
        """
    )
    else:
        st.warning("No figures available for this clock.")
    
    

# previous seperate tab
# import streamlit as st
# import pandas as pd
# import os

# st.set_page_config(page_title="Epigenetic Clock Database", page_icon="🕑")
# st.title("🕰 Epigenetic Clock Database")

# st.write(
#     """
#     The Epigenetic Clock Database is a curated collection of various DNA methylation-based age predictors 
#     (also known as **epigenetic clocks**). These clocks estimate chronological age or biological age based on methylation patterns 
#     across different tissues, variables, and methodologies.

#     This interactive web app allows researchers and practitioners to explore and compare epigenetic clocks 
#     based on their features, tissues studied, and statistical performance.
#     """
# )

# # Load Data
# @st.cache_data
# def load_data():
#     df = pd.read_excel("data/EpiClock_sheet.xlsx", sheet_name='table', engine="openpyxl")

#     df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
#     df["first_published_in"] = df["first_published_in"].astype(str).str.replace(",", "").astype(float).astype("Int64")
#     df["#features"] = pd.to_numeric(df["#features"], errors="coerce").fillna(0).astype(int)
#     df["tissue"] = df["tissue"].fillna("").str.strip().str.lower()
#     df["response_variable"] = df["response_variable"].fillna("").str.strip().str.lower()
#     df["response_variable"] = df["response_variable"].replace("varies?", "unknown")

#     return df

# df = load_data()

# response_options = ["Chronological Age", "Mitotic Age", "Biomarker Age"]
# tissue_options = ["Whole Blood", "Others"]

# # Widgets
# response_var = st.multiselect("Select Response Variable", response_options, ["Chronological Age"])
# tissue_selected = st.multiselect("Select Tissue Type", tissue_options, ["Whole Blood"])

# # Ensure min/max values for slider
# min_year = int(df["first_published_in"].min()) if not df["first_published_in"].isna().all() else 2010
# max_year = int(df["first_published_in"].max()) if not df["first_published_in"].isna().all() else 2024
# years = st.slider("Years", min_year, max_year, (2020, 2024))

# # Apply filters correctly
# df_filtered = df[
#     (df["first_published_in"].between(years[0], years[1])) &
#     (
#         (
#             df["tissue"].apply(lambda x: "whole blood" in x) if "Whole Blood" in tissue_selected
#             else df["tissue"].apply(lambda x: x not in ["", "whole blood"]) if "Others" in tissue_selected
#             else True  # If nothing is selected, return all tissues
#         )
#     ) &
#     (
#         (df["response_variable"].apply(lambda x: 
#             ("chronological" in x or "chronological" in response_var) or 
#             ("mitotic" in x or "mitotic" in response_var) or
#             ("biomarker" in x or "biomarker" in response_var)
#         )) if response_var else True  # If empty, include all response variables
#     )
# ]

# # Rename columns for display
# df_filtered_display = df_filtered.rename(columns={
#     "name": "Clock Name",
#     "tissue": "Tissue Type",
#     "programme": "Programming Language",
#     "method": "Regression Method",
#     "response_variable": "Target Variable",
#     "#features": "Number of Features",
#     "special": "Special Features",
#     "web_links": "Code Link",
#     "first_published_in": "Year Published",
#     "link": "Reference Link",
#     "correlation_coefficient_(r²)_with_chronological_age": "R² (Chronological Age)",
#     "mean_absolute_deviation_(mad)_with_chronological_age": "MAD (Chronological Age)"
# })

# if not df_filtered_display.empty:
#     st.dataframe(df_filtered_display, use_container_width=True)

    
#     # Ensure selected clock is stored in session state
#     if "selected_clock" not in st.session_state:
#         st.session_state.selected_clock = None

#     st.subheader("Select a Clock to View Figures")

#     FIGURE_FOLDER = "figures"

#     def get_figures(clock_name):
#         """Finds and returns a list of figure paths for a given clock."""
#         clock_id = clock_name.replace(" ", "_").lower()  # Normalize clock name for matching
#         figures = [
#             os.path.join(FIGURE_FOLDER, f) 
#             for f in os.listdir(FIGURE_FOLDER) if f.startswith(clock_id)
#         ]
#         return figures

#     # Display table with "Show Figures" buttons
#     for index, row in df_filtered_display.iterrows():
#         col1, col2 = st.columns([0.9, 0.1])  # Adjust layout
#         with col1:
#             st.write(f"📊 **{row['Clock Name']}** ({row['Year Published']})")
#         with col2:
#             if st.button(f"Show Figures", key=row["Clock Name"]):
#                 st.session_state.selected_clock = row["Clock Name"]

# else:
#     st.warning("No matching data found. Try adjusting your filters!")

# # Show figures when a clock is selected
# if st.session_state.selected_clock:
#     st.subheader(f"Figures for {st.session_state.selected_clock}")

#     # Get figure paths
#     figure_paths = get_figures(st.session_state.selected_clock)

#     # Display figures
#     if figure_paths:
#         for fig_path in figure_paths:
#             st.image(fig_path, caption=os.path.basename(fig_path))
#     else:
#         st.warning("No figures available for this clock.")
