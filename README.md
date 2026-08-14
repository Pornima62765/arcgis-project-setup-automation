# GIS Project Setup Automation

## Overview

This project contains an ArcGIS Pro Python script tool that automatically creates a standard GIS project workspace.

Instead of manually creating project folders, copying an ArcGIS Pro project template, creating a file geodatabase, and updating project settings, the script performs the full setup process automatically.

The purpose of the project is to improve consistency, reduce repetitive setup work, and provide GIS analysts with a repeatable project creation workflow.

## What the Tool Does

The script performs the following workflow:

1. Receives project information from an ArcGIS Pro script tool.
2. Builds a standard project name using the project year and project name.
3. Checks that the selected ArcGIS Pro template exists and is an `.aprx` file.
4. Creates the main project directory.
5. Creates a standard set of GIS project subfolders.
6. Copies the master ArcGIS Pro project template into the new project.
7. Creates a project-specific file geodatabase.
8. Sets the new project's home folder.
9. Sets the project geodatabase as the default geodatabase.
10. Saves the configured ArcGIS Pro project.
11. Returns the created project folder and `.aprx` file to ArcGIS Pro.

## Project Folder Structure

The tool creates the following structure:

```text
2026_Project_Name
│
├── 01_Input_Data
├── 02_ArcGIS_Project
│   └── 2026_Project_Name.aprx
│
├── 03_Scripts
├── 04_Working_Data
│   └── 2026_Project_Name.gdb
│
├── 05_Outputs
├── 06_Documentation
├── 07_Maps
└── 08_FieldMaps
```

## Script Tool Parameters

The script is designed to run as an ArcGIS Pro Script Tool.

### Inputs

| Parameter     | Type   | Description                                          |
| ------------- | ------ | ---------------------------------------------------- |
| Base Folder   | Folder | Location where the new GIS project will be created   |
| Project Year  | String | Project year, for example `2026`                     |
| Project Name  | String | Name of the GIS project                              |
| Template APRX | File   | Master ArcGIS Pro `.aprx` project used as a template |

### Derived Outputs

| Parameter      | Type   | Description                                  |
| -------------- | ------ | -------------------------------------------- |
| Project Folder | Folder | Path to the newly created GIS project        |
| Output APRX    | File   | Path to the newly created ArcGIS Pro project |

## Example

User inputs:

```text
Base Folder:
C:\GIS_Projects

Project Year:
2026

Project Name:
Park_Accessibility

Template APRX:
C:\GIS_Templates\Standard_GIS_Template.aprx
```

The tool creates:

```text
C:\GIS_Projects\2026_Park_Accessibility
```

and creates the ArcGIS Pro project:

```text
C:\GIS_Projects\2026_Park_Accessibility\
02_ArcGIS_Project\
2026_Park_Accessibility.aprx
```

The project geodatabase is created as:

```text
C:\GIS_Projects\2026_Park_Accessibility\
04_Working_Data\
2026_Park_Accessibility.gdb
```

## Technologies Used

* Python
* ArcPy
* ArcGIS Pro
* `arcpy.mp`
* `arcpy.management`
* Python `os` module

## Important ArcPy Functions Used

### `arcpy.GetParameterAsText()`

Receives parameter values entered through the ArcGIS Pro Script Tool interface.

### `arcpy.mp.ArcGISProject()`

Opens an ArcGIS Pro `.aprx` project so that it can be copied or modified programmatically.

### `saveACopy()`

Creates a copy of the master ArcGIS Pro project template for the new project.

### `arcpy.management.CreateFileGDB()`

Creates the project-specific file geodatabase.

### `arcpy.SetParameterAsText()`

Returns the newly created project folder and ArcGIS Pro project as outputs from the Script Tool.

## Error Handling

The script checks for several potential problems before completing the workflow.

For example, it checks whether:

* The ArcGIS Pro template exists
* The template is an `.aprx` file
* The output ArcGIS Pro project already exists

If an error occurs, ArcGIS Pro displays an error message using:

```python
arcpy.AddError()
```

## Why I Created This Project

GIS projects often require the same initial setup:

* Creating standard folders
* Creating a working geodatabase
* Copying a standard ArcGIS Pro project
* Configuring project paths
* Maintaining consistent naming

Doing this manually for every project is repetitive and can lead to inconsistent project structures.

This script demonstrates how Python and ArcPy can automate the process and create a repeatable GIS project setup workflow.

## Skills Demonstrated

This project demonstrates practical experience with:

* Python scripting
* ArcPy
* ArcGIS Pro automation
* GIS project management
* Script Tool development
* File and folder handling
* File geodatabase creation
* Project template management
* Input validation
* Exception handling
* Workflow standardisation

## Possible Future Improvements

Future versions could include:

* Automatic creation of feature datasets
* Automatic creation of standard map layouts
* Coordinate system selection
* Automatic creation of standard feature classes
* Project metadata generation
* Logging project creation details
* Copying standard symbology and layer files
* Automatically adding reference datasets
* Creating Field Maps-ready inspection layers
* Publishing selected project layers to ArcGIS Online
