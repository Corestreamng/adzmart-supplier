# Overview
At the core of Adzmart are the unit inventory that we'll be maintaining and selling. 

## Unit Types
A list of different unit types that we'll maintain on the platform. To start out, a unit type will include the following fields:
1. name
2. description


## Unit
A unit is the place where ads are shown to users. The unit include different information including the format, type, direction it's facing, location etc.
A collection of these units is called the inventory or catalog.

The following initial fields will be captured for a unit:

| Field        | Description                                                   |
| ------------ | ------------------------------------------------------------- |
| Name         | We can make this required for now                             |
| UnitType     | The unit type                                                 |
| Supplier     | We'll store this as a text now, and revisit this model        |
| Display name | Optional string value                                         |
| Adzmart Hash | We will generate a hash from some values TBD                  |
| Reference ID |                                                               |
| Billboard ID |                                                               |
| Latitude     | Required                                                      |
| Longitude    | Required                                                      |
| District     |                                                               |
| State        |                                                               |
| Postal Code  |                                                               |
| Country      |                                                               |
| Facing       | An enum of N,S,E,W, NE, NW,SE, SW                             |
| Description  |                                                               |
| UnitInfo     | A json representation of additional info specific to the unit |
|              |                                                               |

```
Note: We'll be expecting these headers in the excel sheet (Grid) that will be uploaded.
```
