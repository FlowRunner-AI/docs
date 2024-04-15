When piecing together workflows (or "flows") in Backendless Automations, you're engaging in a dance of data. Every block in your flow, actions, triggers, conditions, utilities, or transformers plays with data. Each block has input parameters and produces outcomes that propel your process forward. Take the `Send Email` block as an example - it needs an email address to know where to send an email message. 

![Send Email Inputs Demo](images/send-email-inputs-demo.png)

Each time a block completes its task, it produces a "result". This result could be anything from a simple data point to a complex information set. For example, a trigger might kick off when a web form is submitted, capturing a treasure trove of the information entered by a customer in its "result". Notice that you can configure a human-readable name of the result element. The name you assign is how the system will present the result in many parts of the Flow Editor:

![Sample Result](images/reference-result-as-sample.png)

But here's where it gets interesting: the output of one block can feed directly into the next, even if they're not directly linked in your flow's sequence. Sometimes, the "result" of a block cannot be used as-is by the next block in line. It might need a bit of tweaking or transformation to fit the bill. For instance, if you want to email someone who just filled out a web form, you'll need to extract their email address from the form's submission data. In this case, Transformers and Expressions come into play, allowing you to mold the data to your needs.

![Get Email from Result](images/using-result-to-get-email.png)

By understanding and leveraging these data movements within your workflows, you're not just building processes but choreographing a seamless dance of information that powers your business operations. This chapter will guide you through mastering the art of data movement in your workflows, ensuring that each step is purposeful and powerful.
