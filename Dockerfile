# Written by Wyatt J, Miller
# For Docker Python 3 demo

# Pull image from Docker Hub
FROM python:alpine3.6

# Set a enviroment variable
# Here, I set the variable work to a Unix directory path
ENV work /usr/bin/app

# Set the working directory, using the work variable I set
WORKDIR ${work}

# Copy the files over to the Docker image, referencing the working directory
# The peroids are the directory we are in right now on the host machine
# and the current working directory in the Docker image respectively
COPY . .

# Exectue our app using Python 3, referencing the working directory
CMD ["python3", "."]
