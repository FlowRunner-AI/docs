---
icon: material/security
---

# Assigning Execution Permissions

In the exciting world of FlowRunner™, setting up who gets to do what is crucial to keeping your system's operations smooth and secure. Imagine you've built a fantastic set of automations to streamline your business processes. Now, you need to ensure that only the right eyes and hands can trigger these automations. This is where execution permissions come into play, a simple yet powerful feature in Backendless that helps you manage who can call your automation flows. It may not necessarily be a person, FlowRunner™ can be invoked from other external systems. The permissions system allows you to specify the identities (either explicit or implicit via roles) which are authorized to call your flows.

## Understanding Execution Permissions

Execution permissions in FlowRunner™ are all about control and security. By setting these permissions, you decide which user accounts or security roles can invoke your automation flows. This capability is particularly important because it affects two primary ways your flows can be triggered:

- **API Calls**: This option allows external systems or services to execute a flow, extending the power of FlowRunner™ beyond the confines of your app.
- **The [`Call Flow`](../flow-execution/overview.md#callflow-commandapi) Action Block in a Flow**: With this, you can set up a chain reaction where one flow triggers another, creating a complex but efficient automation system within your Backendless app.

## Granting or Denying Permissions

Every flow you create in Backendless can have its own custom set of permissions. You can grant or deny access to specific users or security roles, tailoring who can trigger your flows based on your app's needs. This granularity ensures that your automations run exactly as intended, by the right people or systems.

- **For Individual Users**: When you assign permissions to a user account, you directly control that account's ability to invoke your flows.
- **For Security Roles**: Assigning permissions to a security role applies that permission to all users under that role. This way, you can efficiently manage permissions for groups of users, streamlining the process.

## System-Level Roles

Backendless goes a step further by allowing you to assign permissions to system-level roles. This feature is especially handy for managing access between authenticated and non-authenticated users. For example, denying permission to the `NonAuthenticatedUser` role means only users who are logged in can trigger certain flows. 

## Default Permissions

It's worth noting that by default, Backendless sets all roles and users to have permission granted. This default setup ensures that you can test and integrate your automations without any hiccups. Once you're ready to go live, fine-tuning your system's security is straightforward. With just a few clicks in the Backendless Console, you can restrict permissions to only those necessary for your app's operation, adding an extra layer of security and efficiency.

## Changing Permissions in the UI

Setting up permissions for your Backendless Automation flows is a process designed to be as intuitive as possible. By following a few simple steps, you can access the permissions interface and start managing access to your flows. Let's walk through how you can navigate to this interface within the Backendless UI:

<div style="position: relative; padding-bottom: calc(52.583333333333336% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/NUnKG6vd7bMoBp5IUVkX?embed&show_copy_link=true" title="Automations - Browser - Dashboards - Backendless" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>

1. First, head over to the Flow Manager. This is where all your automation magic begins. You'll find a list of the flows you've created, each with its purpose and design to automate tasks within your app.
2. Look through the list for the flow you want to assign permissions to. Once you've found it, you're ready for the next step.
3. Move your mouse over the title bar of the flow you're interested in. As you hover over it, you'll notice several management icons pop up. These icons are your gateway to fine-tuning your flow's settings, including its permissions.
4. Among the icons, you'll see one that resembles a lock. This is the "permissions" icon. Clicking on it will bring up the "Permissions" popup, a dedicated space for managing who gets to do what with your flow.
5. Within the "Permissions" popup, you'll find two tabs:
    - `USER PERMISSIONS`: Use this tab when you want to set permissions for individual user accounts.
    - `ROLES PERMISSIONS`: Select this tab to manage permissions for user roles, affecting all users within a role.
6. Here's where you decide who can call your flow. You'll see icons representing different permission states next to each user account or role. Clicking on these icons will toggle between states:

    - **Gray Checkmark**: This indicates that permission is granted implicitly. It means the permission is inherited from the app-wide settings and hasn't been set explicitly for this flow.
    - **Green Checkmark**: When you see this, it means permission is granted explicitly for this flow. You've specifically allowed this user or role to trigger the flow.
    - **Red X**: This symbolizes denied permission. If you set this for a user or role, they won't be able to invoke the flow.

By toggling these icons, you effectively control access to your automation flows, ensuring that only the right individuals or groups can trigger them. This process is designed to be straightforward, allowing you to secure your app's operations with just a few clicks. 

With these steps, managing permissions becomes a seamless part of your workflow in Backendless, allowing you to maintain the right balance between functionality and security.

Managing execution permissions is a critical step in securing your FlowRunner™. By carefully assigning these permissions, you ensure that your automations are not just powerful and efficient but also safe and under control. Whether you're dealing with sensitive data or just want to keep your workflows running smoothly, taking the time to configure these settings is well worth the effort. And remember, Backendless is designed to make this process as easy as possible, so you can focus on what you do best: building amazing applications.