# Anime Recommendation

<h3>Hi everyone,</h3>

This is my mini-project. I was a second-year student in a Data Mining course. My project is about recommending anime on a website using K-nearest neighbors (KNN) to make recommendations.

<h3>About my project !</h3>

My datasets and images from [MyanimeList](https://myanimelist.net/).

I created the model using Jupyter, and I have uploaded all of my code to Google Colab [Click](https://colab.research.google.com/drive/1YGCNVizuTujnL4ZK2Nx35TGdcvIonIy0?usp=sharing).

I created the website using Svelte for the frontend and Flask for the backend.

<h3>How to use?</h3>

* First you want to download [backend.zip](https://www.dropbox.com/s/apyoabvieotk13s/backend.zip?dl=0), clone the frontend from main branch and the backend from backend branch
* Once you have done this, you will have two folders - frontend and backend. You have to navigate to the backend folder and unzip the backend.zip file there.
* Next, you need to open a new terminal and run the command `npm install` to install the necessary packages
* Then, you should edit the `src/lib/path_url.ts` file and change the URL variable to your IP address.
* Run the command `npm run build` to build project.
* In the backend folder, you need to install the required packages by running the command `pip install -r requirements.txt`
* Finally, to start the project, navigate to the frontend folder and run the command `npm start` in one terminal window and run the command `python app.py` in another terminal window to start the backend.
