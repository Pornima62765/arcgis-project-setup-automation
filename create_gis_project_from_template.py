"""ArcGIS Pro script tool for creating a standard GIS project.

Script tool parameters:
    0 - Base Folder (Folder, Input)
    1 - Project Year (String, Input)
    2 - Project Name (String, Input)
    3 - Template APRX (File, Input; filter: aprx)
    4 - Project Folder (Folder, Derived Output)
    5 - Output APRX (File, Derived Output)

    Run this script inside ArcGIS Pro
"""

import os

import arcpy



# Receive the script tool parameters.
base_folder = arcpy.GetParameterAsText(0)
project_year = arcpy.GetParameterAsText(1)
project_name = arcpy.GetParameterAsText(2)
template_aprx = arcpy.GetParameterAsText(3)

# Create the standard project name and full project path.
project_folder_name = project_year + "_" + project_name
project_folder = os.path.join(base_folder, project_folder_name)

subfolders = [
    "01_Input_Data",
    "02_ArcGIS_Project",
    "03_Scripts",
    "04_Working_Data",
    "05_Outputs",
    "06_Documentation",
    "07_Maps","08_FieldMaps"
]


try:
    # Check the template.
    if not os.path.isfile(template_aprx):
        raise FileNotFoundError(
            "The template project could not be found: " + template_aprx
        )

    if not template_aprx.lower().endswith(".aprx"):
        raise ValueError("The template must be an ArcGIS Pro .aprx file.")

    # Create the project folders.
    os.makedirs(project_folder, exist_ok=True)
    arcpy.AddMessage("Creating project folders...")

    for folder_name in subfolders:
        folder_path = os.path.join(project_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        arcpy.AddMessage("Created: " + folder_name)

    # Create the output APRX path.
    arcgis_project_folder = os.path.join(project_folder, "02_ArcGIS_Project")
    output_aprx_name = project_folder_name + ".aprx"
    output_aprx = os.path.join(arcgis_project_folder, output_aprx_name)

    if os.path.exists(output_aprx):
        raise FileExistsError("The project already exists: " + output_aprx)

    # Copy the master ArcGIS Pro project template.
    arcpy.AddMessage("Copying the master project template...")
    template_project = arcpy.mp.ArcGISProject(template_aprx)
    template_project.saveACopy(output_aprx)
    del template_project

    arcpy.AddMessage("New ArcGIS project created:")
    arcpy.AddMessage(output_aprx)

    # Create the project file geodatabase.
    working_data_folder = os.path.join(project_folder, "04_Working_Data")
    geodatabase_name = project_folder_name + ".gdb"
    geodatabase_path = os.path.join(working_data_folder, geodatabase_name)

    if not arcpy.Exists(geodatabase_path):
        arcpy.management.CreateFileGDB(
            working_data_folder,
            geodatabase_name,
        )
        arcpy.AddMessage("Project geodatabase created: " + geodatabase_path)

    # Update and save the new project's settings.
    new_project = arcpy.mp.ArcGISProject(output_aprx)
    new_project.homeFolder = project_folder
    new_project.defaultGeodatabase = geodatabase_path
    new_project.save()
    del new_project

    # Return the derived outputs to ArcGIS Pro.
    arcpy.SetParameterAsText(4, project_folder)
    arcpy.SetParameterAsText(5, output_aprx)
    arcpy.AddMessage("GIS project created successfully from the template.")

except Exception as error:
    arcpy.AddError("The GIS project could not be created.")
    arcpy.AddError(str(error))
    raise
