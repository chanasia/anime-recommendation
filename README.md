# Anime Recommendation

<h4>RengMe! website: http://rengme.chanasia.xyz/<h4>

![home](https://drive.google.com/uc?id=1k31QFoPlqBcr2VSsCCr-Dltd46zm6q-T)
![similar anime](https://drive.google.com/uc?id=1aztjtf6dLqwyKkkazTxN1kNFneHIiNqh)

<h3>Hi everyone,</h3>

This is my mini-project. I was a second-year student in a Data Mining course. My project is about recommending anime on a website using K-nearest neighbors (KNN) to make recommendations.

<h3>About my project !</h3>

My datasets and images from [MyanimeList](https://myanimelist.net/).

I created the model using Jupyter, and I have uploaded all of my code to Google Colab [Click](https://colab.research.google.com/drive/1YGCNVizuTujnL4ZK2Nx35TGdcvIonIy0?usp=sharing).

I created the website using Svelte for the frontend and Flask for the backend.

<h3>How to use?</h3>
<h4>Build docker images</h4>

```cli
docker build -f Dockerfile.frontend -t chanasia/rengme:1.0 .
```
```cli
docker build -f Dockerfile.backend -t chanasia/rengme_api:1.0 .
```
<h4>Run docker-compose</h4>

```cli
docker-compose up -d
```


