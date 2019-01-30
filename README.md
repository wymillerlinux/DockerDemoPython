# DockerDemoPython
A Docker Demo for the Python 3.6 image on Docker Hub. Feel free to follow along.
I have wrote this little Python app for fictional medical purposes. It takes name, age, height, weight and saves it to a JSON file and spits output at you. Kind of lame. Anywho, let's begin.

## Installation
Please note these installation instructions are for Ubuntu Linux 16.04 or higher. Email me if you have a different distribution or operating system.

First, you have to install `git`.<br>
`sudo apt install git`<br>

Also, you have to have Docker.<br>
`snap install docker`<br>
`sudo apt install docker.io`<br>

Next, build the image with Docker.<br>
`docker build -t demo02 .`<br>

You call your Docker image however you like by replacing `demo02` with anything.<br>
If you get a permission denied error, add your user to the Docker group.<br>
`sudo usermod -aG docker wyatt`<br>
Replace `wyatt` with your user.<br>

Finally, run your image with the flags `-it`.<br>
`docker run -it demo02`<br>

Follow the on-screen prompts.

## Troubleshooting

Email me with the locally downloaded repo and we'll have a disscusion.
