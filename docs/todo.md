# High-level TODO
- [x] Fix message getting reset issue
- [x] Make GUI
- [x] Make username.txt more restrictive
- [x] Ping to find users
  - [x] Display list of users
- [x] Colour
- [ ] Encryption

# Encryption TODO
- [ ] Update the way messages are sent or recieved. Messages are now a JSON packet to be intercepted and appended to the message history.
  - This JSON packet includes:
    - [ ] Username. Validity must be checked by peer, and by self to warn of illegal usernames.
    - [ ] Chat message
    - [ ] Time sent
    - [ ] Colour
- [ ] Encryption
  - JSON packet now includes:
    - Username (alr implemented by now)
    - [ ] Encrypted message
    - [ ] Encrypted test phrase
    - Time sent
    - Colour