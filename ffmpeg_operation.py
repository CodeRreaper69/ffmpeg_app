import os
import subprocess
import re

def get_media_info(file_path):
    result = subprocess.run(['ffmpeg', '-i', file_path], stderr=subprocess.PIPE, text=True)
    return result.stderr

def parse_media_info(media_info):
    video_stream = re.search(r'Stream #\d+:\d+.*Video: (.*)', media_info)
    audio_stream = re.search(r'Stream #\d+:\d+.*Audio: (.*)', media_info)
    duration = re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)', media_info)

    video_codec = video_stream.group(1).split(',')[0] if video_stream else None
    audio_codec = audio_stream.group(1).split(',')[0] if audio_stream else None
    duration_seconds = int(duration.group(1)) * 3600 + int(duration.group(2)) * 60 + float(duration.group(3)) if duration else None

    return video_codec, audio_codec, duration_seconds

def calculate_bitrate(target_size_mb, duration_seconds):
    target_size_bits = target_size_mb * 8 * 1024 * 1024
    return (target_size_bits / duration_seconds) - 128 * 1024  # subtracting 128kbps for audio

def cut_video(input_file, start_time, end_time, output_file):
    ffmpeg_command = [
        'ffmpeg', '-i', input_file, 
        '-ss', start_time, '-to', end_time,
        '-c', 'copy', output_file
    ]
    subprocess.run(ffmpeg_command)
    print(f"Video cut complete. Saved as {output_file}")

def convert_video(input_file, target_size_mb, quality, output_file):
    media_info = get_media_info(input_file)
    video_codec, audio_codec, duration_seconds = parse_media_info(media_info)

    if not duration_seconds:
        print("Could not determine the duration of the video.")
        return

    video_bitrate = calculate_bitrate(target_size_mb, duration_seconds)
    audio_bitrate = 128  # default to 128kbps

    if quality == 'low':
        preset = 'fast'
    elif quality == 'medium':
        preset = 'medium'
    elif quality == 'high':
        preset = 'slow'
    else:
        print("Unknown quality. Defaulting to medium.")
        preset = 'medium'

    ffmpeg_command = [
        'ffmpeg', '-i', input_file, 
        '-vcodec', 'libx264', '-b:v', f'{int(video_bitrate/1000)}k',
        '-acodec', 'aac', '-b:a', f'{audio_bitrate}k',
        '-preset', preset, output_file
    ]

    subprocess.run(ffmpeg_command)
    print(f"Video conversion complete. Saved as {output_file}")

def merge_videos(input_files, output_file):
    with open('input.txt', 'w') as f:
        for file in input_files:
            f.write(f"file '{file}'\n")

    ffmpeg_command = [
        'ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'input.txt', '-c', 'copy', output_file
    ]
    subprocess.run(ffmpeg_command)
    os.remove('input.txt')
    print(f"Videos merged successfully. Saved as {output_file}")

def merge_audios(input_files, output_file):
    with open('input.txt', 'w') as f:
        for file in input_files:
            f.write(f"file '{file}'\n")

    ffmpeg_command = [
        'ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'input.txt', '-c', 'copy', output_file
    ]
    subprocess.run(ffmpeg_command)
    os.remove('input.txt')
    print(f"Audios merged successfully. Saved as {output_file}")

def extract_audio(input_file, output_file):
    ffmpeg_command = [
        'ffmpeg', '-i', input_file, '-q:a', '0', '-map', 'a', output_file
    ]
    subprocess.run(ffmpeg_command)
    print(f"Audio extracted successfully. Saved as {output_file}")

def resize_video(input_file, width, height, output_file):
    ffmpeg_command = [
        'ffmpeg', '-i', input_file, '-vf', f'scale={width}:{height}', output_file
    ]
    subprocess.run(ffmpeg_command)
    print(f"Video resized successfully. Saved as {output_file}")

def add_watermark(input_file, watermark_file, output_file, position="10:10"):
    ffmpeg_command = [
        'ffmpeg', '-i', input_file, '-i', watermark_file, 
        '-filter_complex', f'overlay={position}', output_file
    ]
    subprocess.run(ffmpeg_command)
    print(f"Watermark added successfully. Saved as {output_file}")

def extract_frames(input_file, frame_rate, output_pattern):
    ffmpeg_command = [
        'ffmpeg', '-i', input_file, '-vf', f'fps={frame_rate}', output_pattern
    ]
    subprocess.run(ffmpeg_command)
    print(f"Frames extracted successfully. Saved as {output_pattern}")

def adjust_speed(input_file, speed, output_file):
    ffmpeg_command = [
        'ffmpeg', '-i', input_file, '-filter:v', f'setpts={speed}*PTS', output_file
    ]
    subprocess.run(ffmpeg_command)
    print(f"Video speed adjusted successfully. Saved as {output_file}")

def add_subtitles(input_file, subtitle_file, output_file):
    ffmpeg_command = [
        'ffmpeg', '-i', input_file, '-vf', f'subtitles={subtitle_file}', output_file
    ]
    subprocess.run(ffmpeg_command)
    print(f"Subtitles added successfully. Saved as {output_file}")

def convert_audio(input_file, output_file):
    ffmpeg_command = [
        'ffmpeg', '-i', input_file, output_file
    ]
    subprocess.run(ffmpeg_command)
    print(f"Audio conversion complete. Saved as {output_file}")

def create_slideshow(image_pattern, frame_rate, output_file):
    ffmpeg_command = [
        'ffmpeg', '-framerate', str(frame_rate), '-pattern_type', 'glob', '-i', image_pattern, 
        '-c:v', 'libx264', '-r', '30', '-pix_fmt', 'yuv420p', output_file
    ]
    subprocess.run(ffmpeg_command)
    print(f"Slideshow created successfully. Saved as {output_file}")

def convert_video_format(input_file, output_format, output_file):
    ffmpeg_command = [
        'ffmpeg', '-i', input_file, f'{output_file}.{output_format}'
    ]
    subprocess.run(ffmpeg_command)
    print(f"Video format converted successfully. Saved as {output_file}.{output_format}")

def main():
    print("Choose an operation:")
    print("1. Cut Video")
    print("2. Convert Video")
    print("3. Merge Videos")
    print("4. Merge Audios")
    print("5. Extract Audio from Video")
    print("6. Resize Video")
    print("7. Add Watermark to Video")
    print("8. Extract Frames from Video")
    print("9. Adjust Video Speed")
    print("10. Add Subtitles to Video")
    print("11. Convert Audio Format")
    print("12. Create Video Slideshow from Images")
    print("13. Convert Video Format")
    
    choice = input("Enter the number of the operation you want to perform: ")

    if choice == '1':
        input_file = input("Enter the path to the input video file: ")
        start_time = input("Enter the start time (in hh:mm:ss or seconds): ")
        end_time = input("Enter the end time (in hh:mm:ss or seconds): ")
        output_file = input("Enter the desired output file name (with extension): ")
        cut_video(input_file, start_time, end_time, output_file)

    elif choice == '2':
        input_file = input("Enter the path to the input video file: ")
        target_size_mb = float(input("Enter the desired output size in MB: "))
        quality = input("Enter the desired quality (low, medium, high): ").strip().lower()
        output_file = input("Enter the desired output file name (with extension): ")
        convert_video(input_file, target_size_mb, quality, output_file)

    elif choice == '3':
        input_files = input("Enter the paths to the input video files, separated by spaces: ").split()
        output_file = input("Enter the desired output file name (with extension): ")
        merge_videos(input_files, output_file)

    elif choice == '4':
        input_files = input("Enter the paths to the input audio files, separated by spaces: ").split()
        output_file = input("Enter the desired output file name (with extension): ")
        merge_audios(input_files, output_file)

    elif choice == '5':
        input_file = input("Enter the path to the input video file: ")
        output_file = input("Enter the desired output file name (with extension): ")
        extract_audio(input_file, output_file)

    elif choice == '6':
        input_file = input("Enter the path to the input video file: ")
        width = input("Enter the desired width: ")
        height = input("Enter the desired height: ")
        output_file = input("Enter the desired output file name (with extension): ")
        resize_video(input_file, width, height, output_file)

    elif choice == '7':
        input_file = input("Enter the path to the input video file: ")
        watermark_file = input("Enter the path to the watermark image file: ")
        position = input("Enter the position of the watermark (format: x:y, default is 10:10): ") or "10:10"
        output_file = input("Enter the desired output file name (with extension): ")
        add_watermark(input_file, watermark_file, output_file, position)

    elif choice == '8':
        input_file = input("Enter the path to the input video file: ")
        frame_rate = input("Enter the frame rate (e.g., 1 for one frame per second): ")
        output_pattern = input("Enter the desired output file name pattern (e.g., frame_%04d.png): ")
        extract_frames(input_file, frame_rate, output_pattern)

    elif choice == '9':
        input_file = input("Enter the path to the input video file: ")
        speed = input("Enter the speed multiplier (e.g., 0.5 for half speed, 2 for double speed): ")
        output_file = input("Enter the desired output file name (with extension): ")
        adjust_speed(input_file, speed, output_file)

    elif choice == '10':
        input_file = input("Enter the path to the input video file: ")
        subtitle_file = input("Enter the path to the subtitle file: ")
        output_file = input("Enter the desired output file name (with extension): ")
        add_subtitles(input_file, subtitle_file, output_file)

    elif choice == '11':
        input_file = input("Enter the path to the input audio file: ")
        output_file = input("Enter the desired output file name (with extension): ")
        convert_audio(input_file, output_file)

    elif choice == '12':
        image_pattern = input("Enter the file pattern for the input images (e.g., 'images/*.jpg'): ")
        frame_rate = input("Enter the frame rate for the slideshow: ")
        output_file = input("Enter the desired output file name (with extension): ")
        create_slideshow(image_pattern, frame_rate, output_file)

    elif choice == '13':
        input_file = input("Enter the path to the input video file: ")
        output_format = input("Enter the desired output video format (e.g., mp4, mkv): ")
        output_file = input("Enter the desired output file name (without extension): ")
        convert_video_format(input_file, output_format, output_file)

if __name__ == "__main__":
    main()
