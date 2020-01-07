# quick-meme

Simple Python script to generate a basic meme with text above an image.

DISCLAIMER: This was thrown together hastily and doesn't have much thought put
into it, so it would probably be best to do some simple modifications that I
mention below to make it nicer for you to interact with. Customization is the fun
part!

## How to use

```
python quick-meme.py <file name> <output file name> <font file> <meme text>
```

## Why?

Making a meme by hand with the modern style (text with a white background above
an image) is annoying, having the resize an image without modifying dimensions
becomes a pain. I figured this would be convenient for myself.


## Making more user friendly

The script accepts a font so the user can choose. If you don't care, go to [Google
Fonts](http://fonts.google.com) and download the first one. For practical use, I'd
recommend hiding this script behind another script like:

```bash
#!/bin/sh
python quick-meme.py $1 <font file> $2
```

This would make a nice abstraction to automatically call the script with the font
path already hidden, or you could add `#!/usr/bin/python` to the top of the file
and hardcode the path to your chosen font.

## Future

I might clean this script up a bit (mostly wanting to change the way that top and
bottom margins are dealt with, instead of a hardcoded value), and if I care to,
I might make a simple REST API so you could do something like `POST` a base64
encoded string and the desired text, and then receive a response with the base64
encoded resulting image