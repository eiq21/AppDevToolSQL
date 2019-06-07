const { app, BrowserWindow } = require("electron");
const url = require("url");
const path = require("path");
if (process.env.NODE_ENV !== "production") {
  require("electron-reload")(__dirname, {});
}
let mainWindow;
app.on("ready", () => {
  mainWindow = new BrowserWindow({
    webPreferences: {
      nodeIntegration: true
    }
  });
  mainWindow.webContents.openDevTools();
  mainWindow.loadURL(
    url.format({
      pathname: path.join(__dirname, "index.html"),
      protocol: "file:",
      slashes: true
    })
  );
});
