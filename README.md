# ChatWithSPIKE
##### Web-based tool for communicating with LEGO's SPIKE Robotics kit over ChatGPT.

**Developed by Richard Geoghegan: rpgeoghegan@gmail.com**

## Introduction

This tool is unique because ChatGPT cannot write code for LEGO's SPIKE on its own, as LEGO frequently updates the firmware, making online-generated code often out of date. ChatWithSPIKE addresses this by instructing ChatGPT to query the SPIKE device itself for documentation. The 'upload documentation' button pushes the documentation for SPIKE Prime 3 directly onto the SPIKE device. This ensures that the code generated and used is always current and compatible with your SPIKE kit. By leveraging this real-time querying, ChatGPT can effectively utilize its coding skills to interact with the SPIKE Robotics kit through this platform.

**Note:** You will need to connect to your own ChatGPT API, as this guide does not include an API token to avoid billing issues. However, the principles of connecting and using the API remain the same.

## SPIKE-Chat Quickstart

1. Connect SPIKE to your laptop via USB.

2. Locally host `index.html` on your computer within this folder. This can easily be done using the Live Server extension on VS Code, but any other locally hosted webpage should work.

3. Host under `127.0.0.1:5500` or else you won't be able to chat with the Firebase server.

4. Open Chrome and go to `127.0.0.1:5500`. Hit connect and choose SPIKE Prime in the popup.

5. Hit the 'upload documentation' button and wait for it to finish.

6. Start chatting with SPIKE!

7. If you wish to upload any additional files/documentation to the device, include them in the folder `SPIKE-Documentation`. Next, include the relative file path into the files array on line 436 of `javascript/chat.js`. 
   E.g. 'doc_function.py', or 'modules/color_matrix.py' to include a file in a subdirectory.
