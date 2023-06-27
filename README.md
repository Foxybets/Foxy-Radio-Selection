# Foxy-Radio-Selection
## Radio guide, search for world favorite radio stations as a background while you work, study or just relax

###Video Demo: [URL HERE]

##Description:

###The Foxy Radio Selection project is a Python application that allows users to search for and play radio stations based on their preferred genre. It provides a user-friendly graphical interface where users can enter a genre, click the search button, and get a list of radio stations matching that genre. They can then double-click on a station to play it.


##Files

###*project.py: This is the main file of the project that contains the code for the Foxy Radio Selection application. It imports necessary libraries and defines various functions for retrieving radio stations, playing stations, searching stations, displaying weather information, and setting up the graphical user interface (GUI). The main function is responsible for running the program.

*images/background.png: This folder contains a background image file that is used to enhance the visual appearance of the application's GUI.

*config.json: This file stores the API key required for retrieving weather information. It is read by the project.py file to access the API key.

*requirements.txt: This file lists the necessary libraries and their versions required for running the project. You can use the pip install -r requirements.txt command to install these dependencies.

*test_project.py: This file contains the test cases for the functions implemented in the project.py file. It uses the pytest framework to execute the tests and ensure the correctness of the project's functionality.

*readme.txt: This file provides a short description of the project and outlines the steps to use it. However, the README.md file you are currently reading is a more comprehensive and detailed documentation of the project.

##Design Choices

###*Logging: The project utilizes the logging module to create log files (app.log) that record the application's activity. The log files store information about API requests, errors, and other relevant events, which can be helpful for debugging and troubleshooting.

*API Integration: The project integrates with two external APIs. It uses the Radio-Browser API to retrieve radio stations based on the provided genre. Additionally, it utilizes the OpenWeatherMap API to fetch current weather information based on the user's location. These APIs enhance the functionality and user experience of the application.

*Graphical User Interface (GUI): The project employs the Tkinter library to create an interactive GUI for the Foxy Radio Selection application. The GUI provides an intuitive interface for users to input the genre, view search results, and interact with radio stations.

##How to Use

###To run the Foxy Radio Selection project, follow these steps:

Install the required dependencies listed in the requirements.txt file using the command: pip install -r requirements.txt.

Ensure that the config.json file contains a valid API key for the OpenWeatherMap API. If you don't have one, you can obtain it by creating an account on the OpenWeatherMap website and generating an API key.

Execute the project.py file using a Python interpreter: python project.py.

The Foxy Radio Selection application window will open, presenting you with a graphical interface.

Enter a genre in the provided text field and click the "Search" button to retrieve radio stations matching the genre.

The list of stations will appear below the text field. Double-click on a station to play it.

You can click the "Clear" button to reset the genre input field.

To display the current weather information, click the "Show Weather" button. A separate window will appear, showing details such as temperature, condition, pressure, wind speed, and wind direction.

Enjoy exploring and listening to your favorite radio stations!

##Debated Design Choices

###During the development of the Foxy Radio Selection project, several design choices were considered and debated. Here are some of the notable decisions:

*GUI Framework: Tkinter was chosen as the GUI framework due to its simplicity and compatibility with Python. It provides the necessary functionality to create a responsive and visually appealing interface.

*Weather Display: The decision to display the weather information in a separate window was made to keep the main application window uncluttered and focused on radio station search and playback. By separating the weather display, users can access weather information when desired without overwhelming the main interface.

*Logging Level: The logging level was set to DEBUG to capture detailed information about the application's activity. This level of logging can be helpful during development and troubleshooting, as it provides insights into API requests, errors, and other events.



