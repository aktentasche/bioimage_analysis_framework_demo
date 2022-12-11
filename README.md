# bioimage_analysis_framework_demo
Demo application for the position Python programmer at Danish BioImaging Infrastructure Image Analysis Core Facility (DBI-INFRA IACF)


# Prerequisites

The code in this repository is only known to run on Linux but Windows and Mac should in principle work as well if below requistes are installed.

Feel free to submit an issue or drop me an email if you have problems setting things up .

1. [Python 3.10+](https://www.python.org/)
2. [poetry version 1.2.2+](https://python-poetry.org/docs/#installing-with-the-official-installer)
3. [Node 18.12.1 LTS](https://nodejs.org/en/)
4. [VSCode](https://code.visualstudio.com/)


# Installation / Library download
The framework is not really installed but rather the required libraries are download using poetry and npm.
All commands have to be executed in the repository root.

Download python libraries for the virtual environment:

```
poetry install
```

Download node modules for web frontend development:

```
cd frontend
npm install
```

# Development

The below hints how to start developing different parts of the framework refer to a Linux machine and VSCode. 
If you use a different environment things might be different.



## Web frontend
To start the Quasar development server:

1. Press **Ctrl+Shift+P**
2. Select **Run Task**
3. Select **quasar-dev**

Note: the quasar-dev task is defined in .vscode/tasks