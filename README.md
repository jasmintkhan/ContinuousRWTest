# ContinuousRWTest

This repository contains a **Python script** to perform continuous read and write operations on hard drives (HDDs) and solid-state drives (SSDs) to test their performance and validity. The script writes and reads data in a file until it reaches a target of 100,000 bytes (100 KB) written in total. Then, it calculates the error rate to ensure the drive's reliability.

## Motivation
I developed this script during my Comcast internship to **automate the testing process** for HDDs and SSDs. The goal was to determine how various frequencies and sound pressure levels (SPLs) affect the reliability of the drives in our company's data centers. By automating this process, I aimed to streamline the testing of dozens of different drives. Using the data collected with this script, I was able to determine which drives to utilize, ultimately **improving the reliability of our servers**.

## Features
- **Continuous Read and Write Operations**: Performs continuous read and write operations to test drive performance.
- **Configurable Test Parameters**: Easily edit file path and target bytes.
- **Error Rate Calculation**: Calculates and prints the error rate per byte to ensure drive reliability  (the drive passes if the error rate is less than 10<sup> -6</sup>).
- **Memory-Efficient**: The script loops over itself within the file, minimizing memory usage during the test.
- **Graceful Interrupt Handling**: Handles keyboard interrupts (**CTRL + C**) to stop the test gracefully.

## Memory-Efficient Design
One of the key features of this script is its memory-efficient design. Instead of writing to a new part of the file each time, the script loops over itself in the file. This approach minimizes the amount of memory the test consumes, making it suitable for both short and long-duration tests without consuming excessive disk space.

## Requirements
- Python 3.x

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/jasmintkhan/ContinuousRWTest.git
2. Navigate to the repository directory:
   ```sh
   cd ContinuousRWTest
4. Run the script:
   ```sh
   py continuous_read_write.py

## Impact
This script has been used to test dozens of different hard drives, providing invaluable data that has been instrumental in improving the reliability of the servers in our company's data centers. Previously, instability of the servers affected **hundreds of thousands of users**. By automating the testing process, we were able to efficiently identify issues and implement solutions to **enhance performance and stability**.
