# ManimTTS-Testing
Welcome to my playground!

Here, I just experiment with Manim and TTS support over normal Manim.


# Installing Kokoro-TTS
Kokoro is the model I used for the Text-to-Speech Program. Kokoro is very capable and runs very fast.
It has only 82M parameters and many voice packs.
For these reasons, I chose Kokoro.


Run:
```zsh
pip install kokoro-tts 
```

Then run these or something equivalent:
```zsh
wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.json

wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx

```

* Keep this files in root directory of this git repo


#### For more information on Kokoro, go here:

https://github.com/nazdridoy/kokoro-tts 


