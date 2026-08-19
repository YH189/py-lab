# Message Encoder CLI

A command-line tool for encoding and decoding text messages using a configurable character shift, with layered input validation.

## Features
- Encode or decode messages using a shift value (1–25)
- Shift and text inputs validated independently before processing
- Strict mode available: rejects text containing non-letter characters
- Interactive CLI — prompts for message, shift value, and mode

## Usage


You'll be prompted for:
- a message to process
- a shift value (1–25)
- whether to encode (`E`) or decode (`d`)

The same shift value must be used for both encoding and decoding a given message.

## Notes

Validation logic is separated into `is_valid_shift()` and `is_valid_text()` functions rather than combined into a single check, keeping the core processing function easier to read and test independently.
