# Bluetooth SDP Protocol Testing Tool

## Overview

This project is an experimental Bluetooth protocol testing utility intended for authorized security research, interoperability testing, and protocol analysis in controlled environments.

The tool establishes an L2CAP connection to a Bluetooth device and sends custom SDP (Service Discovery Protocol) test packets for observing device behavior, protocol handling, and error responses.

## Features

* Establishes Bluetooth L2CAP connections
* Sends custom SDP test messages
* Supports randomized payload generation for protocol robustness testing
* Useful for Bluetooth stack analysis and research
* Lightweight Python implementation

## Requirements

* Python 3.x
* PyBluez or a compatible Bluetooth library
* Bluetooth adapter with L2CAP support
* **Linux operating system**
* Appropriate permissions to access the local Bluetooth stack

## Limitations

* **Linux only:** The script was developed and tested on Linux systems and may not function correctly on Windows or macOS due to differences in Bluetooth stack implementations and library support.
* The tool requires the target device to support incoming L2CAP connections.
* Results may vary depending on the Bluetooth stack, firmware version, and operating system running on the tested device.
* Some devices restrict or reject SDP-related requests and may not respond as expected.
* Devices that only support a single active Bluetooth connection at a time may refuse additional connections while already paired or connected to another device.
* Devices capable of maintaining multiple simultaneous Bluetooth connections generally provide a more suitable environment for interoperability and protocol robustness testing.
* Bluetooth security settings, pairing requirements, and access controls may prevent successful communication.
* Performance and behavior can differ significantly between hardware vendors and Bluetooth versions.

## Compatibility

| Component | Support         |
| --------- | --------------- |
| Linux     | ✅ Supported     |
| Windows   | ❌ Not Supported |
| macOS     | ❌ Not Supported |

### Testing Environment

This project is intended for authorized Bluetooth protocol research, interoperability testing, and educational purposes in controlled environments. Always ensure you have permission to test any device involved in your experiments.


## Installation

```bash
pip install pybluez
```

## Usage

1. Configure the target device address.
2. Ensure you have authorization to test the target system.
3. Run the script:

```bash
python main.py
```

4. Monitor logs, packet captures, or device responses for analysis.

## Research Use Cases

* Bluetooth protocol learning
* SDP implementation testing
* Device interoperability validation
* Controlled laboratory security research
* Bluetooth stack behavior analysis

## Safety and Legal Notice

This software is intended solely for authorized testing, research, and educational purposes.

You must only use this tool against systems and devices that you own or for which you have explicit written permission to test. Unauthorized testing of third-party devices or networks may violate laws, regulations, terms of service, or organizational policies.

The authors assume no responsibility for misuse of this software.

## License

MIT License

