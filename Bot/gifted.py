from pygame import init, display, time, image, quit
from moviepy.editor import VideoFileClip

def display_home_video(video_path):
    # Load the video using moviepy
    video_clip = VideoFileClip(video_path)
    # Initialize Pygame
    init()
    # Set up the display
    screen = display.set_mode(video_clip.size)
    display.set_caption("Video Player")
    clock = time.Clock()
    running = True
    loop = 1
    while running:
        # Get the current time in milliseconds
        current_time = time.get_ticks()
        # Get the current frame of the video
        frame = video_clip.get_frame(current_time / 1000)
        # Convert the frame to a Pygame surface
        frame_surface = image.fromstring(frame.tobytes(), video_clip.size, 'RGB')
        # Display the current frame
        screen.blit(frame_surface, (0, 0))
        display.flip()
        clock.tick(30)  # Adjust the frame rate as needed
        # Check if the current time exceeds the duration of the video
        if abs(current_time - loop * video_clip.duration * 1000) < 200:
            # Reinitialize the video clip reader
            video_clip.reader.initialize()
            loop += 1

    quit()

