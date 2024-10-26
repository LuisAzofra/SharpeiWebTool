# Rental Earnings Calculator

## Overview

This tool calculates potential earnings from renting a product, providing an estimate of revenue based on
parameters such as **demand**, **price**, and **rental duration**. The application is designed to help users
assess how much they could earn by renting their products under different conditions. Some core functions and
data are kept hidden to protect the underlying business logic in the public codebase.

## Features

- **Revenue Estimation**: Calculate potential earnings based on product demand, rental pricing, and time period.
- **Flexible Parameters**: Adjust parameters to see how different configurations affect rental income.
- **Privacy-Preserving Code**: Key functionalities and data points are hidden to maintain proprietary business insights.

## Project Structure

The main components of the application are organized as follows:

- `AboutUs.vue` - Displays information about the team and the purpose of the tool.
- `Compare.vue` - Allows users to compare potential earnings across different products or settings.
- `ErrorNotFound.vue` - Shows a custom 404 page for navigation errors.
- `LastSearches.vue` - Displays a list of the user's recent searches or configurations for convenience.
- `ProductSearch.vue` - Provides details about available products that can be rented.
- `MainLayout.vue` - Serves as the main layout of the application, coordinating the display of various components.

## Python
Python is used in this project to connect the web tool with Sharpeis DataBase (URL and Keys are hidden) and update it when it is necessary

## Js Files
Used for route bottons and connection between Project Structure
# Quasar App (quasar-project)

A Quasar Project

## Install the dependencies
```bash
yarn
# or
npm install
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)
```bash
quasar dev
```


### Lint the files
```bash
yarn lint
# or
npm run lint
```


### Format the files
```bash
yarn format
# or
npm run format
```



### Build the app for production
```bash
quasar build
```

### Customize the configuration
See [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-vite/quasar-config-js).
