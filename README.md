# Airbnb Clone Collaboration Project
 Welcome to the Airbnb Clone console project!!.

## Introduction
This is a joint endeavor between Felicity Essien and Dennis Makaka aimed at developing a simplified version of the popular accommodation rental platform, Airbnb. The aim is to create a command-line Interface application that replicate some of the core functionalities of Airbnb, such as property listing, booking management, and user interaction among others.

## Project structure
 
 The project follows a structured file organization:

### airbnb-clone
 - models/
	- init.py
	- base-model.py
	- user.py
	- amenity.py
	- property.py
	- booking.py
	- review.py
	- location.py
	- host.py
	- guest.py
	- *other modules*
 - tests/ 
	- init.py
	- test-base-model.py
	- test-user.py
	- test-amenity.py
	- *other modules*
 - console.py
 - file-storage.py
 - README.md

* `models/`: Contains Python modules related to Airbnb objects.*
* `tests/`: Holds unit test files organized based on the project structure.*
* `console.py`: The command interpreter script.*
* `README.md`: This file providing information about the project.*
* `file_storage.py`: The file storage engine script.*

## Collaboration
 *Felicity Essien and Dennis Makaka will collaborate closely throughout the development process. They will divide tasks based on their individual strengths and expertise, regularly communicate progress, and provide feedback to each other to ensure the project's success.

 <u>Collaborators:</u>
	1. Felicity Essien - Github: [felabel](https://github.com/felabel/felabel.git)
	2. Dennis Makaka - Github: [DennisMakaka] (https://https://github.com/DennisMakaka)

## Usage
 Run the command interpreter:
 _python3 console.py_ or _./console.py_

## Testing
 To run all unit tests use the following command: 
 _python3 -m unittest discover tests_

 To test individual files use:
 _python3 -m unittest tests/test_models/...._





