# Pitches
An application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.   

## Built By [Martin Gathu](https://github.com/martingathu/)

## Description
Pitches is a web application that allow user to post a pitch of any title, be it business ,potitics or lifestyle, he/she can vote or devote other people pitches, add comments on them.

#### You can view the site at: 

## User Stories
These are the behaviours/features that the application implements for use by a user. As a user I would like to:

* See the pitches other people have posted
* Vote on the pitch they liked and give it a downvote or upvote
* Signed in for me to leave a comment
* View the pitches I have created in profile page
* Comment on different pitches
* Submit a pitch in any category
* view different categories


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click on View A rticles on a news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click Read More** | Redirected to the news source's site to read the entire article |
| Go back to news sources | **Click on Global News Highlight** | Redirected to the news source list |
## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv

### Cloning
* In your terminal:
        
        $ git clone https://github.com/martingathu/Pitches
        $ cd Pitches

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python 
        
* Installing Flask and other Modules

        $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
        $ python3.6 -m pip install requests
        
        
* To run the application, in your terminal:
        $ python3.6 manage.py server

## Testing the Application
* To run the tests for the class files:

        $ python3.6 -m unittest discover -s tests
   
## Technologies Used
* Python3.6
* Flask


## License
MIT &copy;2020 [Martin Gathu](https://github.com/martingathu/)