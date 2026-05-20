# A Simple Password Generator 🎲

Just a little Python script I wrote to generate random passwords. Nothing fancy, but it gets the job done.

## What's inside?

Three ready-to-use password strengths + an advanced mode where you can customize everything.

- **Weak passwords** - 6 characters, just letters and numbers
- **Medium passwords** - 12 characters, adds some symbols
- **Hard passwords** - 22 characters, full mix of everything
- **Custom generator** - you pick the length and what goes in it

Oh, and I removed confusing characters like `I`, `l`, `1`, and `0` so you don't mix them up when reading the password.

## How to use it

### The simple way:

```python
from password_generator import Generator, advance_generator

# Get a weak password (6 chars)
weak = Generator.generate_weak()

# Get a medium password (12 chars)
medium = Generator.generate_medium()

# Get a hard password (22 chars)
hard = Generator.generate_hard()