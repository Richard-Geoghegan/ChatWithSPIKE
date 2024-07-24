# ChatWithSPIKE
##### Web-based tool for communicating with LEGO's SPIKE Robotics kit over ChatGPT.

**Developed by Richard Geoghegan: rpgeoghegan@gmail.com**

## Introduction

When LEGO released firmware version 3 for their SPIKE robotics kit, the existing code for SPIKE firmware 2 no longer worked as intended. This created challenges for generating accurate and up-to-date code for SPIKE, especially since ChatGPT can write MicroPython but not accurately for the latest SPIKE firmware. This can be frustrating for teachers and pupils learning to code SPIKE with generative AI tools.

To address these issues, ChatWithSPIKE allows users to upload the latest documentation directly onto the SPIKE device. This is important because SPIKE runs MicroPython, which lacks docstrings, so this functionality is recreated on the device when the user hits 'upload documentation'. This ensures that ChatGPT can always generate code using the most current syntax and capabilities by 
querying the device for the latest information. Users can easily update the content in the SPIKE-Documentation folder to reflect newer versions of the firmware, ensuring continued compatibility.

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
