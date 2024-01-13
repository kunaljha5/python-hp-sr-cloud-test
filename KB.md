# OSI Layer General overview

```bash
+-------------------------------------------------------------------------------------------------------------------------+
| Layer Number | Layer Name          | Protocol                | Data Unit                  | Addressing                  |
+--------------|---------------------|-------------------------|----------------------------|-----------------------------+
| 7            | Application Layer   | HTTP, FTP, SMTP         | Data                       | Data (Data Link Layer)      |
| 6            | Presentation Layer  | SSL, TLS                | Data                       | N/A                         |
| 5            | Session Layer       | NetBIOS, RPC            | Data                       | N/A                         |
| 4            | Transport Layer     | TCP, UDP                | Segment                    | Port (Transport Layer)      |
| 3            | Network Layer       | IP                      | Packet                     | IP Address                  |
| 2            | Data Link Layer     | Ethernet, PPP, ARP      | Frame                      | MAC Address (Data Link)     |
| 1            | Physical Layer      | Ethernet, USB, Bluetooth| Bit                        | N/A                         |
+-------------------------------------------------------------------------------------------------------------------------+
```
