


# streamlit run test_version.py --server.enableCORS false --server.enableXsrfProtection false
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







# 0319 V1
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

# @st.cache_data
# @st.cache_data
# def load_data():
#     df = pd.read_excel("data/EpiClock_sheet.xlsx", sheet_name='table', engine="openpyxl")

#     # Standardizing column names
#     df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")

#     # Fixing column-specific formats
#     df["first_published_in"] = pd.to_numeric(df["first_published_in"], errors="coerce").fillna(0).astype(int)
    
#     # Clean "#features_cpgs" column (removing non-numeric characters)
#     df["#features_cpgs"] = df["#features_cpgs"].astype(str).str.replace(r"\D", "", regex=True)  # Remove non-digits
#     df["#features_cpgs"] = pd.to_numeric(df["#features_cpgs"], errors="coerce").fillna(0).astype(int)

#     df["tissue"] = df["tissue"].fillna("").str.strip().str.lower()
#     df["response_variable"] = df["response_variable"].fillna("").str.strip().str.lower()
#     df["response_variable"] = df["response_variable"].replace("varies?", "unknown")

#     return df


# df = load_data()
# # Define available options for selection
# response_options = ["Chronological Age", 
#                     "Mitotic Age (Proxy for cumulative stem cell divisions)", 
#                     "Biomarker Age", 
#                     "Telomere Length", 
#                     "Others"]
# tissue_options = ["Whole Blood Only", "Multi-tissue", "Others"]
# method_options = ["Elastic Net", "Others"]  # Users can now multi-select

# # User selection filters
# response_var = st.multiselect("Select Response Variable", response_options, ["Chronological Age"])
# tissue_selected = st.multiselect("Select Tissue Type", tissue_options, ["Whole Blood Only"])
# method_selected = st.multiselect("Select Method", method_options, method_options)  # Default: All methods

# # Determine min and max years
# min_year = int(df["first_published_in"].min()) if not df["first_published_in"].isna().all() else 2010
# max_year = int(df["first_published_in"].max()) if not df["first_published_in"].isna().all() else 2024
# years = st.slider("Years", min_year, max_year, (2020, 2024))

# # Apply filters
# df_filtered = df[
#     (df["first_published_in"].between(years[0], years[1]))
# ]

# # Apply **Tissue Type** Filter
# if "Whole Blood Only" in tissue_selected:
#     df_filtered = df_filtered[df_filtered["tissue"].str.lower() == "whole blood"]
# elif "Multi-tissue" in tissue_selected:
#     df_filtered = df_filtered[df_filtered["tissue"] != "whole blood"]  # Excludes whole blood-only models

# # Apply **Response Variable** Filter
# if "Biomarker Age" in response_var:
#     df_filtered = df_filtered[df_filtered["response_variable"].str.contains("bio|causal", case=False, na=False)]
# elif "Mitotic Age (Proxy for cumulative stem cell divisions)" in response_var:
#     df_filtered = df_filtered[df_filtered["response_variable"].str.contains("mitotic", case=False, na=False)]
# elif "Chronological Age" in response_var:
#     df_filtered = df_filtered[df_filtered["response_variable"].str.contains("chronological", case=False, na=False)]
# elif "Telomere Length" in response_var:
#     df_filtered = df_filtered[df_filtered["response_variable"].str.contains("telomere", case=False, na=False)]
# elif "Others" in response_var:
#     df_filtered = df_filtered[~df_filtered["response_variable"].str.contains("chronological|mitotic|bio|causal|telomere", case=False, na=False)]

# # Apply **Method Filter**
# if "Elastic Net" in method_selected and "Others" not in method_selected:
#     df_filtered = df_filtered[df_filtered["method"].str.contains("elastic net", case=False, na=False)]
# elif "Others" in method_selected and "Elastic Net" not in method_selected:
#     df_filtered = df_filtered[~df_filtered["method"].str.contains("elastic net", case=False, na=False)]  # Excludes Elastic Net
# # If both or none are selected, no filtering is applied (default: show all methods)

# # Rename columns for better readability
# df_filtered_display = df_filtered.rename(columns={
#     "name": "Clock Name",
#     "tissue": "Tissue Type",
#     "method": "Regression Method",
#     "response_variable": "Target Variable",
#     "#features_cpgs": "Number of Features",
#     "first_published_in": "Year Published",
#     "special": "Special Notes",
#     "model_accessible_via": "Model Link",
#     "link": "Reference"
# })

# # Display the filtered dataframe
# st.dataframe(df_filtered_display)


# # Use AgGrid for interactive table
# gb = GridOptionsBuilder.from_dataframe(df_filtered_display)
# gb.configure_selection("single", use_checkbox=True)
# grid_options = gb.build()

# grid_response = AgGrid(df_filtered_display, gridOptions=grid_options, height=300, width='100%', theme="streamlit")

# # Debug: Print selected_rows to check if row selection is working
# # selected_rows = grid_response.get("selected_rows", [])
# # if isinstance(selected_rows, list) and len(selected_rows) > 0:
# #     selected_rows = pd.DataFrame(selected_rows)  # Convert to DataFrame explicitly
# # if isinstance(selected_rows, pd.DataFrame) and not selected_rows.empty:
# #     st.write("✅ Debug: Selected Row Data (as DataFrame) ->", selected_rows)  # Print full selected row

# #     # Convert first row to dictionary
# #     selected_dict = selected_rows.iloc[0].to_dict()

# #     # Print available keys
# #     st.write("✅ Debug: Available Keys in Selected Row ->", selected_dict.keys())

# #     # Extract clock name
# #     clock_name = selected_dict.get("Clock Name", "❌ NOT FOUND")
    
# #     # Debug print clock name
# #     st.write("✅ Debug: Extracted Clock Name ->", clock_name)

# #     # Store in session state
# #     if clock_name != "❌ NOT FOUND":
# #         st.session_state.selected_clock = clock_name
# #         st.rerun()  # ✅ Use this instead of experimental_rerun
# #     else:
# #         st.write("❌ Debug: Could not extract a valid Clock Name.")

# FIGURE_FOLDER = "figures"
# def get_figures(clock_name):
#     """Finds and returns a list of figure paths that contain the clock name."""
#     if not clock_name:
#         return []

#     clock_name_lower = clock_name.strip().replace(" ", "_").lower()  # Normalize clock name


#     # List all files in folder
#     available_files = os.listdir(FIGURE_FOLDER)

#     # Improved filename matching logic
#     matching_figures = [
#         os.path.join(FIGURE_FOLDER, f)
#         for f in available_files
#         if clock_name_lower in f.lower().replace(" ", "_").strip()
#     ]

#     return matching_figures


# # Ensure session state exists before use
# if "selected_clock" not in st.session_state:
#     st.session_state.selected_clock = None

# # Debug: Print selected_rows to check if row selection is working
# selected_rows = grid_response.get("selected_rows", [])
# if isinstance(selected_rows, list) and len(selected_rows) > 0:
#     selected_rows = pd.DataFrame(selected_rows)  # Convert to DataFrame explicitly

# if isinstance(selected_rows, pd.DataFrame) and not selected_rows.empty:
    
#     # Convert first row to dictionary
#     selected_dict = selected_rows.iloc[0].to_dict()

#     # Extract clock name
#     clock_name = selected_dict.get("Clock Name", "❌ NOT FOUND").strip()

#     # Store in session state and rerun if a new clock is selected
#     if clock_name != "❌ NOT FOUND" and st.session_state.selected_clock != clock_name:
#         st.session_state.selected_clock = clock_name
#         st.rerun()

# # Ensure figures are displayed **only if selected_clock exists**
# if st.session_state.selected_clock:
#     st.subheader(f"Figures for {st.session_state.selected_clock}")

#     # Get figure paths for the selected clock
#     figure_paths = get_figures(st.session_state.selected_clock)

#     # Define expected order of plots
#     expected_plot_order = [
#         "variance_inflation_factor",  # VIF plot
#         "trend_consistency",          # Trend consistency plot
#         "predicted_age_arthritis"     # Arthritis-related plot
#     ]

#     # Sort figure paths based on expected order
#     def sort_key(path):
#         for index, keyword in enumerate(expected_plot_order):
#             if keyword in path.lower():
#                 return index
#         return len(expected_plot_order)  # Place unknown plots at the end

#     figure_paths = sorted(figure_paths, key=sort_key)

#     # Display figures
#     if figure_paths:
#         for fig_path in figure_paths:
#             st.image(fig_path, caption=os.path.basename(fig_path))
#         st.write(
#         """
#         **1. Variance Inflation Factor (VIF) Plot**  
#         This plot quantifies multicollinearity in the regression model by measuring how much the variance of CpG coefficient estimates is inflated due to correlation with other CpGs. A higher VIF indicates stronger collinearity among CpGs in the model.  

#         **2. Trend Consistency Plot**  
#         This evaluates the proportion of CpGs whose correlation with age aligns with the sign of their assigned coefficient in the model. As expected, CpGs positively correlated with age should contribute positively to the predicted age, vice versa.

#         **3. Predicted Age in Arthritis (Healthy vs. Disease)**  
#         This plot compares the predicted age for individuals with and without arthritis. Note that some clocks may have less accurate predictions because the arthritis dataset does not contain all CpGs present in the original model.  
#         """
#         )
#     else:
#         st.warning("No figures available for this clock.")





# 03212025 version
# import streamlit as st
# import pandas as pd
# import os
# from st_aggrid import AgGrid, GridOptionsBuilder
# from PIL import Image
# import requests
# from bs4 import BeautifulSoup

# st.set_page_config(page_title="Epigenetic Clock Database", page_icon="🕑", layout="wide")

# # Function to load and clean data
# @st.cache_data
# def load_data():
#     df = pd.read_excel("data/EpiClock_sheet.xlsx", sheet_name='table', engine="openpyxl")

#     # Standardizing column names
#     df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")

#     # Convert 'first_published_in' to numeric while handling errors
#     df["first_published_in"] = pd.to_numeric(df["first_published_in"], errors="coerce").fillna(0).astype(int)

#     # Remove non-numeric characters from '#features_cpgs' and convert to int
#     df["#features_cpgs"] = df["#features_cpgs"].astype(str).str.replace(r"\D", "", regex=True)
#     df["#features_cpgs"] = pd.to_numeric(df["#features_cpgs"], errors="coerce").fillna(0).astype(int)

#     df["tissue"] = df["tissue"].fillna("").str.strip().str.lower()
#     df["response_variable"] = df["response_variable"].fillna("").str.strip().str.lower()
#     df["response_variable"] = df["response_variable"].replace("varies?", "unknown")

#     return df

# df = load_data()

# # Define available options for selection
# response_options = ["Chronological Age", "Mitotic Age (Proxy for cumulative stem cell divisions)", 
#                     "Biomarker Age", "Telomere Length", "Others"]
# tissue_options = ["Whole Blood Only", "Multi-tissue", "Others"]
# method_options = ["Elastic Net", "Others"]  # Users can now multi-select

# # User selection filters
# response_var = st.multiselect("Select Response Variable", response_options, ["Chronological Age"])
# tissue_selected = st.multiselect("Select Tissue Type", tissue_options, ["Whole Blood Only"])
# method_selected = st.multiselect("Select Method", method_options, method_options)  # Default: All methods

# # Determine min and max years
# min_year = int(df["first_published_in"].min()) if not df["first_published_in"].isna().all() else 2010
# max_year = int(df["first_published_in"].max()) if not df["first_published_in"].isna().all() else 2024
# years = st.slider("Years", min_year, max_year, (2020, 2024))

# # Apply filters
# df_filtered = df[df["first_published_in"].between(years[0], years[1])]

# # Apply **Tissue Type** Filter
# if "Whole Blood Only" in tissue_selected:
#     df_filtered = df_filtered[df_filtered["tissue"].str.lower() == "whole blood"]
# elif "Multi-tissue" in tissue_selected:
#     df_filtered = df_filtered[df_filtered["tissue"] != "whole blood"]  # Excludes whole blood-only models

# # Apply **Method Filter**
# if "Elastic Net" in method_selected and "Others" not in method_selected:
#     df_filtered = df_filtered[df_filtered["method"].str.contains("elastic net", case=False, na=False)]
# elif "Others" in method_selected and "Elastic Net" not in method_selected:
#     df_filtered = df_filtered[~df_filtered["method"].str.contains("elastic net", case=False, na=False)]  # Excludes Elastic Net

# df_display = df_filtered.rename(columns={
#     "Name": "Clock Name",
#     "Tissue": "Tissue Type",
#     "Method": "Regression Method",
#     "Response Variable": "Target Variable",
#     "#Features (CpGs)": "Number of Features",
#     "First Published In": "Year Published",
#     "Special": "Special Notes",
#     "Model Accessible Via": "Model Link",
#     "Link": "Reference"
# })


# st.write("### Epigenetic Clocks Overview")
# gb = GridOptionsBuilder.from_dataframe(df_display)
# gb.configure_selection("single", use_checkbox=True, pre_selected_rows=[0])
# grid_options = gb.build()
# grid_response = AgGrid(df_display, gridOptions=grid_options, theme="streamlit")

# # Function to get figures
# def get_figures(clock_name):
#     if not clock_name:
#         return [], ""

#     figure_base_path = "test_figures"
#     available_folders = os.listdir(figure_base_path)

#     matching_folders = [folder for folder in available_folders if folder == clock_name]

#     if not matching_folders:
#         return [], ""

#     clock_folder = os.path.join(figure_base_path, matching_folders[0])
#     figure_files = sorted(os.listdir(clock_folder))

#     vif_figures = [f for f in figure_files if "vif" in f.lower()]
#     other_figures = [f for f in figure_files if "vif" not in f.lower()]

#     return vif_figures + other_figures, clock_folder

# # Function to extract an abstract from a research paper link
# def extract_abstract(paper_link):
#     try:
#         response = requests.get(paper_link, timeout=5)
#         response.raise_for_status()

#         soup = BeautifulSoup(response.text, 'html.parser')
#         paragraphs = soup.find_all('p')

#         abstract_text = ""
#         for para in paragraphs[:6]:  # Extract first 6-7 sentences
#             abstract_text += para.get_text() + " "

#         return abstract_text.strip()
#     except Exception:
#         return "⚠️ Abstract preview not available."

# # Show Detailed Info for Selected Clock
# selected_rows = grid_response.get("selected_rows", [])
# if isinstance(selected_rows, list) and len(selected_rows) > 0:
#     selected_rows = pd.DataFrame(selected_rows)

# if isinstance(selected_rows, pd.DataFrame) and not selected_rows.empty:
#     selected_clock = selected_rows.iloc[0]["name"]
#     st.subheader(f"📜 Detailed Information for {selected_clock}", anchor='details-section')

#     st.markdown("""
#         <script>
#         setTimeout(function() {
#             document.getElementById('details-section').scrollIntoView({behavior: 'smooth', block: 'center'});
#         }, 500);
#         </script>
#         """, unsafe_allow_html=True)

#     # Display full details for selected row
#     df_selected = df_filtered[df_filtered["name"] == selected_clock].T.iloc[1:, :]
#     df_selected.columns = [selected_clock]
#     st.dataframe(df_selected, use_container_width=True)


#     # Show Figures for Selected Clock
#         # Show Figures for Selected Clock
#     st.subheader(f"📊 Figures for {selected_clock}")

#     figure_files, figure_folder = get_figures(selected_clock)

#     if figure_files:
#         vif_figs = [f for f in figure_files if "vif" in f.lower()]
#         if vif_figs:
#             st.markdown(
#                 """
#                 **Variance Inflation Factor (VIF)**
                
#                 - **VIF > 5** → Moderate collinearity.
#                 - **VIF > 10** → Strong collinearity.
#                 - **VIF > 20** → Very high correlation affecting model performance.
                
#                 The proportions indicate the percentage of features exceeding these thresholds.
#                 """
#             )

#         # Display each figure in its own row for consistency
#         for fig_file in figure_files:
#             fig_path = os.path.join(figure_folder, fig_file)
#             image = Image.open(fig_path)

#             # Use full width for uniform display
#             st.image(image, caption=fig_file, use_container_width=True)


#     else:
#         st.warning("⚠️ No figures available for this clock yet.")





# # don't know why but also like aggrid
# import streamlit as st
# import pandas as pd
# import os
# from PIL import Image

# st.set_page_config(page_title="Epigenetic Clock Database", page_icon="🕑", layout="wide")

# # Function to load and clean data
# @st.cache_data
# def load_data():
#     df = pd.read_excel("data/EpiClock_sheet.xlsx", sheet_name='table', engine="openpyxl")

#     # Standardizing column names
#     df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")

#     # Convert 'first_published_in' to numeric while handling errors
#     df["first_published_in"] = pd.to_numeric(df["first_published_in"], errors="coerce").fillna(0).astype(int)

#     # Remove non-numeric characters from '#features_cpgs' and convert to int
#     df["#features_cpgs"] = df["#features_cpgs"].astype(str).str.replace(r"\D", "", regex=True)
#     df["#features_cpgs"] = pd.to_numeric(df["#features_cpgs"], errors="coerce").fillna(0).astype(int)

#     df["tissue"] = df["tissue"].fillna("").str.strip().str.lower()
#     df["response_variable"] = df["response_variable"].fillna("").str.strip().str.lower()
#     df["response_variable"] = df["response_variable"].replace("varies?", "unknown")

#     return df

# df = load_data()

# # Define available options for selection
# response_options = ["Chronological Age", "Mitotic Age (Proxy for cumulative stem cell divisions)", 
#                     "Biomarker Age", "Telomere Length", "Others"]
# tissue_options = ["Whole Blood Only", "Multi-tissue", "Others"]
# method_options = ["Elastic Net", "Others"]

# # User selection filters
# response_var = st.multiselect("Select Response Variable", response_options, ["Chronological Age"])
# tissue_selected = st.multiselect("Select Tissue Type", tissue_options, ["Whole Blood Only"])
# method_selected = st.multiselect("Select Method", method_options, method_options)

# # Determine min and max years
# min_year = int(df["first_published_in"].min()) if not df["first_published_in"].isna().all() else 2010
# max_year = int(df["first_published_in"].max()) if not df["first_published_in"].isna().all() else 2024
# years = st.slider("Years", min_year, max_year, (2020, 2024))

# # Apply filters
# df_filtered = df[df["first_published_in"].between(years[0], years[1])]

# if "Whole Blood Only" in tissue_selected:
#     df_filtered = df_filtered[df_filtered["tissue"].str.lower() == "whole blood"]
# elif "Multi-tissue" in tissue_selected:
#     df_filtered = df_filtered[df_filtered["tissue"] != "whole blood"]

# if "Elastic Net" in method_selected and "Others" not in method_selected:
#     df_filtered = df_filtered[df_filtered["method"].str.contains("elastic net", case=False, na=False)]
# elif "Others" in method_selected and "Elastic Net" not in method_selected:
#     df_filtered = df_filtered[~df_filtered["method"].str.contains("elastic net", case=False, na=False)]

# df_display = df_filtered.rename(columns={
#     "name": "Clock Name",
#     "tissue": "Tissue Type",
#     "method": "Regression Method",
#     "response_variable": "Target Variable",
#     "#features_cpgs": "Number of Features",
#     "first_published_in": "Year Published",
#     "special": "Special Notes",
#     "model_accessible_via": "Model Link",
#     "link": "Reference"
# })

# # Display dataframe
# st.write("### Epigenetic Clocks Overview")
# st.dataframe(df_display, height=400, use_container_width=True)

# # **Radio button for selecting a row**
# clock_names = df_display["Clock Name"].tolist()
# if clock_names:
#     selected_clock = st.radio("Select a clock:", clock_names, index=0)

#     # Show Detailed Information
#     st.subheader(f"📜 Detailed Information for {selected_clock}", anchor='details-section')

#     # Extract selected row's details
#     df_selected = df_display[df_display["Clock Name"] == selected_clock].drop(columns=["Clock Name"]).T
#     df_selected.columns = ["Value"]
#     df_selected.reset_index(inplace=True)
#     df_selected.columns = ["Property", "Value"]

#     # Convert into a proper **2-column table**
#     details_table = df_selected.to_dict(orient="records")

#     # Use Markdown to format as a 2-column table
#     table_html = "<table style='width:100%; border-collapse: collapse;'>"
#     for i in range(0, len(details_table), 2):
#         table_html += "<tr>"
#         for j in range(2):
#             if i + j < len(details_table):
#                 key = details_table[i + j]["Property"]
#                 value = details_table[i + j]["Value"]
#                 table_html += f"<td style='padding: 8px; border: 1px solid black;'><b>{key}</b></td>"
#                 table_html += f"<td style='padding: 8px; border: 1px solid black;'>{value}</td>"
#         table_html += "</tr>"
#     table_html += "</table>"

#     st.markdown(table_html, unsafe_allow_html=True)

# else:
#     st.warning("No clocks available with the selected filters.")


import streamlit as st
import pandas as pd
import os
from PIL import Image

st.set_page_config(page_title="Epigenetic Clock Database", page_icon="🕑", layout="wide")
st.title("🕰 Epigenetic Clock Database")

st.write(
    """
    The Epigenetic Clock Database is a curated collection of various DNA methylation-based age predictors 
    (also known as **epigenetic clocks**). These clocks estimate chronological age or biological age based on methylation patterns 
    across different tissues, variables, and methodologies.

    This interactive web app allows researchers to explore and compare epigenetic clocks 
    based on their features, tissues studied, and statistical performance. All info is manually added, please contact _ for corrections, updates, or discussions.
    """
)

# Function to load and clean data
@st.cache_data
def load_data():
    df = pd.read_excel("data/EpiClock_sheet.xlsx", sheet_name='table', engine="openpyxl")

    # Standardizing column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")

    # Convert 'first_published_in' to numeric while handling errors (Fix: No commas)
    df["first_published_in"] = pd.to_numeric(df["first_published_in"], errors="coerce").fillna(0).astype(int)

    # Remove non-numeric characters from '#features_cpgs' and convert to integer
    df["#features_cpgs"] = df["#features_cpgs"].astype(str).str.replace(r"\D", "", regex=True)
    
    # ✅ Convert to Int64 (Ensures No Decimals, Keeps NaN)
    df["#features_cpgs"] = pd.to_numeric(df["#features_cpgs"], errors="coerce").astype("Int64")

    df["tissue"] = df["tissue"].fillna("").str.strip().str.lower()
    df["response_variable"] = df["response_variable"].fillna("").str.strip().str.lower()
    df["response_variable"] = df["response_variable"].replace("varies?", "unknown")

    return df

df = load_data()

# Define available options for selection
response_options = ["Chronological Age", "Mitotic Age (Proxy for cumulative stem cell divisions)", 
                    "Biomarker Age", "Telomere Length", "Others"]
tissue_options = ["Whole Blood Only", "Multi-tissue", "Others"]
method_options = ["Elastic Net", "Others"]

# User selection filters
response_var = st.multiselect("Select Response Variable", response_options, ["Chronological Age"])
tissue_selected = st.multiselect("Select Tissue Type", tissue_options, ["Whole Blood Only"])
method_selected = st.multiselect("Select Method", method_options, method_options)

# Determine min and max years (Fix: Remove comma formatting)
min_year = int(df["first_published_in"].min()) if not df["first_published_in"].isna().all() else 2010
max_year = int(df["first_published_in"].max()) if not df["first_published_in"].isna().all() else 2024
years = st.slider("Years", min_year, max_year, (2020, 2024))

# Apply filters
df_filtered = df[df["first_published_in"].between(years[0], years[1])]

if "Whole Blood Only" in tissue_selected:
    df_filtered = df_filtered[df_filtered["tissue"].str.lower() == "whole blood"]
elif "Multi-tissue" in tissue_selected:
    df_filtered = df_filtered[df_filtered["tissue"] != "whole blood"]

if "Elastic Net" in method_selected and "Others" not in method_selected:
    df_filtered = df_filtered[df_filtered["method"].str.contains("elastic net", case=False, na=False)]
elif "Others" in method_selected and "Elastic Net" not in method_selected:
    df_filtered = df_filtered[~df_filtered["method"].str.contains("elastic net", case=False, na=False)]

# Convert missing/0 feature counts to "Not Specified"
df_filtered["#features_cpgs"] = df_filtered["#features_cpgs"].apply(
    lambda x: "Not Specified" if pd.isna(x) or x == 0 else str(int(x))  # Ensure Integer Format
)

df_display = df_filtered.rename(columns={
    "name": "Clock Name",
    "tissue": "Tissue Type",
    "method": "Regression Method",
    "response_variable": "Target Variable",
    "#features_cpgs": "Number of Features",
    "first_published_in": "Year Published",
    "special": "Special Notes",
    "model_accessible_via": "Model Link",
    "link": "Reference"
})

# Ensure Year Published is displayed without commas
df_display["Year Published"] = df_display["Year Published"].astype(str)

# Display dataframe
st.write("### Epigenetic Clocks Overview")
st.dataframe(df_display, height=400, use_container_width=True)

# **Radio button for selecting a row**
clock_names = df_display["Clock Name"].tolist()
if clock_names:
    selected_clock = st.radio("Select a clock:", clock_names, index=0)

    # Show Detailed Information
    st.subheader(f"📜 Detailed Information for {selected_clock}", anchor='details-section')

    # Extract selected row's details
    df_selected = df_display[df_display["Clock Name"] == selected_clock].drop(columns=["Clock Name"]).T
    df_selected.columns = ["Value"]
    df_selected.reset_index(inplace=True)
    df_selected.columns = ["Property", "Value"]

    # Convert into a proper **2-column table**
    details_table = df_selected.to_dict(orient="records")

    # Use Markdown to format as a 2-column table
    table_html = "<table style='width:100%; border-collapse: collapse;'>"
    for i in range(0, len(details_table), 2):
        table_html += "<tr>"
        for j in range(2):
            if i + j < len(details_table):
                key = details_table[i + j]["Property"]
                value = details_table[i + j]["Value"]
                table_html += f"<td style='padding: 8px; border: 1px solid black;'><b>{key}</b></td>"
                table_html += f"<td style='padding: 8px; border: 1px solid black;'>{value}</td>"
        table_html += "</tr>"
    table_html += "</table>"

    st.markdown(table_html, unsafe_allow_html=True)

else:
    st.warning("No clocks available with the selected filters.")
