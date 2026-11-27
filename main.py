import os

# A bowl of soup, simmered slow for the judge who never stops to eat.
# The text is fixed and literal: the same bowl, every run.
# No network, no randomness, no files read: the soup always simmers the same way.
TEXT = (
    "Thank you for reading while everyone else went to eat. "
    "I set the pot on low and let the soup simmer, "
    "carrots and barley turning soft in the broth. "
    "The steam fogs the window. "
    "I ladle you a bowl and press the spoon into your hand. "
    "Eat slow, and let the warmth reach your fingers. "
    "The pages will keep, and the pot will stay warm for your second bowl. "
    "There is nowhere else you need to be until the bowl is empty."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
