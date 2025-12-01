
The block processes the uploaded file and validates it against specific criteria:  

  - The file size must be **less than 5242880 bytes** (5 MB).  
  - The file extension must be one of the following: `.png`, `.jpg`, or `.jpeg`.  

These criteria are defined as a multi-part condition attached to the trigger. Take a moment to observe how the condition and its individual parts are configured. The overall condition is structured as shown below:

![ai extraction parts](../images/ai-extraction-condition-parts.png)
 
This means that `Part A` must always be met, and at least one of Parts `B`, `C`, or `D` must also be true for the flow to proceed with its execution. The configuration of the individual parts is shown below:

<div style="width:400px" markdown>
![condition part A](../images/ai-extraction-trigger-partA.png)
</div>
<div style="width:400px" markdown>
![condition part B](../images/ai-extraction-trigger-partB.png)
</div>
<div style="width:400px" markdown>
![condition part C](../images/ai-extraction-trigger-partC.png)
</div>
<div style="width:400px" markdown>
![condition part D](../images/ai-extraction-trigger-partD.png)
</div>

If the uploaded file meets the overall condition, the flow continues. Otherwise, the flow waits for a new upload.