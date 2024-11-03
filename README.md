# Client Management CLI

This project is a Command Line Interface (CLI) built with Python and the click library, allowing CRUD (Create, Read, Update, and Delete) operations on a client record. Client data is stored in a CSV file, facilitating persistence and easy access to records.

## Features

+ **Create** new client records
+ **Update** a client's information
+ **Delete** client records
+ **List** all clients in the CSV file

## Requirements

+ **Python 3.7+**
+ **click** (installable via pip)

## Installation

Clone this repository:

`git clone https://github.com/faidrn/platzi-ventas.git`

## Usage

The CLI supports various commands to manage client records. You can see the list of available commands by using:

`pv clients --help`

### Available Commands

1. **Create a client**
Adds a new client to the CSV file.
`pv clients create`

2. **Update a client**
Modifies the information of an existing client (requires the client’s ID).
`pv clients update`

3. **Delete a client**
Removes a client from the CSV file using their ID.
`pv clients delete`

4. **List all clients**
Displays all client records in a table format.
`pv clients list`

## Project Structure
![](https://pandao.github.io/editor.md/examples/images/4.jpg)
