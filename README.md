# FFmpeg App

This repository contains a Python script (`ffmpeg_operation.py`) that leverages FFmpeg to perform various media processing tasks, such as cutting videos, converting formats, merging files, extracting audio, and more.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/CodeRreaper69/ffmpeg_app
   cd ffmpeg_app
   ```

2. **Ensure FFmpeg is installed on your system:**

   - **Windows:**
     Download FFmpeg from the [official website](https://ffmpeg.org/download.html) and follow the installation instructions.
     Adding ffmpeg to path
     - Go to ffmpeg path an copy this path "ffmpeg-7.0.1-essentials_build\bin" to the envionment variables path, then 
   - **macOS:**
     ```sh
     brew install ffmpeg
     ```
   - **Linux:**
     ```sh
     bash run.sh
     
     ```
     # this will install all necessary files and packages, in one single command for Debian based users only

## Usage

To run the script, navigate to the directory containing `ffmpeg_operation.py` and execute it with Python:

```sh
cd ffmpeg_app
bash run.sh
```
# (or you can directly run the python file -
```
python3 ffmpeg_operation.py
```

The script will present a menu with various media processing options:

1. Cut Video
2. Convert Video
3. Merge Videos
4. Merge Audios
5. Extract Audio from Video
6. Resize Video
7. Add Watermark to Video
8. Extract Frames from Video
9. Adjust Video Speed
10. Add Subtitles to Video
11. Convert Audio Format
12. Create Video Slideshow from Images
13. Convert Video Format

Follow the on-screen prompts to provide the necessary inputs for the selected operation.

## Functions

### `get_media_info(file_path)`

Extracts media information using FFmpeg.

### `parse_media_info(media_info)`

Parses the media information to extract video and audio codec details and duration.

### `calculate_bitrate(target_size_mb, duration_seconds)`

Calculates the video bitrate for a target file size.

### `cut_video(input_file, start_time, end_time, output_file)`

Cuts a segment from a video file.

### `convert_video(input_file, target_size_mb, quality, output_file)`

Converts a video file to a specified size and quality.

### `merge_videos(input_files, output_file)`

Merges multiple video files into one.

### `merge_audios(input_files, output_file)`

Merges multiple audio files into one.

### `extract_audio(input_file, output_file)`

Extracts audio from a video file.

### `resize_video(input_file, width, height, output_file)`

Resizes a video to specified dimensions.

### `add_watermark(input_file, watermark_file, output_file, position="10:10")`

Adds a watermark to a video at the specified position.

### `extract_frames(input_file, frame_rate, output_pattern)`

Extracts frames from a video at a specified frame rate.

### `adjust_speed(input_file, speed, output_file)`

Adjusts the playback speed of a video.

### `add_subtitles(input_file, subtitle_file, output_file)`

Adds subtitles to a video.

### `convert_audio(input_file, output_file)`

Converts an audio file to a different format.

### `create_slideshow(image_pattern, frame_rate, output_file)`

Creates a video slideshow from a pattern of images.

### `convert_video_format(input_file, output_format, output_file)`

Converts a video file to a different format.

Enjoy using FFmpeg App!
