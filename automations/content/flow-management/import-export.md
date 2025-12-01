---
icon: material/import
---

The Import/Export feature in FlowRunner™ makes it easy to back up and share your automation flows. By exporting a flow version, you create a file containing everything needed to replicate or migrate the version, including its automation logic, schedule (if any), and SLA goals (if any). This file can later be used to recreate the version within the same app or in another Backendless environment.  

## Exporting a Flow Version  

Exporting a flow version is quick and simple:  

1. Locate the version you want to export in the **Flow Manager**.  
2. Navigate to the **VERSION ADMIN** tab.
2. Click the **START EXPORT** button.  

    ![export action](../images/export-version.png)

FlowRunner™ will generate an export file that includes:  

- The version’s automation flow and logic.  
- Any associated schedule.  
- Any defined SLA goals.  

The file is then available for download and can be stored or shared as needed.  

## Importing a Flow Version  

FlowRunner™ offers two ways to import a flow version from an export file:  

### Import into an Existing Flow  

To add a version to an existing flow:  

1. Open the **Flow Manager** and locate the target flow (the flow where you would like to import a version to).  
2. Click the hamburger icon (☰) located next to the flow name.
2. Click the **Import Flow** icon in the flow’s title bar.  
3. Use the file browser to select the export file.  
  
    ![import version to flow](../images/import-version.png)

Once imported, the flow will include a new version that is an exact replica of the exported version.  

### Create a New Flow from an Export  

To create a brand-new flow using an export file:  

1. Click the **Create a New Flow** button in the **Flow Manager**.  
2. In the **Create a New Flow** popup, click the **Browse…** button.  
3. Select the export file from your local machine and confirm.  

    ![new flow from export](../images/create-new-flow-from-export.png)

A new flow will be created, with its first version being an identical copy of the original exported version.  

This feature is invaluable for migrating, replicating, or sharing flows while ensuring all associated settings and configurations are preserved.  