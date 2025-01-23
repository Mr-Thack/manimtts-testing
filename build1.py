#!/usr/bin/python
import os
import subprocess
import re
from pathlib import Path
from moviepy import VideoFileClip, concatenate_videoclips

def get_scene_line_numbers(filename):
    """Extract line numbers and scene names from the source file."""
    scene_positions = {}
    with open(filename, 'r') as f:
        for line_num, line in enumerate(f, 1):
            # Look for class definitions that might be scenes
            match = re.match(r'class\s+(\w+)', line.strip())
            if match:
                scene_name = match.group(1)
                scene_positions[scene_name] = line_num
    return scene_positions

def build_scenes(filename):
    """Build all scenes in the file using manim."""
    cmd = ['manim', filename, '--write_all', '--disable_caching']
    subprocess.run(cmd, check=True)

def get_video_files(filename):
    """Get all MP4 files for the given source file."""
    # Remove .py extension if present
    base_name = Path(filename).stem
    video_dir = Path(f'./media/videos/{base_name}/1080p60')
    return list(video_dir.glob('*.mp4'))

def get_scene_name_from_video(video_path):
    """Extract scene name from video filename."""
    # Manim typically names videos like Scene_Name.mp4
    return video_path.stem

def merge_videos(video_files, scene_positions, output_file):
    """Merge videos based on their scene positions in the source file."""
    
    print(video_files)
    print(scene_positions)
    print(output_file)

    # Sort video files based on their scene's line number
    video_files.sort(key=lambda x: scene_positions[get_scene_name_from_video(x)])
    
    # Load all video clips
    clips = [VideoFileClip(str(video_file)) for video_file in video_files]
    
    # Concatenate clips
    final_clip = concatenate_videoclips(clips, method="compose")
    
    # Write the final video
    final_clip.write_videofile(output_file)
    
    # Close all clips
    for clip in clips:
        clip.close()

def main():
    root = "ASP"
    # Setup constants
    source_file = f"{root}.py"  # Replace with your file name
    output_file = f"{root}.mp4"
    
    try:
        # Step 1: Get line numbers for all scenes
        scene_positions = get_scene_line_numbers(source_file)
        
        # Step 2: Build all scenes
        print("Building scenes...")
        build_scenes(source_file)
        
        # Step 3: Get all video files
        video_files = get_video_files(source_file)
        
        if not video_files:
            print("No video files found!")
            return
        
        # Step 4: Merge videos
        print("Merging videos...")
        merge_videos(video_files, scene_positions, output_file)
        
        print(f"Successfully created {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
