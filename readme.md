# Steam Screenshot Backup
This script copies (does not delete at source location) screenshots that were taken with the steam overlay.

## How to use
1. Check where you steam games are installed. Note that you can have multiple locations on different drives.
1. Create the destination folder
1. Run this script from console like this
    ```sh
    python3 steam_screenshot_backup.py --steamfolder 'C:/Games/Steam' --targetfolder 'C:/Users/Oshimani/Desktop/SteamScreenshots'

    # short version
    python3 steam_screenshot_backup.py -s 'C:/Games/Steam' -t 'C:/Users/Oshimani/Desktop/SteamScreenshots'
    ```