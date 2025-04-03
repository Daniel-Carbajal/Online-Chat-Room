# Online-Chat-Room
This is a simple personal project I worked on that utilizes Flask and SocketIO in Python for an online chatroom. This was also my first time using CSS for styling. For the styling, I followed an @techwithtim tutorial! 
This project utilizes Python, HTML, JavaScript, and CSS

# app.py
This project introduced me to the Flask and SocketIO API in Python. 
My use of Flask in the project was to route my chatroom to a URL so that it can be accessed as a website. With further and simple implementation of ngrok as well, this chatroom can allow you to chat with anyone from anywhere.
My implementation of SocketIO was necessary for listening for specific events from users, and performing events appropriately. More specifically, it listens for things like users connecting to a room, disconnecting, pressing buttons, and sending messages. When the socket hears those events, the program will handle them and send data back between the client and server.

# templates (HTML)
Despite having a basic understanding of HTML prior to this project, I had never utilized it personally, so this was another learning curve for me. I became a lot more familiar with the possible formatting options it provides.
  ### base.html
  This is essentially series of initializations which extends to home.html and room.html. It initializes the route to the CSS style the website will use, UTF-8, as well as the script language(JavaScript) I use to communicate to the server when client end events occur such as buttons being pressed.
  
  ### home.html
  This is the formatting for the homepage of the chat room website. It includes the title text, user text inputs for name and room code, buttons for joining or creating a room, and text for potential errors the user should see. 
  It can communicate to the server to reroute the client to a room.html in the event that they join or create a room.
  
  ### room.html
  This is the formatting for the rooms of the chat room website. It includes the title and room code texts, the message box with time stamps, user text input, and a send message button. 
  This can also send data to the server in the event that a user leaves the chat room. 

# static(CSS Styling)
This was my first time doing any CSS, so I was unfamiliar with the language and its uses. I followed a @techwithtim YouTube tutorial and got some-what familiar with how it can be utilized to style website visuals and format!
