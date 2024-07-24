# ChatWithSPIKE
Web based tool for communicating with LEGO's SPIKE Robotics kit over ChatGPT.

## SPIKE-Chat Quickstart. Developed by Richard Geoghegan: rpgeoghegan@gmail.com

1. Connect SPIKE to laptop via USB.

2. Locally host index.html on your computer within this folder. This can easily
   be done using the Live Server extension on VS code. But any other locally
   hosted webpage should work.

3. Host under 127.0.0.1:5500 or else you won't be able to chat with the
   Firebase server.

4. Open Chrome and go to 127.0.0.1:5500. Hit connect and choose
   SPIKE prime in the popup.

5. Hit the 'upload documentation' button and wait for it to finish.

6. Start chatting with SPIKE!

7. If you wish to upload any additional files/documentation to the device,
   include them in the folder SPIKE-Documentation. Next, include the relative
   file path into the files array on line 433 of javascript/chat.js. 
   E.g. 'doc_function.py', or 'modules/color_matrix.py' to include a file in a
   subdirectory.
