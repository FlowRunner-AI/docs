# Quick Start: A Contact Us Form (with code)

Almost every site has a Contact Us page, and the submission has to reach a human as something readable
rather than a raw blob of fields. This guide builds the flow that does it: a website form posts to your
flow, the flow drops the submitted values into an HTML email template, and sends the result to your inbox.

The substitutions are done here in a few lines of JavaScript. If you would rather not write code at all,
[A Contact Us Form (no-code)](quickstart.md) builds the same thing with one block per placeholder. Neither
is more correct, and a flow can mix both.

Nothing here assumes you have used FlowRunner before. Every block is named, you are told where to find it,
and each field is filled in step by step. It takes about twenty minutes.

!!! note "What you need"
    An email account you can send from. This guide uses Gmail, and step 7 walks through authorizing it.
    Any email extension works the same way.

## The flow you are building

![The flow on the canvas: Start into a Contact Us Form Submitted trigger, then Set Template Text as Variable, then a single Perform Substitutions block running Custom Cloud Code, ending at a Send Email block using Gmail.](../images/learn/quickstart-cloudcode-flow.png)

Four blocks: the form arrives, the template is loaded, one snippet fills in every placeholder, and the
finished HTML is emailed.

## 1. Create the flow

In the left sidebar, hover **Automate ▸ Flows** and click the ((+)) that appears. Give the flow a name -
`Contact Us` - and click ((CREATE)).

![The Create a New Flow dialog with a Name field, an optional Description, and Cancel and Create buttons.](../images/manage/flows-create.png)

The flow opens on an empty canvas with a ((Start)) marker and a dotted placeholder that reads "Drop a block
from right panel here". The panel on the right is where every block lives, grouped into categories:
**AI**, **Triggers**, **Actions**, **Utils**, **Extensions**, and more. You build a flow by dragging blocks
from there onto the canvas.

## 2. Add the block the form will post to

A flow does not have to start with a schedule or a button. This one starts when your website posts to it,
which is what an [External Callback](../reference/external-callback.md){.fr-block} trigger is for.

1. In the right panel, expand the ((TRIGGERS)) category.
2. Drag ((External Callback)) onto the dotted placeholder next to ((Start)).
3. With the block selected, its settings appear in the right panel. Type `Contact Us Form Submitted` into
   the ((Name)) field at the top.

Naming blocks is not decoration. The name becomes how you refer to this block's data later, so a good name
now saves confusion in every step that follows.

![The block palette with the Triggers category expanded, showing the External Callback block ready to drag onto the canvas.](../images/learn/quickstart-palette-trigger.png)

## 3. Copy the address the form will post to

When you select a block, the interface displays its settings in the panel on the right. Select the
`Contact Us Form Submitted` block and you will find ((Callback URL)) - a generated web address with a copy
button beside it. This address belongs to *this trigger*. A flow can hold several callback triggers, and
each one gets its own distinct URL.

Copy it, and set it as the form's submit target on your website.

Below the URL, notice ((Reference Trigger Data As)). Whatever the trigger receives becomes available in the
flow under this name. The alias name defaults to the block's name with "Data" on the end -
`Contact Us Form Submitted Data`. That is the name you will look for whenever a later step needs one of the
submitted fields.

![The External Callback block selected, its settings showing the generated Callback URL with a copy button.](../images/learn/quickstart-callback-url.png)

## 4. Send one test submission (optional, but it makes the rest easier)

The trigger does not know what fields your form sends until it has seen one submission. You can skip this
and type field names by hand later, but letting the trigger learn them means you pick fields from a list
instead of guessing.

Turn on ((Learning Mode)) using the purple callback icon on the block's hover toolbar:

![The External Callback learning mode button.](../images/learn/quickstart-learning-mode.png)

Once the learning mode is activated, send one sample submission to the Callback URL. Any of these works:

=== "From your form"

    Submit the live form once with real-looking values. Best if the form is already wired up.

=== "With curl"

    ```bash
    curl -X POST '<paste your Callback URL here>' \
      -H 'Content-Type: application/json' \
      -d '{"name":"Dana Meyer","email":"dana@example.com","subject":"Question about pricing","phone":"+1 555 0134","message":"Do you offer annual billing for small teams?"}'
    ```

=== "From a browser tool"

    Paste the Callback URL into a request tool such as reqbin.com, set the method to POST, set the body
    type to JSON, and paste the following JSON:

    ```json
    {
       "name": "Dana Meyer",
       "email": "dana@example.com",
       "subject": "Question about pricing",
       "phone": "+1 555 0134",
       "message": "Do you offer annual billing for small teams?"
    }
    ```

Once a sample arrives the icon turns green. Click it to see what was captured - name, email, subject,
phone, and message, each with its value and type. Those five fields are now pickable everywhere in this
flow.

![The trigger's Result Structure popup listing the learned fields - name, email, subject, phone, and message - each with its value and type.](../images/learn/quickstart-learned.png)

## 5. Put the email template into a variable

Your email is one long piece of HTML with gaps in it. You need somewhere to keep that text while the flow
works on it, and that is what a **variable** is: a named value the flow holds for the length of a run.

1. In the right panel, expand ((UTILS)) and drag [Set Variables](../reference/set-variables.md){.fr-block}
   onto the canvas, below the trigger.
2. **Connect it to the trigger.** The first block joined itself to ((Start)) because you dropped it on the
   placeholder. This one landed on open canvas, so nothing runs it yet. Hover the trigger block to reveal
   its action icons. The ((chain)) icon in the lower-right corner is the one that connects a block with its
   successors. Click the icon and drag onto the Set Variables block. A line joins the two.

![Connecting two blocks: the upstream block hovered so its action icons are showing, with a line being dragged from the chain icon in its lower-right corner onto the next block.](../images/learn/quickstart-connect.png)

That line represents the flow's execution path. It sets the order things happen in: the run finishes one
block, travels along the line, and starts the next. A block sitting on the canvas with nothing connected
into it never runs at all, and the flow will report an error rather than start. You will draw one of these
after every block you add from here on.

Now configure the block:

1. Name it `Set Template Text as Variable`.
2. Leave ((Data Bucket)) as `Default`.
3. Under ((Perform Changes)), a row asks for a ((Name)) and a ((Value)). Type `TEMPLATE` as the name.
4. For the value, click the wand icon at the right edge of the ((Value)) field. This opens the
   **Expression Editor** - the dialog FlowRunner uses everywhere a field can hold something more than
   typed text. You will use it again in the next step to pick form fields; for now you only need to type
   into it.
5. Paste your HTML into the editing area and click ((APPLY)).

The template is ordinary HTML with placeholders where the submitted values belong - `{name}`, `{email}`,
`{subject}`, `{phone}`, and `{message}`.

??? example "The HTML template used here"
    Placeholders appear more than once on purpose - `{email}` is both the address shown and the target of
    the Reply button, and `{subject}` appears in the subject bar and in that button's link.

    ```html
    <table role="presentation" width="600" style="background:#ffffff;border-radius:8px;">
      <tr>
        <td style="background:#16213e;padding:16px 40px;">
          <p style="margin:0;font-size:13px;color:#7f8fa6;">Subject</p>
          <p style="margin:4px 0 0;font-size:15px;font-weight:600;color:#e8e8e8;">{subject}</p>
        </td>
      </tr>
      <tr>
        <td style="padding:32px 40px 24px;">
          <table role="presentation" width="100%">
            <tr><td width="100">Name</td><td>{name}</td></tr>
            <tr><td>Email</td><td><a href="mailto:{email}">{email}</a></td></tr>
            <tr><td>Phone</td><td><a href="tel:{phone}">{phone}</a></td></tr>
          </table>
        </td>
      </tr>
      <tr>
        <td style="padding:24px 40px 32px;">
          <p style="margin:0;line-height:1.7;color:#333333;">{message}</p>
        </td>
      </tr>
      <tr>
        <td style="padding:8px 40px 36px;">
          <a href="mailto:{email}?subject=Re:%20{subject}">Reply to Lead</a>
        </td>
      </tr>
    </table>
    ```

Single braces are deliberate. FlowRunner's own expressions use double braces, so single-brace placeholders
stay plain text and are not mistaken for something the editor should work out.

![The Set Variables block's settings: Data Bucket set to Default and a Perform Changes row with the name TEMPLATE, its value holding the HTML template.](../images/learn/quickstart-template.png)

![The Expression Editor open on the Set Template Text as Variable block's Value field: a Block Data tab listing Contact Us Form Submitted Data, a Variables tab beside it, the HTML template pasted into the editing area with its single-brace placeholders visible, and an Apply button.](../images/learn/quickstart-variable-value.png)

## 6. Fill in every gap with one code block

Now the substitutions. A [Custom Cloud Code](../reference/custom-cloud-code.md){.fr-block} block runs a
snippet of JavaScript on the server as one step of the flow. It gets a fresh sandbox on every run, so
nothing carries over between runs, and it has no network access - it works on what you hand it and returns
a value.

That last part is the bit to hold on to. The block does not reach into the flow and help itself to data.
You pass values in by name, your code returns one value, and that returned value becomes the block's
result.

1. From the ((ACTIONS)) group, drag ((Custom Cloud Code)) onto the canvas after the Set Variables block,
   and connect the two by dragging from the Set Variables block's ((chain)) icon. Name it
   `Perform Substitutions`.
2. Click ((Open Code Editor)). Everything else happens in the window that opens: the arguments you pass in
   are declared down the left side, and the code that uses them goes in the editor on the right.

Start with the arguments. Click ((ADD ARGUMENT)) twice and fill in the two rows. Each pairs a **name** with
a ((Value)) expression - click the wand to pick it - and that name becomes a ready-made variable inside
your code:

| Argument name | Value to pick |
| --- | --- |
| `template` | the `Default - TEMPLATE` variable |
| `form` | `Contact Us Form Submitted Data` |

Values arrive as the types they already were, so `form` is a real object and `form.name` reads straight off
it.

![The Code Editor window: on the left an Arguments panel holding two arguments - template bound to the Default - TEMPLATE variable and form bound to Contact Us Form Submitted Data - with an Add Argument button below; on the right the empty code area, and Cancel and Apply buttons at the bottom.](../images/learn/quickstart-code-arguments.png)

Now the code. Click into the editor on the right and write the substitutions:

```javascript
// "template" is the HTML you stored, "form" is what the visitor submitted
return template
  .replaceAll("{name}", form.name)
  .replaceAll("{email}", form.email)
  .replaceAll("{subject}", form.subject)
  .replaceAll("{phone}", form.phone)
  .replaceAll("{message}", form.message);
```

Use `replaceAll`, not `replace`. Given a plain string to search for, `replace` swaps only the **first**
occurrence - and `{email}` appears three times in this template, once in the contact details and twice in
the Reply button's link. With `replace`, that button would still be pointing at `{email}` when the email
went out.

Click ((APPLY)) to close the window and keep both the arguments and the code.

![The Code Editor window with the substitution code written in the editor on the right, beside the two arguments it uses.](../images/learn/quickstart-code-editor.png)

Whatever you return becomes the block's result, published under the alias in
((Reference Result Data As)) - `Perform Substitutions Result` if you leave it at the default. That is the
finished HTML, and it is what the email step reads.

!!! tip "One block here, five in the no-code version"
    Each substitution is one line, and a sixth placeholder means one more line. The
    [no-code version](quickstart.md) spends a block per placeholder instead, which puts every substitution
    on the canvas where someone who does not read code can see and test it. Choose based on who maintains
    the flow.

## 7. Send the email

1. In the right panel, expand ((Extensions)), find **Gmail**, and drag its ((Send Email)) block onto the
   canvas after the code block. Connect the two, the same way as before.
2. **Sign in to Gmail.** The block needs permission to send as you, so it shows an ((OAuth Connection))
   field reading `OAuth Connection is required`. Click ((ADD ACCOUNT)); FlowRunner sends you to Google to
   sign in and approve the access, then saves the result as a connection and selects it here.
3. Set the recipient to wherever contact requests should land.
4. For the subject, open the Expression Editor and pick `subject` from `Contact Us Form Submitted Data`.
5. For the body, pick `Perform Substitutions Result` - the finished HTML your code returned.
6. Make sure the body is sent as HTML rather than plain text, so the template renders.

![A block's OAuth Connection field: a Select active connection picker reading "OAuth Connection is required", with MANAGE and ADD ACCOUNT buttons beside it.](../images/platform/oauth-connections-add-account.png)

You sign in once. Every other Gmail block in this flow picks the connection up on its own, and in any other
flow in the workspace it is there to choose without signing in again. See
[OAuth Connections](../platform/oauth-connections.md).

## 8. Run it

Set the flow LIVE using the toolbar above the canvas. Learning Mode let you send that one sample while
you were still building, but real submissions need a published flow: until the version is LIVE, a form
posting to the Callback URL starts nothing.

Now submit the form for real. Open the ((Instances)) tab and you will see the run, with a tick against every
block that finished and a summary telling you it completed without errors.

![The Instances tab for a completed run: the four blocks each marked done on the canvas, an Instance Summary reading Status COMPLETED with no errors, and an Element Execution Details panel showing the selected trigger's Input and Output - the five submitted fields, name through message.](../images/learn/quickstart-code-instance.png)

Selecting a block shows its ((Input)) and ((Output)) side by side in ((Element Execution Details)). Above,
the trigger is selected, so the output is the five fields the form submitted. Select
`Perform Substitutions` and you see the template going in and the finished HTML coming out - which is where
you look first if a placeholder survives into the sent email.

## What to try next
<!-- doclint: no-shot: a list of onward routes, not a scenario; each destination shows its own screens -->

- **Give the code more to do.** Validate the submission, normalise the phone number, or derive a priority
  from the message before the email goes out. It is all the same snippet.
- **Route it instead of just sending it.** Send billing questions somewhere different from sales ones with
  [Routing on a Value](../build/flow-control/routing.md), or let an
  [AI Router](../reference/ai-router.md){.fr-block} read the message and decide.
- **Do not lose a submission when Gmail is down.** Catch the failure and retry or record it. See
  [Handling Errors](../build/flow-control/error-handling.md).

## Related

- [Custom Cloud Code](../reference/custom-cloud-code.md){.fr-block} - arguments, the code editor, what the
  sandbox can and cannot do, and using a snippet as an AI agent tool
- [A Contact Us Form (no-code)](quickstart.md) - the same flow with a block per placeholder
- [External Callback](../reference/external-callback.md){.fr-block} - the trigger, its Callback URL, and
  Learning Mode in full
- [Expression Editor](concepts/expressions.md) - picking the values you bind to arguments
