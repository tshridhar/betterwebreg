# BetterWebReg
An application created with the intent being a more user friendly version of UCI's WebReg site for personal use. Developed in Python with Selenium to automate tedious menu navigation. Currently being built incrementally.
### Background
WebReg is infamous among UCI students for being usable, but rather annoying and inconvenient. A brief look at the current site:
<img src='https://gyazo.com/7e64c7eba5ceefedc7be9105c61e1a20' title='Current WebReg' width='300' />

Things like the current study list, waitlist, and various options should always be available on the same menu. This application is being built with the intent of replacing the need to always have at least 3 tabs open (WebSoC, AntAlmanac, WebReg) and adding some QoL features.

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
- [ ] Alternative instruction set upon failure (e.g. class full, unit cap)
- [ ] If add directly after a drop fails, readd previous class to retain spot
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
