# Picisition #
## Description ##

Picisition is a "hot-cold guessing" game built on the Jetson orin nano to be using detectNet image detectNet and GloVe word embeddings.
This game aims to be a lovely morning brain teaser, making the brain work and getting the player out and about.

## Supported Systems

Jetson orin nano: version 1.0.0

## Quickstart ##

#### Pre Requirements ####

* Allow for around 200MB of space on your Jetson for final setup file size
* Have at least 8GB of memory to run detectNet model
* Have Jetson Inference installed on your nano. You can find the repository [here](https://github.com/dusty-nv/jetson-inference.git)

#### Steps ####

Clone the repository

```bash
git clone https://github.com/BrightonGannaway/Picisition.git
```

Download dependencies needed

```bash
pip install requirements.txt
```

> [!WARNING]  
> This repository uses an older version of numpy to support its functionality. If an error is raised,
> you might need to install an older version of numpy. 
> Run the command:
> ```bash
> pip uninstall numpy
> pip install numpy==1.21.5
> ```

Load GloVe word embeddings file and vectors
```bash
python3 image_game/docs/download.py
```

Wait and after some time you should have two files in the project directory: `glove_100d.kv.vectors.npy` (~152MB) and `glove_100d.kv` (~11MB). Move these folders to `bin` or create `bin` and move them if there is no such directory

Congrats! You have successfully installed Picisition. Before you begin make sure you 
are connected to a monitor and a camera to play. Run the game by running the command:
```bash
python3 image_game/src/main.py
```
__Good Luck and Have Fun__

## How To Play ##

Make sure you are connected to a monitor and camera before you begin.

Start the game by running:
```bash
python3 image_game/src/main.py
```

 - **Setup**: A random object will be chosen randomly from a list of COCO classes <br>
 - **Goal**: Find this object by taking pictures of other objects <br>
 - **Gameplay**: With each picture you take a percentage will be given. The higher the percentage, the higher the similarity to the goal.

To take a picture of an object, simply press "capture", wait a couple seconds, and you will have a relation percentage. 
Keep guessing until you find the goal. 

Once you found the target, you can play again by clicking: "New Object Target"

---

## The Making ##
---
### The Idea ###

**Starting Out**: Obtaining a fresh Jetson nano, and after learning its capabilities, I wanted to create something fun and interactive. A starter project that would
teach me how to work with the computer and share a fun project. Thus, the idea of Picisition (Pik-eh-zi-tion) was born. A simple game that would could see 
on the New York Times games. This working model here, is the start to a grander project that will expand my knowledge 10 fold.

**Finding Purpose**: Even though this project is a game, it allows people to go out and about, exploring their local environments. Through this project, people who desire to go around, as well as those who simply want a classic morning challenge will get to experience a game that incorporates the real world.

**The First Vision**: Unlike the game, the target was very much in sight, yet it was the engineering, structure, and dependencies that were in the dark. The first implementations were implementing detectNet. DetectNet was chosen for a couple of reasons:
- The average user will play in a variable setting
- DetectNet has more accuracy across such chaotic settings
- Even so, we could use the area feature of detectNet to get the most prominent object
- It would be funny if the target was in the frame, and perchance in the future, we could give a hint that the target was in the photo

A simple GUI using tkinter was a straightforward decision. However, the first versions of a object relation calculator was using an API to call 
a prompted llama3 model using open webui. You will be able to find such an API in previous commits or in a gist [here](https://gist.github.com/BrightonGannaway/eba585f74b0aa9bc511f74f93646f206). After implementing everything and testing each part individually things were moving along, until I combined them.

---
### Challenges

#### __Too Much Processing not Enough Memory__
---
**Problem**: Using both detectNet and llama3 was to constricting on my RAM usage. This impeded development 
as the Jetson kept running out of memory to even support basic processes such as a SSH connection. 

**Solution**: After a tough day, I researched solutions. What I came across was a technology called word embeddings, that, with vectors, could determine the relation between two words using a cosine function. This reduced memory usage drastically. Testing models such as GloVe, NumberBatch, FastText and a different technology called sentence transformers using sBERT. Landing on GloVe due to its better accuracy in relations, a final challenge was to be overcome, the speed. It took long to load the embedding model. This was simply solved by converting the model to a binary and having the program load that instead, reducing lookup times, and memory writes.

#### __Worked Half the Time__
---
**Problem**: Every other image capture failed.

**Solution**: After much debugging and looking at error messages, the error arise based off of a trouble with an invalid openGl or DirectX context (error 219). As a result,
I decided to remove dependencies revolving around VideoSource and VideoOutput instead moving towards simpler methods. The most current version uses `loadImage` something I should have used at the start.

---



