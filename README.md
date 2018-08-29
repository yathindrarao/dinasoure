# T-Rex game Bot
As you observe in the video the game is being played automatically by the computer itself and when we stop running the code the dinosaur dies. To do this I mainly focused on capturing the screen and givng the coordinates to the dinosaur (i.e in the form of pixels).
After that I created a box of size length 40 and height 32(you can see in the code that the box is placed 50 pixcels after the dinosaur)
then I stored the color each point in the box and stored it in the form of array using grayscale.As when the whole box is white the sum each value in the array will be having a fixed value and when the colour changes some values in array changes and the difference can be seen by computing the sum of array( when single value in the array changes the sum of array also cahnges). 
In this way when there is a change in sum of array then we will call 'PressSpace' and there will be jump.
In this way you can make it automatic.
