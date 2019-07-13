# emo

Hello! I'm Navdeep, and I hope you are doing well! In my life, I have noticed some people have hard times reading emotions in all sorts of places. Some have a hard time deciphering emotion from audio, from body language, and some have a hard time reading language in texts. This project is meant to solve the latter of the three, since there seems to be much more research on facial detection and audio analysis. It seems like there is not enough research on text-based emotions, weirdly enough.

I know that some students with autism have a hard time expressing emotions and/or detecting them. This project can help those students slowly condition themselves to understand what "standard responses" to certain emotions can be or look like.

### Running the model

To run the model, you should create a python3 virtual environment in-which you install all of the packages in requirements.txt (using the wonderful pip to do this for you). Then, with the virtualenv activated, run "python3 restServer.py"

After that, open up the index.html file and give it a try!

### More information:

List of emotions: worry (9438) neutral (7978) happiness (5860) sadness (5841) love (3734) surprise (2134) fun (1749) relief (1489) hate (1300) anger (947) empty (758) enthusiasm (737) boredom (177)

Creation of model: I was able to create a model using keras and sci-kit learn in-order to classify multiple phrases/sentences. This model does not do the "easier" thing and stick to simpler classifications such as, "positive, neutral, and negative." The model tries to solve a harder problem. It is not perfect, but it does predict some phrases correctly :) The back-end for this project is in Flask, and the front-end makes use of Ajax/JQuery. One of the biggest problems was trying to get past CORS/cross-scripting requests, but Ajax/JQuery saved the day!

Potential Future Improvements: It is already working quite a bit! But, something that would strengthen our model is to train it on even more data with more emotion/sentiment labels. This would lead to a more robust model that consists of numerous words.
