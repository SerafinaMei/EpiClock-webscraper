# # # # V0 origrinal
# # # import streamlit as st
# # # import pandas as pd
# # # import os
# # # from st_aggrid import AgGrid, GridOptionsBuilder

# # # st.set_page_config(page_title="Epigenetic Clock Database", page_icon="🕑")
# # # st.title("🕰 Epigenetic Clock Database")

# # # st.write(
# # #     """
# # #     The Epigenetic Clock Database is a curated collection of various DNA methylation-based age predictors 
# # #     (also known as **epigenetic clocks**). These clocks estimate chronological age or biological age based on methylation patterns 
# # #     across different tissues, variables, and methodologies.

# # #     This interactive web app allows researchers and practitioners to explore and compare epigenetic clocks 
# # #     based on their features, tissues studied, and statistical performance.
# # #     """
# # # )

# # # # Load Data
# # # @st.cache_data
# # # def load_data():
# # #     df = pd.read_excel("data/EpiClock_test.xlsx", sheet_name='Sheet1', engine="openpyxl")

# # #     df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
# # #     df["first_published_in"] = df["first_published_in"].astype(str).str.replace(",", "").astype(float).astype("Int64")
# # #     df["#features"] = pd.to_numeric(df["#features"], errors="coerce").fillna(0).astype(int)
# # #     df["tissue"] = df["tissue"].fillna("").str.strip().str.lower()
# # #     df["response_variable"] = df["response_variable"].fillna("").str.strip().str.lower()
# # #     df["response_variable"] = df["response_variable"].replace("varies?", "unknown")

# # #     return df

# # # df = load_data()

# # # response_options = ["Chronological Age", "Mitotic Age", "Biomarker Age"]
# # # tissue_options = ["Whole Blood", "Others"]

# # # # Widgets
# # # response_var = st.multiselect("Select Response Variable", response_options, ["Chronological Age"])
# # # tissue_selected = st.multiselect("Select Tissue Type", tissue_options, ["Whole Blood"])

# # # # Ensure min/max values for slider
# # # min_year = int(df["first_published_in"].min()) if not df["first_published_in"].isna().all() else 2010
# # # max_year = int(df["first_published_in"].max()) if not df["first_published_in"].isna().all() else 2024
# # # years = st.slider("Years", min_year, max_year, (2020, 2024))

# # # # Apply filters correctly
# # # df_filtered = df[
# # #     (df["first_published_in"].between(years[0], years[1])) & 
# # #     (df["tissue"].apply(lambda x: "whole blood" in x if "Whole Blood" in tissue_selected else x not in ["", "whole blood"]))
# # # ]

# # # # Rename columns for display
# # # df_filtered_display = df_filtered.rename(columns={
# # #     "name": "Clock Name",
# # #     "tissue": "Tissue Type",
# # #     "programme": "Programming Language",
# # #     "method": "Regression Method",
# # #     "response_variable": "Target Variable",
# # #     "#features": "Number of Features",
# # #     "first_published_in": "Year Published"
# # # })

# # # # Ensure session state for selected clock
# # # if "selected_clock" not in st.session_state:
# # #     st.session_state.selected_clock = None

# # # st.subheader("Select a Clock from the Table Below")

# # # # Use AgGrid for interactive table
# # # gb = GridOptionsBuilder.from_dataframe(df_filtered_display)
# # # gb.configure_selection("single", use_checkbox=True)
# # # grid_options = gb.build()

# # # grid_response = AgGrid(df_filtered_display, gridOptions=grid_options, height=300, width='100%', theme="streamlit")

# # # # Debug: Print selected_rows to check if row selection is working
# # # # selected_rows = grid_response.get("selected_rows", [])
# # # # if isinstance(selected_rows, list) and len(selected_rows) > 0:
# # # #     selected_rows = pd.DataFrame(selected_rows)  # Convert to DataFrame explicitly
# # # # if isinstance(selected_rows, pd.DataFrame) and not selected_rows.empty:
# # # #     st.write("✅ Debug: Selected Row Data (as DataFrame) ->", selected_rows)  # Print full selected row

# # # #     # Convert first row to dictionary
# # # #     selected_dict = selected_rows.iloc[0].to_dict()

# # # #     # Print available keys
# # # #     st.write("✅ Debug: Available Keys in Selected Row ->", selected_dict.keys())

# # # #     # Extract clock name
# # # #     clock_name = selected_dict.get("Clock Name", "❌ NOT FOUND")
    
# # # #     # Debug print clock name
# # # #     st.write("✅ Debug: Extracted Clock Name ->", clock_name)

# # # #     # Store in session state
# # # #     if clock_name != "❌ NOT FOUND":
# # # #         st.session_state.selected_clock = clock_name
# # # #         st.rerun()  # ✅ Use this instead of experimental_rerun
# # # #     else:
# # # #         st.write("❌ Debug: Could not extract a valid Clock Name.")

# # # FIGURE_FOLDER = "test_figures"
# # # def get_figures(clock_name):
# # #     """Finds and returns a list of figure paths that contain the clock name."""
# # #     if not clock_name:
# # #         return []

# # #     clock_name_lower = clock_name.strip().replace(" ", "_").lower()  # Normalize clock name


# # #     # List all files in folder
# # #     available_files = os.listdir(FIGURE_FOLDER)

# # #     # Improved filename matching logic
# # #     matching_figures = [
# # #         os.path.join(FIGURE_FOLDER, f)
# # #         for f in available_files
# # #         if clock_name_lower in f.lower().replace(" ", "_").strip()
# # #     ]

# # #     return matching_figures



# # # # Debug: Print selected_rows to check if row selection is working
# # # selected_rows = grid_response.get("selected_rows", [])
# # # if isinstance(selected_rows, list) and len(selected_rows) > 0:
# # #     selected_rows = pd.DataFrame(selected_rows)  # Convert to DataFrame explicitly

# # # if isinstance(selected_rows, pd.DataFrame) and not selected_rows.empty:
    
# # #     # Convert first row to dictionary
# # #     selected_dict = selected_rows.iloc[0].to_dict()

# # #     # Extract clock name
# # #     clock_name = selected_dict.get("Clock Name", "❌ NOT FOUND").strip()

# # #     # Ensure session state exists
# # #     if "selected_clock" not in st.session_state:
# # #         st.session_state.selected_clock = None

# # #     # Store in session state and debug check
# # #     if clock_name != "❌ NOT FOUND":
# # #         st.session_state.selected_clock = clock_name
# # #         st.rerun()
# # #     else:
# # #         st.write("❌ Debug: Could not extract a valid Clock Name.")

# # # # Ensure figures are displayed **only if selected_clock exists**
# # # if st.session_state.selected_clock:
# # #     st.subheader(f"Figures for {st.session_state.selected_clock}")

# # #     # Get figure paths for the selected clock
# # #     figure_paths = get_figures(st.session_state.selected_clock)

# # #     # Display figures
# # #     if figure_paths:
# # #         for fig_path in figure_paths:
# # #             st.image(fig_path, caption=os.path.basename(fig_path))
# # #         st.write(
# # #         """

# # #         **1. Variance Inflation Factor (VIF) Plot**  
# # #         This plot quantifies multicollinearity in the regression model by measuring how much the variance of CpG coefficient estimates is inflated due to correlation with other CpGs. A higher VIF indicates stronger collinearity among CpGs in the model.  

# # #         **2. Trend Consistency Plot**  
# # #         This evaluates the proportion of CpGs whose correlation with age aligns with the sign of their assigned coefficient in the model. As expected, CpGs positively correlated with age should contribute positively to the predicted age, vice versa.

# # #         **3. Predicted Age in Arthritis (Healthy vs. Disease)**  
# # #         This plot compares the predicted age for individuals with and without arthritis. Note that some clocks may have less accurate predictions because the arthritis dataset does not contain all CpGs present in the original model.  
# # #         """
# # #     )
# # #     else:
# # #         st.warning("No figures available for this clock.")
    
    



# #V1
# import streamlit as st
# import pandas as pd
# import os
# from st_aggrid import AgGrid, GridOptionsBuilder
# from PIL import Image

# st.set_page_config(page_title="Epigenetic Clock Database", page_icon="🕑", layout="wide")
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
#     df = pd.read_excel("data/EpiClock_test.xlsx", sheet_name='Sheet1', engine="openpyxl")
#     df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
#     df["first_published_in"] = df["first_published_in"].astype(str).str.replace(",", "").astype(float).astype("Int64")
#     df["#features"] = pd.to_numeric(df["#features"], errors="coerce").fillna(0).astype(int)
#     df["tissue"] = df["tissue"].fillna("").str.strip().str.lower()
#     df["response_variable"] = df["response_variable"].fillna("").str.strip().str.lower()
#     df["response_variable"] = df["response_variable"].replace("varies?", "unknown")
#     return df

# df = load_data()

# # UI Layout Optimization
# col1, col2 = st.columns([2, 1])

# with col1:
#     response_var = st.multiselect("Select Response Variable", ["Chronological Age", "Mitotic Age", "Biomarker Age"], ["Chronological Age"])
#     tissue_selected = st.multiselect("Select Tissue Type", ["Whole Blood", "Others"], ["Whole Blood"])

# with col2:
#     min_year = int(df["first_published_in"].min()) if not df["first_published_in"].isna().all() else 2010
#     max_year = int(df["first_published_in"].max()) if not df["first_published_in"].isna().all() else 2024
#     years = st.slider("Years", min_year, max_year, (2020, 2024))

# # Apply filters
# df_filtered = df[(df["first_published_in"].between(years[0], years[1])) & 
#                  (df["tissue"].apply(lambda x: "whole blood" in x if "Whole Blood" in tissue_selected else x not in ["", "whole blood"]))]

# # Display Initial Table with Limited Columns
# df_display = df_filtered
# df_display.insert(0, "More Info", ["🔍"] * len(df_display))

# st.write("### Epigenetic Clocks Overview")
# gb = GridOptionsBuilder.from_dataframe(df_display)
# gb.configure_selection("single", use_checkbox=True, pre_selected_rows=[0])
# grid_options = gb.build()
# grid_response = AgGrid(df_display, gridOptions=grid_options, height=300, width='100%', theme="streamlit")

# # Show Detailed Info for Selected Clock
# selected_rows = grid_response.get("selected_rows", [])
# if isinstance(selected_rows, list) and len(selected_rows) > 0:
#     selected_rows = pd.DataFrame(selected_rows)  # Convert to DataFrame explicitly
# if isinstance(selected_rows, pd.DataFrame) and not selected_rows.empty:
#     selected_clock = selected_rows.iloc[0]["name"]
#     st.subheader(f"📜 Detailed Information for {selected_clock}")
    
#     # Display full details for selected row
#     df_selected = df_filtered[df_filtered["name"] == selected_clock].T
#     df_selected.columns = [selected_clock]
#     st.dataframe(df_selected, use_container_width=True)
    
#     # Show Figures
#     def get_figures(clock_name):
#         if not clock_name:
#             return []
#         clock_name_lower = clock_name.strip().replace(" ", "_").lower()
#         available_files = os.listdir("test_figures")
#         return [os.path.join("test_figures", f) for f in available_files if clock_name_lower in f.lower().replace(" ", "_")]
    
#     figure_paths = get_figures(selected_clock)
#     if figure_paths:
#         st.subheader("📊 Figures")
#         cols = st.columns(2)
#         for i, fig_path in enumerate(figure_paths):
#             image = Image.open(fig_path)
#             cols[i % 2].image(image, caption=os.path.basename(fig_path), use_column_width=True)
#     else:
#         st.warning("No figures available for this clock.")

#V2 
import streamlit as st
import pandas as pd
import os
from st_aggrid import AgGrid, GridOptionsBuilder
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(page_title="Epigenetic Clock Database", page_icon="🕑", layout="wide")

# Custom CSS for better styling
st.markdown(
    """
    <style>
        .css-1d391kg, .css-1v0mbdj, .css-1r6slb0, .css-18ni7ap {
            font-family: 'Arial', sans-serif !important;
        }
        .stDataFrame {
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 8px 16px;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .stTitle {
            text-align: center;
        }
        .stSubheader {
            text-align: center;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🕰 Epigenetic Clock Database")

st.write(
    """
    <div style='text-align: center;'>
    The Epigenetic Clock Database is a curated collection of various DNA methylation-based age predictors 
    (also known as <b>epigenetic clocks</b>). These clocks estimate chronological age or biological age based on methylation patterns 
    across different tissues, variables, and methodologies.
    
    This interactive web app allows researchers and practitioners to explore and compare epigenetic clocks 
    based on their features, tissues studied, and statistical performance.
    </div>
    """,
    unsafe_allow_html=True,
)

# Load Data
@st.cache_data
def load_data():
    df = pd.read_excel("data/EpiClock_test.xlsx", sheet_name='Sheet1', engine="openpyxl")
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df["first_published_in"] = df["first_published_in"].astype(str).str.replace(",", "").astype(float).astype("Int64")
    df["#features"] = pd.to_numeric(df["#features"], errors="coerce").fillna(0).astype(int)
    df["tissue"] = df["tissue"].fillna("").str.strip().str.lower()
    df["response_variable"] = df["response_variable"].fillna("").str.strip().str.lower()
    df["response_variable"] = df["response_variable"].replace("varies?", "unknown")
    return df

df = load_data()

# UI Layout Optimization
col1, col2 = st.columns([2, 1])

with col1:
    response_var = st.multiselect("Select Response Variable", ["Chronological Age", "Mitotic Age", "Biomarker Age"], ["Chronological Age"])
    tissue_selected = st.multiselect("Select Tissue Type", ["Whole Blood", "Others"], ["Whole Blood"])

with col2:
    min_year = int(df["first_published_in"].min()) if not df["first_published_in"].isna().all() else 2010
    max_year = int(df["first_published_in"].max()) if not df["first_published_in"].isna().all() else 2024
    years = st.slider("Years", min_year, max_year, (2020, 2024))

# Apply filters
df_filtered = df[(df["first_published_in"].between(years[0], years[1])) & 
                 (df["tissue"].apply(lambda x: "whole blood" in x if "Whole Blood" in tissue_selected else x not in ["", "whole blood"]))]

# Display Initial Table with Limited Columns
initial_columns = ["name", "first_published_in", "#features", "method", "tissue"]
df_display = df_filtered[initial_columns]
df_display.insert(0, "", ["🔍"] * len(df_display))

st.write("### Epigenetic Clocks Overview")
gb = GridOptionsBuilder.from_dataframe(df_display)
gb.configure_selection("single", use_checkbox=True, pre_selected_rows=[0])
gb.configure_grid_options(dom_layout='normal')  # Adjust height dynamically
grid_options = gb.build()
grid_response = AgGrid(df_display, gridOptions=grid_options, theme="streamlit")

# Show Detailed Info for Selected Clock
selected_rows = grid_response.get("selected_rows", [])
if isinstance(selected_rows, list) and len(selected_rows) > 0:
    selected_rows = pd.DataFrame(selected_rows)  # Convert to DataFrame explicitly
if isinstance(selected_rows, pd.DataFrame) and not selected_rows.empty:
    selected_clock = selected_rows.iloc[0]["name"]
    st.subheader(f"📜 Detailed Information for {selected_clock}", anchor='details-section')
    
    # Scroll user to detailed info section
    st.markdown("""
        <script>
        setTimeout(function() {
            document.getElementById('details-section').scrollIntoView({behavior: 'smooth', block: 'center'});
        }, 500);
        </script>
        """, unsafe_allow_html=True)
        
    
    # Display full details for selected row
    df_selected = df_filtered[df_filtered["name"] == selected_clock].T.iloc[1:,:] # to remove the row of name
    df_selected.columns = [selected_clock]
    st.dataframe(df_selected, use_container_width=True)
    
    # Show Figures
    def get_figures(clock_name):
        if not clock_name:
            return []
        clock_name_lower = clock_name.strip().replace(" ", "_").lower()
        available_files = os.listdir("test_figures")
        return [os.path.join("test_figures", f) for f in available_files if clock_name_lower in f.lower().replace(" ", "_")]
    
    figure_paths = get_figures(selected_clock)
    if figure_paths:
        st.subheader("📊 Figures")
        cols = st.columns(2)
        for i, fig_path in enumerate(figure_paths):
            image = Image.open(fig_path)
            cols[i % 2].image(image, caption=os.path.basename(fig_path), use_container_width=True)
    else:
        st.warning("No figures available for this clock.")
