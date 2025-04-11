# assignment3

In order to run the app, cd into the REPLACE W NAME directory, run docker, and build the image with the command "docker build -f [path] -t [title] ." Replace [path] with a path to the dockerfile (for example, if you've cded into the exact directory you can just use "Dockerfile") and replace [title] with whatever you'd like to call the image, perhaps "notesapp".

Now you have built the image. Next you should run it with the command "docker run -p 5000:5000 -v $(pwd)/instance:/instance [title]" Replace the [title] with the same [title] you used previously (we suggested notesapp).

As the prompt suggest, navigate to http://127.0.0.1:5000/ and enjoy the notebook!
