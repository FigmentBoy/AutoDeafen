# AutoDeafen
Automatically deafens when your Geometry Dash percent passes a predetermined number without the use of a discord bot

### Security
The request to the server only exchanges the oauth code for a token and sends it back. I do it on my server to prevent my client secret from being leaked. You can see that I only authenticate with the 'rpc' scope so even if I had the token logged I wouldn't be able to do anything without being on the device with the discord client.

## Usage
Download the files and unzip the downloaded file. Download Python 3.8 if you don't have it already. Run `setup.bat`, then whenever you want to use it again you can just run `run.bat`.
