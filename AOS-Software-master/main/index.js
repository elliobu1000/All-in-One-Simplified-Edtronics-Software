const {BrowserWindow, app} = require('electron');
const path = require('path');


const createWindow = () => {
    const win = new BrowserWindow({
        width:1440,
        heaight:1024,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')

        }
    })
    win.loadFile("index.html")
}

app.whenReady().then(() =>{
    createWindow();
});

app.on('window-all-closed', ()=> {
    if (process.platform !== 'darwin') app.quit()
})

var nodeConsole = require('console');
var myConsole = new nodeConsole.Console(process.stdout, process.stderr);
myConsole.log('Hello World!');      