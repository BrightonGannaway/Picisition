from gensim.downloader import load
from gensim.models import KeyedVectors

# Load it using gensim's slow loader
model = load("glove-wiki-gigaword-100")

# Save to binary format
model.save("./glove_100d.kv")
