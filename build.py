#!/usr/bin/python
import os
import subprocess
import re
import argparse
from pathlib import Path
from moviepy import VideoFileClip, concatenate_videoclips
import concurrent.futures


def get_scene_line_numbers(filename):
    """Extract line numbers and scene names from the source file."""
    scene_positions = {}
    with open(filename, 'r') as f:
        for line_num, line in enumerate(f, 1):
            # Look for class definitions that might be scenes
            match = re.match(r'class\s+(\w+)\s*\([^)]*\bTTSScene\b[^)]*\)', line.strip())
            if match:
                scene_name = match.group(1)
                scene_positions[scene_name] = line_num
    return scene_positions

def build_scenes(filename, quality_params="qm", threads=6):
    """Build all scenes in the file using manim with 6 parallel threads."""
    scene_positions = get_scene_line_numbers(filename)
    scene_names = scene_positions.keys()

    def run_command(scene_name):
        """Run the manim command for a single scene."""
        cmd = ['manim', '-' + quality_params, filename, scene_name, '--disable_caching']
        subprocess.run(cmd, check=True)

    # Using ThreadPoolExecutor to handle parallel execution with 6 workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(run_command, name) for name in scene_names]
        # Wait for all futures to complete and propagate any exceptions
        for future in concurrent.futures.as_completed(futures):
            future.result()

def get_video_files(filename, quality_name="1080p60"):
    """Get all MP4 files for the given source file."""
    # Remove .py extension if present
    base_name = Path(filename).stem
    video_dir = Path(f'./media/videos/{base_name}/{quality_name}')
    return list(video_dir.glob('*.mp4'))

def get_scene_name_from_video(video_path):
    """Extract scene name from video filename."""
    # Manim typically names videos like Scene_Name.mp4
    return video_path.stem

def merge_videos(video_files, scene_positions, output_file, threads=6, quality_merge="medium"):
    """Merge videos based on their scene positions in the source file."""
    
    # Filter out video files whose scenes aren't in the current source file
    filtered_video_files = []
    for video_file in video_files:
        scene_name = get_scene_name_from_video(video_file)
        if scene_name in scene_positions:
            filtered_video_files.append(video_file)
        else:
            print(f"Skipping video {video_file.stem} (not in current scenes)")

    if not filtered_video_files:
        raise ValueError("No valid video files to merge after filtering.")

    # Sort video files based on their scene's line number
    filtered_video_files.sort(key=lambda x: scene_positions[get_scene_name_from_video(x)])
    
    # Load all video clips
    clips = [VideoFileClip(str(video_file)) for video_file in filtered_video_files]
    
    # Concatenate clips
    final_clip = concatenate_videoclips(clips, method="chain")
    
    # Write the final video
    final_clip.write_videofile(
        output_file,
        threads=threads,
        preset=quality_merge,
        codec="libx264"
    )
    
    # Close all clips
    for clip in clips:
        clip.close()

def main():
    parser = argparse.ArgumentParser(description='Build a file with specified quality.')
    parser.add_argument('filename', help='The name of the file to build')
    parser.add_argument('--quality', choices=['low', 'medium', 'high'], 
                        default='medium', help='Quality level (default: medium)')
    parser.add_argument('--threads', type=int, default=6, help='Number of CPU threads allocated to help render and merge')
    args = parser.parse_args()

    root = args.filename
    # Setup constants
    source_file = f"{root}.py"  # Replace with your file name
    output_file = f"{root}.mp4"
    

    threads = args.threads
    quality = args.quality

    quality_mapping = {
        "low": ("ql", "480p15", "ultrafast"),
        "high": ("qk", "2160p60", "veryslow"),
    }

    # Default to medium if not "low" or "high"
    quality_params, quality_name, quality_merge = quality_mapping.get(
        quality, 
        ("qh", "1080p60", "medium")  # Explicit medium default
    )

    try:
        # Step 1: Get line numbers for all scenes
        scene_positions = get_scene_line_numbers(source_file)
        
        # Step 2: Build all scenes
        print("Building scenes...")
        build_scenes(source_file, quality_params, threads)
        
        # Step 3: Get all video files
        video_files = get_video_files(source_file, quality_name)
        
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
