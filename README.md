# Speech Converter

## Purpose
#### It speeds up the conversion from speeches in Word documents into Markdown for the [Open Speeches App](https://github.com/lbarberiscanoni/OpenSpeeches)

## Requirements
1. Command Line
2. Python 3.3
3. Dropbox
4. Git

## Set Up
1. Download the script 
  * You can use either Git or manually download the zipfile
  * If you are using Git, then download it with
            git clone https://github.com/lbarberiscanoni/speechConverter.git
2. Put the script in the folder where the speeches you want to convert are 
  * This is somewhere in the Dropbox folder

## Usage
1. Open up the Command Prompt/Powershell (for Windows) or Terminal (for Mac)
  * As a windows user, if you are having issues just follow [this video](https://www.youtube.com/watch?v=7uRnMIsamD0) and proceed on Cygwin
2. Navigate to the directory of the speeches

        cd Dropbox/path/to/folder/where/the/speeches/are
    * Let me clarify that you are not actually supposed to put path/to/folder/where/the/speeches/are, but the actual path from the Dropbox folder to the folder where he speeches are lol
    * Ex. on my computer this is what it looks like
            
            cd Dropbox/Lorenzo/Congress/Speeches/
3. Run the conversion.py script
  
        python conversion.py
4. The rest is explained by the script
5. Once you are done, move your new speeches into the markdown folder
