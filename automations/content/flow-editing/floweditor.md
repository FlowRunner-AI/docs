---
icon: material/palette
---
# Introduction to the Flow Editor  

The Flow Editor is the centerpiece of FlowRunner™, offering an intuitive, graphical environment to design and refine workflows. With its user-friendly interface and robust features, it caters to both beginners and experienced automation specialists. This chapter introduces the key elements of the Flow Editor and guides you through its layout and functionalities.  

To access the Flow Editor, click the **Edit Flow** icon for the desired flow version in the Flow Manager:  

![Enter Flow Editor](../images/navigate-to-editor.png)  

!!! warning "Editing a Version with Analytics Data"  

    Editing a previously `LIVE` flow version will result in the deletion of its analytics data.  

    ![delete analytics confirmation](../images/edit-version-analytics.png)  

    Analytics data becomes invalid when a flow’s internal model changes during editing. FlowRunner™ requires confirmation before proceeding, ensuring you understand the implications.  

## Editor Canvas  

The Editor Canvas is where workflows come to life. It provides a visual space to design your automation by arranging and connecting blocks such as Triggers, Actions, Conditions, Transformers, and Groups. This graphical representation makes workflows easy to understand and adjust.  

![Editor Canvas](../images/editor-canvas.png)  

The Canvas is highly flexible, allowing you to arrange components intuitively. You can drag, drop, and connect blocks to create a seamless flow, visually reflecting your automation logic.  

## Blocks Toolbox  

Located beside the Editor Canvas, the Blocks Toolbox contains all the building blocks needed to create workflows. Blocks are categorized into Triggers, Actions, Groups, and Utilities, making it easy to locate the functionality you need.  

![Blocks Toolbox](../images/blocks-toolbox.png)  

Features of the Blocks Toolbox include:  

- **Search Bar**: Quickly find blocks by name or functionality.  
- **Marketplace Access**: Click the Marketplace icon to the right of the search bar to access FlowRunner™ Extensions in the Marketplace.
- **Hover Descriptions**: Hover over a block to view a detailed description of its purpose.  

## Control Bar  

The Control Bar is your command center, providing essential tools for workflow development.  

![Control Bar](../images/control-bar.png)  

Key functionalities include:  

- **Back to Flows Manager**: Return to the Flow Manager.  
- **Start Flow**: Launch the current version, moving it to the `LIVE` state.  
- **Test Mode Toggle**: Validate your workflow’s logic and execution in a safe, controlled environment. Visit the [Testing your Flows](../flow-execution/testing.md) section of this guide for more information about the Test Mode. 
- **Auto Save Toggle**: Ensure your changes are automatically saved.  
