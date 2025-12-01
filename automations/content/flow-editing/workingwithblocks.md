---
icon: fontawesome/solid/boxes-stacked
---

# Working with Blocks  

Blocks are the core components of your workflows in FlowRunner™, each offering distinct functionality to automate tasks and processes. While individual blocks have unique capabilities, the principles for adding, connecting, and editing them remain consistent. This chapter provides an overview of these principles to help you efficiently build and refine workflows in the Flow Editor.  

## The Basics of Blocks  

- **Starting Point**: Every flow begins with a `Start` marker, which designates the starting point of your workflow. This marker is a fixed reference for your automation's entry point.  
![Flow Start Marker](../images/start-element-in-flow.png)  

    ??? info "Changing the Starting Point"  
        To change the starting block, follow the steps outlined in the interactive tutorial below:  
        <div style="position: relative; padding-bottom: calc(52.583333333333336% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/TpCpdxhwI1Qs42Dv5uK7?embed&show_copy_link=true" title="Automations - Edit Flow - My First Flow - Version 1 - Automations - Backendless" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>  

- **Adding Blocks**: Drag blocks from the [Blocks Toolbox](floweditor.md#blocks-toolbox) onto the [Editor Canvas](floweditor.md#editor-canvas) to build your workflow. Each block adds new capabilities to your automation.  

- **Initiating Flows**: A flow can start with various blocks, including triggers, actions, or groups. For example, triggers wait for specific events to activate the subsequent blocks in your workflow.  

## Connecting Blocks  

- **Flow Transitions**: Blocks are connected by lines that represent the execution flow, guiding the logic from one block to the next.  To remove a transition, hover the mouse over the connecting line and click the **Remove Connection** icon.

    ![remove connection](../images/remove-connection.png)

- **Multiple Successors**: A block can lead to multiple successors, enabling parallel execution. For example, in the image below, the `Callback from CRM` trigger activates two successors, both executed when the trigger fires:  
![Multiple successors](../images/multiple-successors.png)  

- **Multiple Predecessors**: Similarly, a block can have multiple predecessors, allowing different triggers or conditions to converge. In the image below, the `Send SMS` block has two predecessors, executing immediately after each:  
![Multiple predecessors](../images/multiple-predecessors.png)  

    !!! info "Handling Concurrency with Multiple Predecessors"  
        Use [Action Groups](./grouping-actions.md) or [Trigger Groups](./grouping-triggers.md) to manage concurrency effectively.  

## Editing and Viewing Properties  

Clicking a block opens its properties in the Property Editor, where you can customize its settings to fit your automation needs.  
![Property Editor](../images/property-sheet-sample.png)  

The properties displayed vary depending on the block. For detailed information about specific blocks, refer to the relevant sections in the documentation.  