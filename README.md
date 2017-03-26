# eff-passphrase-generator

This is a simple passphrase generator.

It uses [Electronic Frontier Foundation](https://www.eff.org)'s long wordlist to create a passphrase according to the [dice-based guidelines provided by EFF](https://www.eff.org/dice).

## Installation
```bash
pip install eff_passphrase_generator
```

## Usage

From the command line:
```bash
eff-passphrase-generator
```

From package:
```bash
import eff_passphrase_generator
```

With prompt:
```
eff-passphrase-generator.passphrase()
```

Without prompt, where n is the number of words:
```
eff-passphrase-generator.get_passphrase(n)
```
