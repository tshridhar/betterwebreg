# BetterWebReg
An application created with the intent being a more user friendly version of UCI's WebReg site for personal use. Developed in Python with Selenium to automate tedious menu navigation. Currently being built incrementally.

---
### Features
#### Initial Focus
- [x] Basic Functionality
- [x] Instruction input via text file
- [x] Preservation of instruction order for complicated add/drop sets
- [ ] Basic UI
- [ ] UI input (make text file format secondary/optional)
- [ ] Full WebReg menu navigation
- [ ] View list of currently enrolled classes
- [ ] Retain session until manual logout (for use during peak hours)
#### Long Term
- [ ] Click to add classes (with advanced UI)
- [ ] Integrated class catalog (WebSoc)
- [ ] Viewable calendar (like AntAlmanac)
---
### Known Issues
- Lack of security. Credentials are sent with no protection, stored in main memory with no protection.
- No error checking built in. This application assumes the user input and WebReg side work with no issues.
---
### Changelog
- v0.3
	- Usable version with instruction order preservation
	- Changed input format to be more intuitive
	- Browser automatically closes upon completion
- v0.2
	- Class created to handle separate sessions
- v0.1
	- Proof of concept created with add/drop functionality, text file input
