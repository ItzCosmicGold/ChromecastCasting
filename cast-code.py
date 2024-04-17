import time
import pychromecast
import pyautogui

def cast_screen(chromecast_name):
    chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[chromecast_name])
    if not chromecasts:
        print("Chromecast '{}' not found.".format(chromecast_name))
        return

    cast = chromecasts[0]
    cast.wait()

    mc = cast.media_controller
    mc.play_media("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4", "video/mp4")

    time.sleep(5)  # Wait for the media to start playing

    while True:
        # Capture screen and cast it
        screenshot = pyautogui.screenshot()
        mc.update_picture(screenshot)
        time.sleep(0.1)  # Adjust the refresh rate as needed

if __name__ == "__main__":
    chromecast_name = "ENTER NAME HERE."
    cast_screen(chromecast_name)
