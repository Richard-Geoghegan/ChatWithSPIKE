 /*  chat.js
  *  Javascript with Firebase server connection. Makes everything work.
  *
  *  Developed by Richard Geoghegan (Pronounced Gay-ghun)
  *  Contact: rpgeoghegan@gmail.com
  *  Please alert me about any security vulnerabilities!
  */

/* Stores conversation as json */
var conversationHistory = [];

/* Store each command and its associated 'Run' button */
let runButtonCommandPairs = new Map ();

/* Delay for updating the ACE editor with the new console */
const updateConsoleDelay = 500;

/* This defines how long we wait before attempting to get
 * 'latestConsoleUpdate'. Sometimes console updates with 200ms delay between
 * updates. This ensures we get the entire "new" section after pressing run */
const monitorSerialDelay = 500;

/* Load initialConversation.json */
document.addEventListener("DOMContentLoaded", function() {
    fetch('json/initialConversation.json')
        .then(response => response.json())
        .then(data => {
            conversationHistory = data;
        })
        .catch(error => console.error("Failed to load initial prompts:", error));
});

/* Toggle console Ace Editor object */
document.getElementById('toggleConsole').addEventListener('click', function() {
    var consoleSection = document.getElementById('consoleOutputSection');
    var padding = document.getElementById('Padding');

    if (consoleSection.classList.contains('hidden')) {
        padding.classList.add('hidden');
        consoleSection.classList.remove('hidden');
        consoleSection.classList.remove('hidden');
        this.innerHTML = 'Hide Console <span class="glyphicon glyphicon-console"></span>'
        document.getElementById('toggleJson').classList.add('disabled')
        document.getElementById('toggleJson').disabled = true;

    } else {
        document.getElementById('toggleJson').disabled = false;
        document.getElementById('toggleJson').classList.remove('disabled');
        consoleSection.classList.add('hidden');
        padding.classList.remove('hidden');
        this.innerHTML = 'Show Console <span class="glyphicon glyphicon-console"></span>'
    }
});

/* Toggle JSON (conversation history view) */
document.getElementById('toggleJson').addEventListener('click', function() {
    var jsonSection = document.getElementById('jsonViewer');
    var padding = document.getElementById('Padding');

    if (jsonSection.classList.contains('hidden')) {
        padding.classList.add('hidden');
        jsonSection.classList.remove('hidden');
        jsonSection.classList.remove('hidden');
        this.textContent = 'Hide JSON';
        document.getElementById('toggleConsole').classList.add('disabled')
        document.getElementById('toggleConsole').disabled = true;
    } else {
        document.getElementById('toggleConsole').disabled = false;
        document.getElementById('toggleConsole').classList.remove('disabled');
        jsonSection.classList.add('hidden');
        padding.classList.remove('hidden');
        this.textContent = 'Show JSON';
    }
});

/* Display user message on key enter */
document.getElementById('userInput').addEventListener('keypress', function(event) {
    if (event.key === "Enter" && this.value.trim() !== "") {
        let userText = this.value;
        this.value = '';

        let chatBox = document.getElementById('chatBox');

        /* Inject HTML for bubble */
        let userBubble = `
        <div class="text-right">
            <div class="username-label">User</div>
            <div class="message-bubble user-message">${userText}</div>
        </div>`;
        chatBox.innerHTML += userBubble;
        chatBox.scrollTop = chatBox.scrollHeight;

        /* AI loading dots */
        let loadingId = "loading" + Math.random().toString(16).slice(2);
        let loadingDots = `<div id="${loadingId}" class="text-left loading-dots"><span>.</span><span>.</span><span>.</span></div>`;
        chatBox.innerHTML += loadingDots;
        chatBox.scrollTop = chatBox.scrollHeight;

        sendMessage(userText, loadingId);
    }
});

/* This handles what happens when you click the 'Run' button */
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('chatBox').addEventListener('click', function(event) {
        let target = event.target;
        while (target != this) {
            if (target.id.includes('run')) {
                let commandToWrite = runButtonCommandPairs.get(target.id);
                if (!(window.pyrepl && window.pyrepl.isActive)) {
                    alert("Please connect SPIKE before executing code!");
                    return;
                }
                else if (commandToWrite != null) {
                    window.pyrepl.write = commandToWrite;
                }

                setTimeout(() => {
                    monitor_serial();
                    latestConsoleUpdate = escapeHTML(latestConsoleUpdate);
                    let spikeBubble = `
                        <div class="text-right">
                            <div class="username-label">SPIKE</div>
                            <div class="message-bubble spike-message">${latestConsoleUpdate}</div>
                        </div>`;
                    chatBox.innerHTML += spikeBubble;
                    chatBox.scrollTop = chatBox.scrollHeight;
            
                    /* AI loading dots */
                    let loadingId = "loading" + Math.random().toString(16).slice(2);
                    let loadingDots = `<div id="${loadingId}" class="text-left loading-dots"><span>.</span><span>.</span><span>.</span></div>`;
                    chatBox.innerHTML += loadingDots;
                    chatBox.scrollTop = chatBox.scrollHeight;
            
                    sendMessage(latestConsoleUpdate, loadingId);
                }, monitorSerialDelay);

                console.log('Button clicked!');
                event.stopPropagation();
                return;
            }
            target = target.parentNode;
        }
    });
});

/* escape required special HTML characters */
function escapeHTML(str) {
    return str
        .replace(/&f/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}

/* Setup for console output */
var consoleEditor = ace.edit("consoleEditor");
consoleEditor.setTheme("ace/theme/chaos");
consoleEditor.session.setMode("ace/mode/text");
consoleEditor.session.setUseWrapMode(true);
consoleEditor.setReadOnly(true);
consoleEditor.setShowPrintMargin(false);

/* Stop motors when STOP pressed */
var buttonStop = document.getElementById("stop");
buttonStop.addEventListener("click", function () {
    window.pyrepl.stop;
    window.pyrepl.write = "import motor\nmotor.stop()"
})

/* Handle manually entering commands to the console */
document.getElementById("consoleInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        var input = document.getElementById('consoleInput').value;
        window.pyrepl.write = input;
        document.getElementById("consoleInput").value = "";
    }
});

/* LatestConsoleUpdate contains the section of the console after the latest
 * prompt */
let latestConsoleUpdate = "";
let command = "";
let updateTimeoutId = null;
let num_lines_in_repl = 0;

/* Update 'latestConsoleUpdate' with new section of console */
function monitor_serial() {
    if (window.pyrepl && window.pyrepl.isActive) {
        let consoleOut = window.pyrepl.read;
        let newLinesCount = consoleOut.length - num_lines_in_repl;

        if (newLinesCount > 0) {
            let newLines = consoleOut.slice(num_lines_in_repl).join("\n");

            latestConsoleUpdate = newLines;
            num_lines_in_repl = consoleOut.length;
        }
    }
}

var sent = false;

document.getElementById('documentation').disabled = true;
document.getElementById('documentation').classList.add('disabled');

/* Global variable to handle active documentation upload */
var activeUpload = false;

/* Gets new section of the console */
function updateConsole() {
    if (window.pyrepl && window.pyrepl.isActive) {

        if (!activeUpload) {
            document.getElementById('documentation').disabled = false;
            document.getElementById('documentation').classList.remove('disabled');
        }

        /* import required function every time SPIKE is connected */
        if (sent == false) {
            window.pyrepl.write = "from doc_function import doc";
            sent = true;
            setTimeout(() => {
                monitor_serial();
            }, 2000);
        }
        currLines = consoleEditor.session.getLength();

        let consoleOut = window.pyrepl.read;        
        let outputString;

        if (Array.isArray(consoleOut)) {
            outputString = consoleOut.join('\n');
        }

        if (outputString) {
            var isScrolledToBottom = consoleEditor.isRowFullyVisible
            (consoleEditor.session.getLength() - 1);
            var currentPosition = consoleEditor.getCursorPosition();

            consoleEditor.setValue(outputString);
            consoleEditor.moveCursorToPosition(currentPosition);
            consoleEditor.moveCursorTo(currLines);

            if (!isScrolledToBottom) {
                consoleEditor.moveCursorToPosition(currentPosition);
            } else {
                var numberOfLines = consoleEditor.session.getLength();
                consoleEditor.gotoLine(numberOfLines, 0, false);
            }
        }  
    }
}
setInterval(updateConsole, updateConsoleDelay);

/* Send to CEEO GPT-4 interface and update the ace editor */
function sendMessage(message, loadingId) {
    document.getElementById('userInput').disabled = true;

    conversationHistory.push({ "role": "user", "content": message });
    fetch("{YOUR CHATGPT API TOKEN GOES HERE}", {
        method: "POST",
        body: JSON.stringify({ messages: conversationHistory }),
        headers: { "Content-type": "application/json; charset=UTF-8" }
    })
    .then((res) => res.json())
    .then((res) => {
        if (res && res.response) {
            conversationHistory.push({ "role": "assistant", "content": res.response });
            
            command = extractFirstTripleSingleQuotedString(res.response);
            console.log(command);

            let message = res.response;
            document.getElementById(loadingId).remove();
            const codeBlockRegex = /```(?:python\s?)?(.*?)```/gs;
            const formattedMessage = message.replace(codeBlockRegex, (match, code) => `<code>${code}</code>`);

            const hasCode = message !== formattedMessage;
            var runId = "";

            /* Assign unique ID to each new 'run' button */
            let chatBox = document.getElementById('chatBox');
            if (hasCode) {
                runId = "run" + Math.random().toString(16).slice(2);
                runButtonCommandPairs.set(runId, command);
            }
            
            /* Display AI response */
            let aiBubble = `
            <div class="text-left">
                <div class="username-label">PrimeBot</div>
                <div class="message-bubble ai-message">${formattedMessage}${hasCode ? `<br><br><button id = "${runId}" class="btn run-message">Run Code</button>` : ''}</div>
            </div>
            `;
            
            chatBox.innerHTML += aiBubble;
            chatBox.scrollTop = chatBox.scrollHeight;
            document.getElementById('userInput').disabled = false;
        } else {
            console.error("Invalid response structure:", res);
        }
    })
    .catch((error) => {
        console.error("Error sending message:", error);
    });
}

/* Get command from chat */
function extractFirstTripleSingleQuotedString(response) {
    const tripleOrPythonQuotedStringRegex = /```(?:python\s?)?(.*?)```/gs;
    const matches = [...response.matchAll(tripleOrPythonQuotedStringRegex)];

    if (matches.length > 0) {
        return matches.map(match => match[1]).join('\n');
    }
    return null;
}

/* Displays the conversationHistory array */
function displayArrayContents(array) {
    const container = document.getElementById('jsonViewer');

    container.innerHTML = '';

    const listGroup = document.createElement('div');
    listGroup.className = 'list-group';

    array.forEach(item => {
        const listItem = document.createElement('a');
        listItem.className = 'list-group-item list-group-item-action';
        listItem.textContent = `${item.role}: ${item.content}`;
        listItem.href = "#";
        listGroup.appendChild(listItem);
    });

    container.appendChild(listGroup);
}

/* Updates the JSON container every 750ms */
setInterval(() => {
    displayArrayContents(conversationHistory);
}, 750);

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

/* Takes in an array of fileNames and their relative paths then uploads them 
 * to the device */
async function uploadFiles(fileNames) {
    activeUpload = true;
    document.getElementById('documentation').disabled = true;
    document.getElementById('documentation').classList.add('disabled');

    var docuementButton = document.getElementById('documentation');

    let loadingId = "loading" + Math.random().toString(16).slice(2);
    let loadingDots = `<div id="${loadingId}" class="text-left loading-dots"><span>.</span><span>.</span><span>.</span></div>`;
    docuementButton.innerHTML = loadingDots;


    const basePath = '/SPIKE-Documentation/'; 
    
    for (const fileName of fileNames) {
        const fileUrl = basePath + fileName;

        try {
            const response = await fetch(fileUrl);
            if (!response.ok) {
                throw new Error(`Failed to fetch ${fileName}: Status ${response.status}`);
            }
            const content = await response.text();
            console.log("File read successfully:", fileName);
            
            /* This is executed on SPIKE for every file uploaded */
            let pythonCode = `
import os

os.chdir('/flash')

if "modules" in "${fileName}":
    try:
        os.chdir("modules")
    except OSError:
        os.mkdir("modules")

os.chdir('/flash')

f = open("${fileName}", "w")
code = '''
${content}
'''
f.write(code)
f.close()

os.chdir('/flash')

print("SUCCESS:", "${fileName}")
`;

            window.pyrepl.write = pythonCode;

            let success = false;
            let output;
            let successMessage = `SUCCESS: ${fileName}`;
            let outputString;

            /* Check for succesful file upload before uploading next one */
            while (!success) {
                output = window.pyrepl.read;
                if (Array.isArray(output)) {
                    outputString = output.join('\n');
                }

                if (outputString.includes(successMessage)) {
                    success = true;
                } else {
                    /* NOTE: There is no timeout for this while loop, 
                     * here is where you should add one */
                    await sleep(200);
                }
            }

            } catch (error) {
                console.error('Error fetching or processing Python file:', fileName, error);
            }
    }
}

/* Single file for testing and debugging the code uploaer */
var file = ["doc_function.py"];

/* Add files and thier paths here to upload any additional documentation */
var files = ["doc_function.py", "doc_strings.py", "modules/color_matrix.py", 
"modules/color_sensor.py", "modules/distance_sensor.py",
"modules/force_sensor.py", "modules/hub.py", "modules/light_matrix.py", 
"modules/motor_pair.py", "modules/motor.py", "modules/runloop.py"];

/* Code for upload documentation button */
document.getElementById('documentation').addEventListener('click', function() {
    /* Change to contain array of file names */
    uploadFiles(files).then(() => {
        console.log('All files have been uploaded successfully.');
        window.pyrepl.write = "from doc_function import doc";

        document.getElementById('documentation').disabled = false;
        document.getElementById('documentation').classList.remove('disabled');
        activeUpload = false;

        var docuementButton = document.getElementById('documentation');

        docuementButton.innerHTML = `Upload Documentation <span class="glyphicon glyphicon-upload"></span>`;
    }).catch(error => {
        console.log('An error occurred during file upload:', error);
    });
});