import os
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Metaspace as PreTokenizersMetaspace
from tokenizers.normalizers import Sequence, NFD, Lowercase
from tokenizers.decoders import Metaspace as DecodersMetaspace


tokenizer = Tokenizer(BPE(unk_token="[UNK]"))

tokenizer.normalizer = Sequence([
    NFD(),
    Lowercase(),   
])

tokenizer.pre_tokenizer = PreTokenizersMetaspace(
    replacement="▁"
)

# Training
trainer = BpeTrainer(
    vocab_size=15_000,
    min_frequency=2,
    special_tokens=["[EOS]", "[UNK]", "[PAD]", "[CLS]", "[SEP]"]
)

print(f"Training tokenizer... on {len(os.listdir('./clean_codes/'))} files.")
tokenizer.train(
    files=[os.path.join("./clean_codes/", f) for f in os.listdir("./clean_codes/")],
    trainer=trainer
)


# Decoder
tokenizer.decoder = DecodersMetaspace(replacement="▁")

# Save tokenizer
tokenizer.save("./french_bpe_tokenizer.json")

print("End of training !")