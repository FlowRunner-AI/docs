The "Save Record in Database" action block in FlowRunner is designed to help you interact with your Backendless database by creating new records or updating existing ones. This block supports three modes of operation: creating a new record, updating a specific record, and updating a collection of records that match a query. 

If you are not familiar with the Backendless Database, it is a cloud-based database service that allows you to store, retrieve, and manage data for your application. It provides a range of powerful features for data management, including real-time data synchronization, advanced querying, and user management.

The block has three modes to support its operations:

## Create a New Record

In this mode, you can create a new record in a specified table. Here's how to configure it:

- **Specify the Table**: Select the table where the new record will be created from a drop-down list of available tables. If the list of tables changes, you can refresh it by clicking the "refresh" icon.
- **Set Column Values**: Use the "Set Column Values" form to assign values to the columns in the table. Each column can be set to a specific value as needed.

The result of this action is the created record, which is returned in a key/value structure format.

## Update Record from Flow

This mode allows you to update a specific record using the result of an action, trigger, or transform operation. Here's how to configure it:

- **Select the Table**: Choose the table where the record exists.        

- **Select a Record to Update**: Choose a result from any of the previous blocks (action, trigger, transform operation, or variable) that you want to update.

    !!! note
        The Backendless databaase uses a special column called `objectId` which uniquely identifies a record in a table. Make sure the data element you select has the `objectId` property/key with a valid value identifying a record in the selected table.

- **Perform Changes**: Configure the **Perform Changes** form by specifying Property/Value pairs. The "Property" is a column from the selected table, and the "Value" is what will be updated in the record.

The result of this action is the updated record, which is returned in a key/value structure format.

## Update Record with a Query

In this mode, you can update multiple records that match a specific query. Here's how to configure it:

- **Define the Query**: Use the [where clause](https://backendless.com/docs/rest/data_search_with_where_clause.html) syntax to define the query that identifies which records to update.
- **Select the Table**: Choose the table where the query will run.
- **Set Changes**: Define the changes to apply as a collection of Property/Value pairs. Each "Property" is a column from the selected table, and the "Value" is what will be set for the corresponding column in the records identified by the query.

The changes will apply new values to the specified columns for all records that match the query.

## Using the Expression Editor

All fields in the "Save Record in Database" block, including query criteria, and column values are integrated with the [Expression Editor](../flow-editing/expressioneditor.md). This tool makes it easy to link data from other blocks in your flow, ensuring a seamless flow of information and enabling dynamic data manipulation based on the results of previous actions.

## Example Usage

Imagine you need to update the status of multiple orders in your database to "shipped" when a shipping confirmation is received. You could configure the "Save Record in Database" block as follows:

1. **Create a New Record**: If you receive a new order, you can add it to your database by specifying the order details in the "Set Column Values" form.
2. **Update Record from Flow**: When a specific order is updated with shipping information, select the order record from a previous block and update its status to "shipped".
3. **Update Record with a Query**: Use a query to find all orders that have a status of "processing" and update their status to "shipped" once they are confirmed for shipping.

By configuring the "Save Record in Database" block in these ways, you can efficiently manage and update your database records, ensuring that your application data remains accurate and up-to-date.