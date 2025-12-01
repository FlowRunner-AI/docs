---
icon: material/function-variant
---
# Developing an Action with Arguments

This guide builds on the [Basic Action Guide](./basic-action-js.md) and extends the **Get Top Headlines** operation by adding input parameters. You will learn how to define and use arguments, making your FlowRunner™ actions more flexible and adaptable to dynamic input.

## What Are Action Arguments?

Action arguments allow you to pass external data into your action when it is executed. Flow designers can supply argument values using static inputs, outputs from other actions, transformation operations, trigger events, or variables.

When you define arguments, you also control how they appear in FlowRunner™. You decide the data type, whether they are required, and how users interact with them—such as text fields, dropdowns, or checkboxes.

In this guide, you will define two arguments, integrate them into your action’s logic, and test the result in FlowRunner™.

## What This Guide Covers

In this guide, you will create a new **Search News Headlines** action with two parameters: **category** and **q** (query). Both are supported by the [NewsAPI.org Top Headlines API](https://newsapi.org/docs/endpoints/top-headlines):  
![newsapi documentation](../images/newsapi-doc.png)

Once implemented, the **category** argument will appear in FlowRunner™ as a dropdown list with predefined values, while **q** will be a free-form text input field. Both parameters will also accept dynamic values through the [Expression Editor](../flow-editing/expressioneditor.md).

!!! note
    In FlowRunner™, any parameter can accept values via the Expression Editor. This makes connecting and transforming data between actions seamless.

## Implementing the Operation

Arguments in your Node.js action function behave like typical JavaScript function parameters. However, to make them available as configurable inputs in FlowRunner™, you must define them using special `@paramDef` JSDoc tags.

Here is the complete action function, followed by a detailed breakdown of the argument declarations:

```js linenums="1"
/**
 * @description Retrieves top news headlines for a category and/or a search query
 *
 * @route GET /getNewsWithCategoryOrQuery
 * @operationName Search News Headlines
 * @appearanceColor #FE1212 #191970
 * @executionTimeoutInSeconds 120
 * @paramDef {"type":"String","label":"Search Query","name":"query","required":false,"description":"Keywords or a phrase to search for."}
 * @paramDef {"type":"String","label":"News Category","name":"category","required":false, "uiComponent": {"type":"DROPDOWN", "options":{ "values":["business", "entertainment", "general", "health", "science", "sports", "technology"] }}, "description":"The category you want to get the headlines for."}
 * @returns {Object} Returns news headlines from the specified category and/or a search query.
 * @sampleResult {"status":"ok","totalResults":1,"articles":[{"source":{"id":"the-hill","name":"The Hill"},"author":"Tara Suter","title":"West Virginia governor says he’ll take legal action against NCAA over tournament snub - The Hill","description":"West Virginia Gov. Patrick Morrisey (R) on Monday said he will take legal action against the NCAA over West Virginia University’s (WVU) snub from the March Madness tournament. “I’ve asked Attorney General [JB McCuskey] to launch an investigation into the NCAA…","url":"https://thehill.com/homenews/state-watch/5199135-west-virginia-governor-says-hell-take-legal-action-against-ncaa-over-tournament-snub/","urlToImage":"https://thehill.com/wp-content/uploads/sites/2/2024/11/AP24131791907837-e1730586407708.jpg?w=1280","publishedAt":"2025-03-17T19:51:12Z","content":"Skip to content..."}]}
 */
async getNewsWithCategoryOrQuery(query, category) {
  try {
    let requestQuery = {
      country: 'us',
      apiKey: this.apiKey
    }

    if (category) {
      requestQuery.category = category;
    }

    if (query) {
      requestQuery.q = query;
    }

    return await Backendless.Request['get']('https://newsapi.org/v2/top-headlines')
      .set({
        'User-Agent': 'FlowRunner™'
      })
      .query(requestQuery)
  } catch (error) {
    logger.error(`NewsAPI - error: ${error.message}`)
    throw error
  }
}
```

## Defining Parameters with `@paramDef`

As shown in the code, function arguments behave like typical parameters in JavaScript. To make them visible in FlowRunner™ as input fields, define them using the `@paramDef` tag:

```js linenums="8"
* @paramDef {"type":"String","label":"Search Query","name":"query","required":false,"description":"Keywords or a phrase to search for."}
* @paramDef {"type":"String","label":"News Category","name":"category","required":false, "uiComponent": {"type":"DROPDOWN", "options":{ "values":["business", "entertainment", "general", "health", "science", "sports", "technology"] }}, "description":"The category you want to get the headlines for."}
```

Once declared, FlowRunner™ automatically renders these arguments as form fields:
![search news headlines args in flowrunner](../images/search-news-headlines-args.png)

### Search Query Parameter

The **Search Query** is rendered as a standard text input field. Its configuration is:

```js
@paramDef { 
    "type":"String",
    "label":"Search Query",
    "name":"query",
    "required":false,
    "description":"Keywords or a phrase to search for."
}
```

| Property      | Value                    | Description |
|---------------|--------------------------|-------------|
| `type`        | `"String"`               | The parameter’s data type |
| `label`       | `"Search Query"`         | The label displayed in FlowRunner™ |
| `name`        | `query`                  | The argument’s name in the function signature |
| `required`    | `false`                  | Whether the parameter is mandatory |
| `description` | `"Keywords or a phrase to search for."` | Tooltip shown in FlowRunner™ |

### News Category Parameter

The **News Category** argument is rendered as a dropdown list with predefined values:

```js
@paramDef {
  "type":"String",
  "label":"News Category",
  "name":"category",
  "required":false, 
  "uiComponent": {
    "type":"DROPDOWN", 
    "options":{ 
      "values":["business", "entertainment", "general", "health", "science", "sports", "technology"] 
    }
  }, 
  "description":"The category you want to get the headlines for."
}
```

| Property      | Value                    | Description |
|---------------|--------------------------|-------------|
| `type`        | `"String"`               | The parameter’s data type |
| `label`       | `"News Category"`        | The label displayed in FlowRunner™ |
| `name`        | `category`               | The argument’s name in the function signature |
| `required`    | `false`                  | Whether the parameter is mandatory |
| `uiComponent` | `{ "type": "DROPDOWN", ... }` | Defines the dropdown behavior |
| `description` | `"The category you want to get the headlines for."` | Tooltip shown in FlowRunner™ |

## Rendering UI Components

The **News Category** parameter is shown as a dropdown in FlowRunner™ due to the `uiComponent` property. This property specifies the component `"type"`, which in this case is `"DROPDOWN"`, along with a list of valid `"options"`.  

FlowRunner™ supports various input types for rendering arguments. To explore more UI component options, refer to the [Parameter Rendering](./parameter-ui-types.md) documentation.
