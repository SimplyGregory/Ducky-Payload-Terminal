# Ducky Payload Terminal 👋

Python tool for sending and receiving Ducky Script-style payloads over open ports and replaying them via local UI automation.

<img width="782" height="634" alt="Image" src="./ExampleImage.png" align="right" width="220" />

[![Language](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D4?style=flat-square&logo=windows&logoColor=white)](#)

---

## About This Project
<hr />

- `Receiver.py` listens on a TCP port and processes a small “Ducky Script”-style command set.
- `remote.py` is a simple client that can send a text payload to a target host.
- `Payload.txt` is a sample payload format.

## Authorization (Password)
<hr />

To reduce accidental execution while testing, the receiver enforces a basic password gate:

- Payloads must include a `PASSWORD <code>` line.
- If the password is missing or incorrect, the payload is canceled and no actions are executed.

`Payload.txt` includes an example `PASSWORD 0000` line.


## Contact
<hr />

- YouTube: https://www.youtube.com/@ModSpidr
- Portfolio: https://gregorybridges.dev
- Email: contact@gregorybridges.dev
