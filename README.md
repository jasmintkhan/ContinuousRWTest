# ContinuousRWTest

This repository contains a Python script to perform continuous read and write operations on hard drives (HDDs) and solid-state drives (SSDs) to test their performance and validity. The script writes and reads data until it reaches a target of 100,000 bytes (100 KB) and calculates the error rate to ensure the drive's reliability (passes if error rate is less than 10^-6).

## Features
- Continuous read and write operations
- Configurable timeout and target bytes
- Calculates and prints error rate per byte
- Handles keyboard interrupt to stop the test gracefully

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/jasmintkhan/ContinuousRWTest.git
2. Navigate to the repository directory:
   cd ContinuousRWTest
3. Run the script:
   py continuous_rw_test.py
