# Release notes

## Latest Features (10/02/24)

### Simple Stuff (for you buffoons)

- Added encryption and other security measures.
- Chat messages are way more consistent now. There are almost no more issues.
- The app is generally more usable
- This new version is ***not*** compatible with earlier versions. Beware.
- Read [Encryption](README.md#encryption) in for info about how encryption works.
- Now comes with a free jpeg of floppa!

### Technical Stuff

- Re-wrote `network.py`
  - The user pinging function also grabs their IP, which is then used for TCP communication to ensure message arrival.
  - The listen function, the one that handles the message recieving now also checks for the validity of the message.
    - Is the username legal?
    - Are we using the same encryption key? (this is determined by decrypting a "test phrase" that was encrypted by the sender)
    - Is the colour prefix legal?
    - Also, messages are now json objects, and are formatted by the reciever instead of by the sender.
  - Messages are now stored in memory and not messages.txt. Also, users now only send a single message, and the recievers simply append it to their own history of messages. This is safer and less chaotic than before. Fun fact: you recieve your own message just like everybody else, your computer binds to itself lol. This is not an issue that needs to be fixed btw.
- Encrypting
  - I am using the enyo library, from which i just copy-pasted the code instead of manageing it through pip, to reduce the amount of dependencies. I also slightly edited it to my liking.
  - The encryption key is located in key.txt
- Extra
  - There are minor and negligible changes to the frontend
    - Slightly changed the handling of colour prefixes.
    - Changed some refresh intervals.