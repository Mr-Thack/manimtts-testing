import hashlib
import os
from KokoroTTS import KokoroTTS
from typing import Optional, Union, Callable
from manim import Scene, Animation, Mobject
from pathlib import Path
import soundfile as sf

def wav_file_length(path: str):
    f = sf.SoundFile(path)
    return f.frames / f.samplerate


class TTSScene(Scene):
    def __init__(self, **kwargs):
        """
        Initialize the TTSScene with TTS support.
        
        Args:
            tts_instance: Instance of TTS class for voice generation
            voice_cache_dir: Directory to store cached voice files
            **kwargs: Additional arguments passed to Scene
        """
        super().__init__(**kwargs)
        self.tts = KokoroTTS()
        self.voice_cache_dir = Path("./voices/")
        self.voice_cache_dir.mkdir(parents=True, exist_ok=True)

        self.set_voice("am_adam")

    def get_voices(self):
        return self.tts.get_voices()

    def set_voice(self, voice: str):
        self.voice = voice

    def get_voice_hash(self, message: str) -> str:
        """Generate a unique hash for a voice message."""
        return hashlib.md5((self.voice + message).encode('utf-8')).hexdigest()
    
    def get_voice_path(self, message: str) -> Path:
        """Get the cached voice file path for a message."""
        voice_hash = self.get_voice_hash(message)
        return self.voice_cache_dir / f"{voice_hash}.wav"
    
    def generate_voice(self, message: str) -> Path:
        """Generate or retrieve cached voice file for a message."""
        voice_path = self.get_voice_path(message)
        
        if not voice_path.exists():
            self.tts.save(self.voice, message, str(voice_path))
            
        return voice_path
    
    def add_voice(
        self,
        voice_message: str,
        *args,
        voice_offset: float = 0.0,
        voice_factor: float = 1.0,
        **kwargs
    ):
        # I think 90% of the actual length will account for pauses at the beggining and the end
        
        """
        Wait while playing a voice message.
        
        Args:
            voice_message: Text to be spoken
            min_time: Minimum wait time (in seconds)
            voice_offset: Time offset for voice playback (in seconds)
        """
        voice_path = self.generate_voice(voice_message)
        voice_length = wav_file_length(voice_path)

        # Add sound to the scene with offset
        self.add_sound(
            str(voice_path),
            time_offset=voice_offset
        )
       
        self.play(*args, **kwargs)

        self.wait((voice_length - voice_offset) * voice_factor)
